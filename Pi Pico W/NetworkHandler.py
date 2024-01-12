# Class that gets Network information and connects to a network if it doesn't work it host its own network
import json
import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests


class NetworkHandler():
    config ={}
    wlan_ssid =""
    wlan_password=""
    wlan_mode =""

    def __init__(self, config_handler):
        print("NetworkHandler init")
        self.config_handler = config_handler
        self.apply_loaded_config()

    def apply_loaded_config(self):
        self.config = self.config_handler.config
        self.wlan_ssid = self.config.get("wlan_ssid", "Buchstabenuhr") 
        self.wlan_password = self.config_handler.config.get("wlan_password","Buchstabenuhr")
        self.wlan_mode = self.config.get("wlan_mode","host")


    def connect_to_wlan(self,ssid="", password="",mode=""):
        print(f"connect_to_wlan: ssid: \"{ssid}\", password: \"{password}\", mode: \"{mode}\"")
        if ssid == "" or mode == "":
            
            print(f"connect_to_wlan with loaded config: ssid: \"{ssid}\", password: \"{password}\", mode: \"{mode}\"")
            ssid = self.wlan_ssid
            password = self.wlan_password
            mode = self.wlan_mode

        self.wlan_ssid = ssid
        self.wlan_password = password
        self.wlan_mode = mode
        if mode == "host":
            print(f"Opening WLAN \"{ssid}\"")
            self.wlan = network.WLAN(network.AP_IF)
            self.wlan.config( essid=ssid,password=password)
            self.wlan.active(True)
            while self.wlan.active ==False:
                pass
            print("Access point active")
            print(self.wlan.ifconfig())
        else:
            print(f"Conecting to WLAN \"{ssid}\"")
            self.wlan = network.WLAN(network.STA_IF)
            self.wlan.active(True)
            while self.wlan.active ==False:
                pass
            # Fill in your network name (ssid) and password here:
            self.wlan.connect(ssid, password)
            print(f"Connecting sucessfull: {self.wlan.isconnected()==True}")
            print(self.wlan.ifconfig())

        return self.wlan.isconnected()
    

    
    def request_available_time_zones(self):
         r = urequests.get(f"https://www.timeapi.io/api/TimeZone/AvailableTimeZones")
         return r.json()
         
    def request_current_time(self,time_zone):
        if self.wlan.isconnected == False:
            print("No network connection - unable to request time")
            return {"hour":-1,"min":-1}
        
        r = urequests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={time_zone}")
        return r.json()
    # Example 2. urequests can also handle basic json support! Let's get the current time from a server
    #print("\n\n2. Querying the current GMT+0 time:")
    #r = urequests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/Berlin") # Server that returns the current GMT+0 time.
    #print(r.json())
