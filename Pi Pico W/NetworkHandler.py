# Class that gets Network information and connects to a network if it doesn't work it host its own network
import json
from microWebSrv import MicroWebSrv
import uasyncio as asyncio

import network  # handles connecting to WiFi
import urequests  # handles making and servicing network requests
import ure

import machine
import time
# import neopixel
import array, time
from machine import Pin
import rp2
import math

# Create a regular expression pattern for validating Wi-Fi credentials
ssid_pattern = ure.compile("^[a-zA-Z0-9_-]{1,32}$")
password_pattern = ure.compile("^.{8,}$")


class NetworkHandler():
    config = {}
    wlan_ssid = ""
    wlan_password = ""
    wlan_mode = ""

    def __init__(self, config_handler):
        print("NetworkHandler init")
        self.config_handler = config_handler
        self.apply_loaded_config()

    def apply_loaded_config(self):
        self.config = self.config_handler.config
        self.wlan_ssid = self.config.get("wlan_ssid", "Buchstabenuhr")
        self.wlan_password = self.config_handler.config.get("wlan_password", "Buchstabenuhr")
        self.wlan_mode = self.config.get("wlan_mode", "host")

    def connect_to_wlan(self, ssid="", password="", mode=""):
        print(f"connect_to_wlan: ssid: \"{ssid}\", mode: \"{mode}\"")
        if ssid == "" or mode == "":
            ssid = self.wlan_ssid
            password = self.wlan_password
            mode = self.wlan_mode
            print(f"connect_to_wlan with loaded config: ssid: \"{ssid}\",  mode: \"{mode}\"")

        self.wlan_ssid = ssid
        self.wlan_password = password
        self.wlan_mode = mode
        if mode == "host":
            print(f"Opening WLAN \"{ssid}\"")
            self.wlan = network.WLAN(network.AP_IF)
            self.wlan.config(essid=ssid, password=password)
            self.wlan.active(True)
            while self.wlan.active == False:
                pass
            print("Access point active")
            print(self.wlan.ifconfig())
        else:
            print(f"Conecting to WLAN \"{ssid}\"")
            self.wlan = network.WLAN(network.STA_IF)
            self.wlan.active(True)
            while self.wlan.active == False:
                pass
            # Fill in your network name (ssid) and password here:
            self.wlan.connect(ssid, password)
            print(f"Connecting successful: {self.wlan.isconnected()}")
            print(self.wlan.ifconfig())
        max_connection_time = 10  # Maximum time to wait for connection in seconds
        connection_time = 0
        while not self.wlan.isconnected() and connection_time < max_connection_time:
            # Wait until connected or max_connection_time is reached
            time.sleep(1)
            connection_time += 1

        return self.wlan.isconnected()

    def request_available_time_zones(self):
        try:
            print("request_available_time_zones")
            r = urequests.get(f"https://www.timeapi.io/api/TimeZone/AvailableTimeZones")
            return r.json()
        except:
            print("Exception while requesting available time zones")
            return None

    def request_current_time(self, time_zone):
        try:
            print(f"request_current_time: time_zone: \"{time_zone}\"")
            r = urequests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={time_zone}")
            return r.json()
        except:
            print("Exception while requesting current time")
            return None

    def handleGetRequest(self, httpClient, httpResponse):
        try:
            with open('index.html', 'r') as file:
                html_content = file.read()
            httpResponse.WriteResponseOk(headers=None, contentType='text/html', contentCharset='UTF-8', content=html_content)
        except:
            httpResponse.WriteResponseNotFound()

    # POST /save
    def handlePostRequest(self, httpClient, httpResponse):
        content = httpClient.ReadRequestContent()

        if content is not None:
            content_str = content.decode('utf-8')
            content_dict = json.loads(content_str)
            ssid = content_dict.get("ssid", "")
            password = content_dict.get("password", "")
            if ssid_pattern.match(ssid) and password_pattern.match(password):
                print(f"new credentials = {ssid}, {password}")
            httpResponse.WriteResponseJSONOk({"msg": "JSON data received"})
        else:
            httpResponse.WriteResponseBadRequest()

    # Webserver startfunction
    async def startWebServer(self):
        routeHandlers = [
            ('/', 'GET', self.handleGetRequest),
            ('/save', 'POST', self.handlePostRequest)
        ]
        mws = MicroWebSrv(routeHandlers=routeHandlers)
        mws.Start()
        print(f"Web server started on http://{self.wlan.ifconfig()[0]}:80/")