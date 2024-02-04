# Class that gets Network information and connects to a network if it doesn't work it host its own network
import json

try:
    import usocket as socket
except:
    import socket
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
            print(f"Connecting sucessfull: {self.wlan.isconnected()}")
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

    # Example 2. urequests can also handle basic json support! Let's get the current time from a server
    # print("\n\n2. Querying the current GMT+0 time:")
    # r = urequests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/Berlin") # Server that returns the current GMT+0 time.
    # print(r.json())

    # Set up a simple web server to handle Wi-Fi setup
    def setup_web_server(self):
        print("setup_web_server")
        html = """<!DOCTYPE html>
        <html>
        <head><title>Wi-Fi Setup</title></head>
        <body>
        <h1>Wi-Fi Setup</h1>
        <form action="/save" method="post">
            <label for="ssid">Wi-Fi SSID:</label>
            <input type="text" id="ssid" name="ssid" required><br>
            <label for="password">Wi-Fi Password:</label>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Save and Connect">
        </form>
        </body>
        </html>
        """
        html2 = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet"><title>WordClock Dashboard v0.1</title><style>@import url(https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap);:root{--color-primary:#6C9BCF;--color-danger:#FF0060;--color-success:#1B9C85;--color-warning:#F7D060;--color-white:#fff;--color-info-dark:#7d8da1;--color-dark:#363949;--color-light:rgba(132, 139, 200, 0.18);--color-dark-variant:#677483;--color-background:#f6f6f9;--card-border-radius:2rem;--border-radius-1:0.4rem;--border-radius-2:1.2rem;--card-padding:1.8rem;--padding-1:1.2rem;--box-shadow:0 2rem 3rem var(--color-light)}.dark-mode-variables{--color-background:#181a1e;--color-white:#202528;--color-dark:#edeffd;--color-dark-variant:#a3bdcc;--color-light:rgba(0, 0, 0, 0.4);--box-shadow:0 2rem 3rem var(--color-light)}*{margin:0;padding:0;outline:0;appearance:0;border:0;text-decoration:none;box-sizing:border-box}html{font-size:14px}body{width:100vw;height:100vh;font-family:Poppins,sans-serif;font-size:.88rem;user-select:none;overflow-x:hidden;color:var(--color-dark);background-color:var(--color-background)}a{color:var(--color-dark)}img{display:block;width:100%;object-fit:cover}h1{font-weight:800;font-size:1.8rem}h2{font-weight:600;font-size:1.4rem}h3{font-weight:500;font-size:.87rem}small{font-size:.76rem}p{color:var(--color-dark-variant)}b{color:var(--color-dark)}input{color:var(--color-dark);background:0}select{color:var(--color-dark);border-bottom:2px;background:0;width:80vw;max-width:400px}.text-muted{color:var(--color-info-dark)}.primary{color:var(--color-primary)}.danger{color:var(--color-danger)}.success{color:var(--color-success)}.warning{color:var(--color-warning)}.container{display:grid;width:96%;margin:0 auto;gap:1.8rem;grid-template-columns:auto 23rem}main{margin-top:1.4rem}main .section{padding:0 0 50px 0}main .section{display:grid;grid-template-columns:repeat(2,1fr);gap:1.6rem}main .section>div{background-color:var(--color-white);padding:var(--card-padding);border-radius:var(--card-border-radius);margin-top:1rem;transition:all .3s ease}main .section>div:hover{box-shadow:var(--box-shadow)}main .card{display:flex;align-items:center;justify-content:space-between}main .colors .colorpicker{position:relative;width:92px;height:92px;border-radius:50%}#base_color,#word_color{position:relative;border:2px solid;border-radius:25px;height:50px;padding:0;width:50px;overflow:hidden}#base_color>input,#word_color>input{position:absolute;height:calc(100% + 8px);width:100%;opacity:0;cursor:pointer}main .slider{height:60px;padding:30px}main .sliders .rangeValue p{font-weight:800;font-size:1.8rem;color:var(--color-dark);width:50px}input[type=range]{-webkit-appearance:none!important;width:420px;height:2px;background:var(--color-dark)}input[type=range]::-webkit-slider-thumb{-webkit-appearance:none!important;width:30px;height:30px;background:var(--color-dark);border:2px solid var(--color-dark);border-radius:50%;cursor:pointer}input[type=range]::-webkit-slider-thumb:hover{background:var(--color-dark)}.text-input{position:relative}.text-input input{background:0;border:0;outline:0;width:80vw;max-width:400px;font-size:1.5em;transition:padding .3s .2s ease}.text-input input:focus+.line:after{transform:scaleX(1)}.text-input .line{width:100%;height:2px;position:absolute;bottom:-8px;background:#bdc3c7}.text-input .line:after{content:" ";position:absolute;float:right;width:100%;height:2px;transform:scalex(0);transition:transform .3s ease;background:var(--color-primary)}.right-section{margin-top:1.4rem}.right-section .nav{display:flex;justify-content:end;gap:2rem}.right-section .nav button{display:none}.right-section .dark-mode{background-color:var(--color-light);display:flex;justify-content:space-between;align-items:center;height:1.6rem;width:4.2rem;cursor:pointer;border-radius:var(--border-radius-1)}.right-section .dark-mode span{font-size:1.2rem;width:50%;height:100%;display:flex;align-items:center;justify-content:center}.right-section .dark-mode span.active{background-color:var(--color-primary);color:#fff;border-radius:var(--border-radius-1)}.right-section .nav .profile{display:flex;gap:2rem;text-align:right}.right-section .nav .profile .profile-photo{width:2.8rem;height:2.8rem;border-radius:50%;overflow:hidden}.right-section .user-profile{display:flex;justify-content:center;text-align:center;background-color:var(--color-white);padding:var(--card-padding);border-radius:var(--card-border-radius);cursor:pointer;transition:all .3s ease;margin:1rem 0 50px 0}.right-section .save-button:hover,.right-section .user-profile:hover{box-shadow:var(--box-shadow)}.right-section .user-profile img{width:11rem;height:auto;margin-bottom:.8rem;border-radius:50%}.right-section .user-profile h2{margin-bottom:.2rem}.right-section .save-button{display:flex;justify-content:center;text-align:center;padding:var(--card-padding);border-radius:var(--card-border-radius);background:var(--color-primary);font-size:1.8rem;font-weight:800}.right-section .reminders{margin-top:2rem}.right-section .reminders .header{display:flex;align-items:center;justify-content:space-between;margin-bottom:.8rem}.right-section .reminders .header span{padding:10px;box-shadow:var(--box-shadow);background-color:var(--color-white);border-radius:50%}.right-section .reminders .notification{background-color:var(--color-white);display:flex;align-items:center;gap:1rem;margin-bottom:.7rem;padding:1.4rem var(--card-padding);border-radius:var(--border-radius-2);box-shadow:var(--box-shadow);cursor:pointer;transition:all .3s ease}.right-section .reminders .notification:hover{box-shadow:none}.right-section .reminders .notification .content{display:flex;justify-content:space-between;align-items:center;margin:0;width:100%}.right-section .reminders .notification .icon{padding:.6rem;color:var(--color-white);background-color:var(--color-success);border-radius:20%;display:flex}.right-section .reminders .notification.deactive .icon{background-color:var(--color-danger)}.right-section .reminders .add-reminder{background-color:var(--color-white);border:2px dashed var(--color-primary);color:var(--color-primary);display:flex;align-items:center;justify-content:center;cursor:pointer}.right-section .reminders .add-reminder:hover{background-color:var(--color-primary);color:#fff}.right-section .reminders .add-reminder div{display:flex;align-items:center;gap:.6rem}@media screen and (max-width:1200px){main .section{grid-template-columns:1fr;gap:0}}@media screen and (max-width:768px){.container{width:100%;grid-template-columns:1fr;padding:0 var(--padding-1)}main{margin-top:8rem;padding:0 1rem}main .sliders{position:relative;margin:3rem 0 0 0;width:100%}main .sliders p{width:100%;margin:0}.right-section{width:94%;margin:0 auto 4rem}.right-section .nav{position:fixed;top:0;left:0;align-items:center;padding:0 var(--padding-1);height:4.6rem;width:100%;z-index:2;margin:0}.right-section .nav .dark-mode{width:4.4rem;position:absolute;left:66%}}</style></head><body><div class="container"><main><form action="/save" method="POST"><h1>Farben</h1><div class="colors section"><div><div class="card"><div><h3>Grundfarbe</h3><h1>Grundfarbe</h1></div><div class="colorpicker" id="base_color"><input type="color"></div></div></div><div><div class="card"><div><h3>Wortfarbe</h3><h1>Wortfarbe</h1></div><div class="colorpicker" id="word_color"><input type="color"></div></div></div></div><h1>Helligkeit</h1><div class="sliders section"><div><div class="card"><div><h3>Grundhelligkeit</h3><div class="rangeValue"><p id="baseLuminationRangeValue">50</p></div></div><div class="slider"><input id="baseLumination" type="range" min="0" max="100" value="50" oninput="baseLuminationRangeValue.innerText=this.value"></div></div></div><div><div class="card"><div><h3>Worthelligkeit</h3><div class="rangeValue"><p id="wordLuminationRangeValue">50</p></div></div><div class="slider"><input id="wordLumination" type="range" min="0" max="100" value="50" oninput="wordLuminationRangeValue.innerText=this.value"></div></div></div></div><h1>Uhrzeit</h1><div class="time section"><div><div class="card"><div><h3>Falls nicht automatisch erkannt</h3><h1>Uhrzeit</h1></div><div><input id="time" type="time"></div></div></div><div><div class="card"><div><h3>Zeitzone</h3><h1>Berlin</h1></div></div></div></div><h1>WLAN</h1><div class="time section"><div><div class="card"><div><h3>SSID</h3><h1>SSID</h1></div><div class="text-input"><input id="ssid" type="text" placeholder="Was ist dein WLAN-Name?"><div class="line"></div></div></div></div><div><div class="card"><div><h3>Passwort</h3><h1>Passwort</h1></div><div class="text-input"><input id="password" type="password"><div class="line"></div></div></div></div></div></form></main><div class="right-section"><div class="nav"><div class="dark-mode"><span class="material-icons-sharp active">light_mode</span><span class="material-icons-sharp">dark_mode</span></div><div class="profile"><div class="info"><p>Hey,<b>Philip</b></p><small class="text-muted">Admin</small></div><div class="profile-photo"><img src="images/profile-1.jpg"></div></div></div><div class="user-profile"><div class="logo"><img src="images/logo.jpg"><h2>WordClock</h2><p>Web Interface</p></div></div><div class="save-button">Speichern</div></div></div><script>const darkMode = document.querySelector('.dark-mode');

        darkMode.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode-variables');
            darkMode.querySelector('span:nth-child(1)').classList.toggle('active');
            darkMode.querySelector('span:nth-child(2)').classList.toggle('active');
        })

        const baseColorDiv = document.querySelector('#base_color'); // #word_color > input
        const baseColorInput = document.querySelector('#base_color > input');
        const saveButton = document.querySelector('.save-button');

        const wordColorDiv = document.querySelector('#word_color'); // #word_color > input
        const wordColorInput = document.querySelector('#word_color > input');

        const baseLuminationInput = document.querySelector('#baseLumination');
        const wordLuminationInput = document.querySelector('#wordLumination');
        const timeInput = document.querySelector('#time');
        const ssidInput = document.querySelector('#ssid');
        const passwordInput = document.querySelector('#password');



        baseColorInput.addEventListener('input', () => {
            baseColorDiv.style.backgroundColor = baseColorInput.value;
        });


        wordColorInput.addEventListener('input', () => {
            wordColorDiv.style.backgroundColor = wordColorInput.value;
        });

        saveButton.addEventListener('click', () => {
            
            //also safe it as a cookie here?

            console.log({
                baseColor: baseColorInput.value,
                wordColor: wordColorInput.value,
                baseLumination: baseLuminationInput.value,
                wordLumination: wordLuminationInput.value,
                time: timeInput.value,
                timezone: 'Berlin',
                ssid: ssidInput.value,
                password: passwordInput.value
            })

            var xhr = new XMLHttpRequest();
            xhr.open("POST", '/save', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify({
                baseColor: baseColorInput.value,
                wordColor: wordColorInput.value,
                baseLumination: baseLuminationInput.value,
                wordLumination: wordLuminationInput.value,
                time: timeInput.value,
                timezone: 'Berlin',
                ssid: ssidInput.value,
                password: passwordInput.value
            }));
        });</script></body></html>"""
        # check if the device has alrady opened a web server
        # properly close the socket if it has been opened before
        if hasattr(self, "web_server_socket"):
            self.web_server_socket.close()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                server.bind(('0.0.0.0', 80))  # Replace 80 with your port number
                break
            except OSError as e:
                if e.errno == 98:  # EADDRINUSE
                    print("Port is already in use. Waiting before retrying...")
                    break
                elif e.errno == 5:  # EIO
                    print("Input/output error. Waiting before retrying...")
                    server.close()  # Close the socket
                    time.sleep(10)  # Wait for 10 seconds before retrying
                else:
                    raise  # Re-raise the exception if it's not EADDRINUSE or EIO

        server.listen(5)  # up to 5 connections at once
        print("Web server started on http://<your_pico_ip>/")
        try:
            while True:
                try:
                    print("Waiting for client to connect...")
                    conn, addr = server.accept()
                    print('Got a connection from %s' % str(addr))
                    request = conn.recv(1024)
                    request_str = request.decode("utf-8")
                    match = ure.match("POST /save HTTP/1.1", request_str)
                    print(f"request_str: {request_str}")
                    if match:
                        print("POST /save")
                        content_length_match = ure.search("Content-Length: (\\d+)", request_str)
                        print(f"content_length_match: {content_length_match}")
                        content_length = int(content_length_match.group(1))
                        print(f"content_length: {content_length}")
                        body = conn.recv(content_length)
                        print(f"body: {body}")
                        form_data = ujson.loads(body)
                        print(f"form_data: {form_data}")
                        ssid = form_data.get("ssid", "")
                        print(f"ssid: {ssid}")
                        password = form_data.get("password", "")
                        print(f"password: {password}")
                        if ssid_pattern.match(ssid) and password_pattern.match(password):
                            print(f"new credentials = {ssid}, {password}")
                            conn.sendall("HTTP/1.1 200 OK\r\n\r\nSaved Wi-Fi credentials. Rebooting...")
                            conn.close()
                            print("machine.reset()")
                            # machine.reset()
                        else:
                            print("Invalid Wi-Fi credentials.")
                            conn.sendall("HTTP/1.1 400 Bad Request\r\n\r\nInvalid Wi-Fi credentials.")
                            conn.close()
                    else:
                        print("GET /")

                        conn.send('HTTP/1.1 200 OK\n')
                        conn.send('Content-Type: text/html\n')
                        conn.send('Connection: close\n\n')
                        conn.sendall(html2)
                        # conn.sendall("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html.encode("utf-8"))
                        print("Sent HTML")
                        conn.close()
                except Exception as e:
                    print(f"Exception while handling client request: {e}")
                    conn.sendall("HTTP/1.1 500 Internal Server Error\r\n\r\n".encode("utf-8"))
                finally:
                    print("Closing client socket")
                    if conn is not None:
                        conn.close()
        except Exception as e:
            print(f"Exception while running web server: {e}")
        finally:
            server.close()
            print("Closed web server socket")
