# Class that gets Network information and connects to a network if it doesn't work it host its own network
import json
import network  # handles connecting to WiFi
import urequests  # handles making and servicing network requests
import ure
import machine
import time
# import neopixel
import array, time
import rp2
import math

from ConfigHandler import Config
from RTCHandler import RTCHandler
from machine import Pin
from microdot import Microdot, Response

# Create a regular expression pattern for validating Wi-Fi credentials
ssid_pattern = ure.compile("^[a-zA-Z0-9_-]{1,32}$")
password_pattern = ure.compile("^.{8,}$")
html_content = """
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet"><title>WordClock Dashboard v0.1</title><style>@import url(https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap);:root{--color-primary:#6C9BCF;--color-danger:#FF0060;--color-success:#1B9C85;--color-warning:#F7D060;--color-white:#fff;--color-info-dark:#7d8da1;--color-dark:#363949;--color-light:rgba(132, 139, 200, 0.18);--color-dark-variant:#677483;--color-background:#f6f6f9;--card-border-radius:2rem;--border-radius-1:0.4rem;--border-radius-2:1.2rem;--card-padding:1.8rem;--padding-1:1.2rem;--box-shadow:0 2rem 3rem var(--color-light)}.dark-mode-variables{--color-background:#181a1e;--color-white:#202528;--color-dark:#edeffd;--color-dark-variant:#a3bdcc;--color-light:rgba(0, 0, 0, 0.4);--box-shadow:0 2rem 3rem var(--color-light)}*{margin:0;padding:0;outline:0;appearance:0;border:0;text-decoration:none;box-sizing:border-box}html{font-size:14px}body{width:100vw;height:100vh;font-family:Poppins,sans-serif;font-size:.88rem;user-select:none;overflow-x:hidden;color:var(--color-dark);background-color:var(--color-background)}a{color:var(--color-dark)}img{display:block;width:100%;object-fit:cover}h1{font-weight:800;font-size:1.8rem}h2{font-weight:600;font-size:1.4rem}h3{font-weight:500;font-size:.87rem}small{font-size:.76rem}p{color:var(--color-dark-variant)}b{color:var(--color-dark)}input{color:var(--color-dark);background:0}select{color:var(--color-dark);border-bottom:2px;background:0;width:80vw;max-width:400px}.hidden{display:none}.text-muted{color:var(--color-info-dark)}.primary{color:var(--color-primary)}.danger{color:var(--color-danger)}.success{color:var(--color-success)}.warning{color:var(--color-warning)}.container{display:grid;width:96%;margin:0 auto;gap:1.8rem;grid-template-columns:auto 23rem}main{margin:1.4rem 0}main .section{padding:0 0 50px 0}main .section{display:grid;grid-template-columns:repeat(2,1fr);gap:1.6rem}main .section>div{background-color:var(--color-white);padding:var(--card-padding);border-radius:var(--card-border-radius);margin-top:1rem;transition:all .3s ease}main .section>div:hover{box-shadow:var(--box-shadow)}main .card{display:flex;align-items:center;justify-content:space-between}main .colors .colorpicker{position:relative;width:92px;height:92px;border-radius:50%}#base_color,#night_mode_base_color,#night_mode_word_color,#word_color{position:relative;border:2px solid;border-radius:25px;height:50px;padding:0;width:50px;overflow:hidden}#base_color>input,#night_mode_base_color>input,#night_mode_word_color>input,#word_color>input{position:absolute;height:calc(100% + 8px);width:100%;opacity:0;cursor:pointer}main .slider{height:60px;padding:30px}main .sliders .rangeValue p{font-weight:800;font-size:1.8rem;color:var(--color-dark);width:50px}input[type=range]{-webkit-appearance:none!important;width:420px;height:2px;background:var(--color-dark)}input[type=range]::-webkit-slider-thumb{-webkit-appearance:none!important;width:30px;height:30px;background:var(--color-dark);border:2px solid var(--color-dark);border-radius:50%;cursor:pointer}input[type=range]::-webkit-slider-thumb:hover{background:var(--color-dark)}.text-input{position:relative}.text-input input{background:0;border:0;outline:0;width:80vw;max-width:400px;font-size:1.5em;transition:padding .3s .2s ease}.text-input input:focus+.line:after{transform:scaleX(1)}.text-input .line{width:100%;height:2px;position:absolute;bottom:-8px;background:#bdc3c7}.text-input .line:after{content:" ";position:absolute;float:right;width:100%;height:2px;transform:scalex(0);transition:transform .3s ease;background:var(--color-primary)}.right-section{margin-top:1.4rem}.right-section .nav{display:flex;justify-content:end;gap:2rem}.right-section .nav button{display:none}.night-mode,.right-section .dark-mode{background-color:var(--color-light);display:flex;justify-content:space-between;align-items:center;height:1.6rem;width:4.2rem;cursor:pointer;border-radius:var(--border-radius-1)}.night-mode span,.right-section .dark-mode span{font-size:1.2rem;width:50%;height:100%;display:flex;align-items:center;justify-content:center}.night-mode span.active,.right-section .dark-mode span.active{background-color:var(--color-primary);color:#fff;border-radius:var(--border-radius-1)}.right-section .nav .profile{display:flex;gap:2rem;text-align:right}.right-section .nav .profile .profile-photo{width:2.8rem;height:2.8rem;border-radius:50%;overflow:hidden}.right-section .user-profile{display:flex;justify-content:center;text-align:center;background-color:var(--color-white);padding:var(--card-padding);border-radius:var(--card-border-radius);cursor:pointer;transition:all .3s ease;margin:1rem 0 50px 0}.right-section .save-button:hover,.right-section .user-profile:hover{box-shadow:var(--box-shadow)}.right-section .user-profile img{width:11rem;height:auto;margin-bottom:.8rem;border-radius:50%}.right-section .user-profile h2{margin-bottom:.2rem}.right-section .save-button{display:flex;justify-content:center;text-align:center;padding:var(--card-padding);border-radius:var(--card-border-radius);background:var(--color-primary);color:var(--color-white);font-size:1.8rem;font-weight:800}.right-section .save-button:active{background:var(--color-dark);color:var(--color-white);box-shadow:none}.right-section .reminders{margin-top:2rem}.right-section .reminders .header{display:flex;align-items:center;justify-content:space-between;margin-bottom:.8rem}.right-section .reminders .header span{padding:10px;box-shadow:var(--box-shadow);background-color:var(--color-white);border-radius:50%}.right-section .reminders .notification{background-color:var(--color-white);display:flex;align-items:center;gap:1rem;margin-bottom:.7rem;padding:1.4rem var(--card-padding);border-radius:var(--border-radius-2);box-shadow:var(--box-shadow);cursor:pointer;transition:all .3s ease}.right-section .reminders .notification:hover{box-shadow:none}.right-section .reminders .notification .content{display:flex;justify-content:space-between;align-items:center;margin:0;width:100%}.right-section .reminders .notification .icon{padding:.6rem;color:var(--color-white);background-color:var(--color-success);border-radius:20%;display:flex}.right-section .reminders .notification.deactive .icon{background-color:var(--color-danger)}.right-section .reminders .add-reminder{background-color:var(--color-white);border:2px dashed var(--color-primary);color:var(--color-primary);display:flex;align-items:center;justify-content:center;cursor:pointer}.right-section .reminders .add-reminder:hover{background-color:var(--color-primary);color:#fff}.right-section .reminders .add-reminder div{display:flex;align-items:center;gap:.6rem}@media screen and (max-width:1200px){main .section{grid-template-columns:1fr;gap:0}}@media screen and (max-width:768px){.container{width:100%;grid-template-columns:1fr;padding:0 var(--padding-1)}main{margin-top:8rem;padding:0 1rem}main .sliders{position:relative;margin:3rem 0 0 0;width:100%}main .sliders p{width:100%;margin:0}.right-section{width:94%;margin:0 auto 4rem}.right-section .nav{position:fixed;top:0;left:0;align-items:center;padding:0 var(--padding-1);height:4.6rem;width:100%;z-index:2;margin:0}.right-section .nav .dark-mode{width:4.4rem;position:absolute;left:66%}}</style></head><body><div class="container"><!-- Main Content --><main><form action="/save" method="POST"><h1>Farben</h1><!-- Colors --><div class="colors section"><div><div class="card"><div><h3>Grundfarbe</h3><h1>Grundfarbe</h1></div><div class="colorpicker" id="base_color"><input type="color" value="#ffffff"></div></div></div><div><div class="card"><div><h3>Wortfarbe</h3><h1>Wortfarbe</h1></div><div class="colorpicker" id="word_color"><input type="color" value="#ffffff"></div></div></div></div><!-- End of Colors --><!-- Lumunation Sliders --><h1>Helligkeit</h1><div class="sliders section"><div><div class="card"><div><h3>Grundhelligkeit</h3><div class="rangeValue"><p id="baseLuminationRangeValue">50</p></div></div><div class="slider"><input id="baseLumination" type="range" min="0" max="100" value="50" oninput="baseLuminationRangeValue.innerText=this.value"></div></div></div><div><div class="card"><div><h3>Worthelligkeit</h3><div class="rangeValue"><p id="wordLuminationRangeValue">50</p></div></div><div class="slider"><input id="wordLumination" type="range" min="0" max="100" value="50" oninput="wordLuminationRangeValue.innerText=this.value"></div></div></div></div><!-- End of Lumination Sliders --><!-- Lumunation Sliders --><h1>Uhrzeit</h1><!-- Time and Zone --><div class="time section"><div><div class="card"><div><h3>Falls nicht automatisch erkannt</h3><h1>Uhrzeit</h1></div><div><input id="time" type="time"></div></div></div><div><div class="card"><div><h3>Zeitzone</h3><h1>Berlin</h1></div></div></div></div><!-- End of Time and Zone --><h1>WLAN</h1><div class="time section"><div><div class="card"><div><h3>SSID</h3><h1>SSID</h1></div><div class="text-input"><input id="ssid" type="text" placeholder="Was ist dein WLAN-Name?"><div class="line"></div></div></div></div><div><div class="card"><div><h3>Passwort</h3><h1>Passwort</h1></div><div class="text-input"><input id="password" type="password"><div class="line"></div></div></div></div></div><!-- End of Time and Zone --><h1>Nachtmodus aktivieren?</h1><div class="night-mode"><span class="material-icons-sharp active">light_mode </span><span class="material-icons-sharp">dark_mode</span></div><div id="night-mode-toggle"><h1>Nachtmodus: Uhrzeit</h1><!-- Time and Zone --><div class="time section"><div><div class="card"><div><h3>Nachtmodus</h3><h1>Start-Uhrzeit</h1></div><div><input id="night_mode_start_time" type="time"></div></div></div><div><div class="card"><div><h3>Nachtmodus</h3><h1>End-Uhrzeit</h1></div><div><input id="night_mode_end_time" type="time"></div></div></div></div><!-- End of Time and Zone --><h1>Nachtmodus: Farben</h1><!-- Colors --><div class="colors section"><div><div class="card"><div><h3>Grundfarbe</h3><h1>Grundfarbe</h1></div><div class="colorpicker" id="night_mode_base_color"><input type="color" value="#ffffff"></div></div></div><div><div class="card"><div><h3>Wortfarbe</h3><h1>Wortfarbe</h1></div><div class="colorpicker" id="night_mode_word_color"><input type="color" value="#ffffff"></div></div></div></div><!-- End of Colors --><!-- Lumunation Sliders --><h1>Nachmodus: Helligkeit</h1><div class="sliders section"><div><div class="card"><div><h3>Grundhelligkeit</h3><div class="rangeValue"><p id="night_mode_baseLuminationRangeValue">50</p></div></div><div class="slider"><input id="night_mode_baseLumination" type="range" min="0" max="100" value="50" oninput="night_mode_baseLuminationRangeValue.innerText=this.value"></div></div></div><div><div class="card"><div><h3>Worthelligkeit</h3><div class="rangeValue"><p id="night_mode_wordLuminationRangeValue">50</p></div></div><div class="slider"><input id="night_mode_wordLumination" type="range" min="0" max="100" value="50" oninput="night_mode_wordLuminationRangeValue.innerText=this.value"></div></div></div></div><!-- End of Lumination Sliders --></div></form></main><!-- End of Main Content --><!-- Right Section --><div class="right-section"><div class="nav"><div class="dark-mode"><span class="material-icons-sharp active">light_mode </span><span class="material-icons-sharp">dark_mode</span></div><div class="profile"><div class="info"><p>Hey, <b>Anna</b></p><small class="text-muted">Admin</small></div><div class="profile-photo"><!--<img src="images/profile-1.jpg">--></div></div></div><!-- End of Nav --><div class="user-profile"><div class="logo"><!--<img src="images/logo.jpg">--><h2>WordClock</h2><p>Web Interface</p></div></div><div class="save-button">Speichern</div></div></div><script>const darkMode = document.querySelector('.dark-mode');

        darkMode.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode-variables');
            darkMode.querySelector('span:nth-child(1)').classList.toggle('active');
            darkMode.querySelector('span:nth-child(2)').classList.toggle('active');
        })

        const nightMode = document.querySelector('.night-mode');
        const nightModeDiv = document.querySelector('#night-mode-toggle')

        nightMode.addEventListener('click', () => {
            console.log('We here')
            nightMode.classList.toggle('active');
            nightModeDiv.classList.toggle('hidden');
            nightMode.querySelector('span:nth-child(1)').classList.toggle('active');
            nightMode.querySelector('span:nth-child(2)').classList.toggle('active');
            
        })

        const baseColorDiv = document.querySelector('#base_color');
        const baseColorInput = document.querySelector('#base_color > input');
        const saveButton = document.querySelector('.save-button');

        const wordColorDiv = document.querySelector('#word_color');
        const wordColorInput = document.querySelector('#word_color > input');

        const baseLuminationInput = document.querySelector('#baseLumination');
        const wordLuminationInput = document.querySelector('#wordLumination');

        const nightModeBaseColorDiv = document.querySelector('#night_mode_base_color');
        const nightModeBaseColorInput = document.querySelector('#night_mode_base_color > input');

        const nightModeWordColorDiv = document.querySelector('#night_mode_word_color');
        const nightModeWordColorInput = document.querySelector('#night_mode_word_color > input');

        const nightModeBaseLuminationInput = document.querySelector('#night_mode_baseLumination');
        const nightModeWordLuminationInput = document.querySelector('#night_mode_wordLumination');


        const timeInput = document.querySelector('#time');
        const nightModeStartTimeInput = document.querySelector('#night_mode_start_time');
        const nightModeEndTimeInput = document.querySelector('#night_mode_end_time');
        const ssidInput = document.querySelector('#ssid');
        const passwordInput = document.querySelector('#password');



        baseColorInput.addEventListener('input', () => {
            baseColorDiv.style.backgroundColor = baseColorInput.value;
        });


        wordColorInput.addEventListener('input', () => {
            wordColorDiv.style.backgroundColor = wordColorInput.value;
        });

        nightModeBaseColorInput.addEventListener('input', () => {
            nightModeBaseColorDiv.style.backgroundColor = nightModeBaseColorInput.value;
        });


        nightModeWordColorInput.addEventListener('input', () => {
            nightModeWordColorDiv.style.backgroundColor = nightModeWordColorInput.value;
        });

        saveButton.addEventListener('click', () => {    

            var xhr = new XMLHttpRequest();
            xhr.open("POST", '/save', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify({
                background_color: baseColorInput.value,
                foreground_color: wordColorInput.value,
                background_brightness: baseLuminationInput.value,
                foreground_brightness: wordLuminationInput.value,
                time: timeInput.value,
                time_zone: 'Berlin',
                wlan_ssid: ssidInput.value,
                wlan_password: passwordInput.value,
                night_mode: nightMode.classList.contains('active'),
                night_mode_background_color: nightModeBaseColorInput.value,
                night_mode_foreground_color: nightModeWordColorInput.value,
                night_mode_background_brightness: nightModeBaseLuminationInput.value,
                night_mode_foreground_brightness: nightModeWordLuminationInput.value,
                night_mode_start_time: nightModeStartTimeInput.value,
                night_mode_end_time: nightModeEndTimeInput.value
            }));
        });</script></body></html>
"""

def time_obj_from_string(string):
    return {'hour': int(string.split(":")[0]), 'minute': int(string.split(":")[1])}

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
class NetworkHandler():

    def __init__(self):
        print("NetworkHandler init")
        self.config = Config()
        self.app = Microdot()
        self.app.route('/')(self.index) 
        self.app.route('/save', methods=['POST'])(self.handlePostRequest)
        self.wlan = None


    def connect_to_wlan(self):
        ssid = self.config.get("wlan_ssid")
        password = self.config.get("wlan_password")
        mode = self.config.get("wlan_mode")
        print(f'connect_to_wlan with loaded config: ssid: "{ssid}", password: "{password}",  mode: "{mode}"')

        if mode == "host":
            print(f'Opening WLAN "{ssid}"')
            self.wlan = network.WLAN(network.AP_IF)
            self.wlan.config(essid=ssid, password=password)
            self.wlan.active(True)
            while self.wlan.active == False:
                 time.sleep(0.5)
            print("Access point active")
            print(self.wlan.ifconfig())
        else:
            print(f'Conecting to WLAN "{ssid}"')
            self.wlan = network.WLAN(network.STA_IF)
            self.wlan.active(True)
            while self.wlan.active == False:
                time.sleep(0.5)
            self.wlan.connect(ssid, password)
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
            print(f'request_current_time: time_zone: "{time_zone}"')
            r = urequests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={time_zone}")  # https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/Berlin
            return r.json()
        except:
            print("Exception while requesting current time")
            return None
        
    def index(self, request):  
        return Response(html_content, headers={'Content-Type': 'text/html'})

    def getConfig(self, request):  
        return Response(json.dumps(self.config.get_config()), headers={'Content-Type': 'application/json'})

    def handlePostRequest(self, request):
            content_dict = json.loads(request.body)

            if content_dict is None:
                return Response("Error", headers={'Content-Type': 'text/html'})    
            
            print(content_dict)

            background_color = hex_to_rgb(content_dict.get("background_color", "0xFFFFFF"))
            foreground_color = hex_to_rgb(content_dict.get("foreground_color", "0xFFFFFF"))
            background_brightness = int(content_dict.get("background_brightness", "1")) / 100
            foreground_brightness = int(content_dict.get("foreground_brightness", "50")) / 100
                
            self.config.set("background_color", background_color)
            self.config.set("foreground_color", foreground_color)
            self.config.set("background_brightness", background_brightness)
            self.config.set("foreground_brightness", foreground_brightness)

            night_mode = bool(content_dict.get("night_mode", "True"))
            night_mode_background_color = hex_to_rgb(content_dict.get("night_mode_background_color", "0xFFFFFF"))
            night_mode_foreground_color = hex_to_rgb(content_dict.get("night_mode_foreground_color", "0xFFFFFF"))
            night_mode_background_brightness = int(content_dict.get("night_mode_background_brightness", "0")) / 100
            night_mode_foreground_brightness = int(content_dict.get("night_mode_foreground_brightness", "0")) / 100
            night_mode_start_time = content_dict.get("night_mode_start_time", "22:00")
            night_mode_end_time = content_dict.get("night_mode_end_time", "07:00")

            self.config.set("night_mode", night_mode)
            self.config.set("night_mode_background_color", night_mode_background_color)
            self.config.set("night_mode_foreground_color", night_mode_foreground_color)
            self.config.set("night_mode_background_brightness", night_mode_background_brightness)
            self.config.set("night_mode_foreground_brightness", night_mode_foreground_brightness)

            self.config.set("night_mode_start_time", time_obj_from_string(night_mode_start_time))
            self.config.set("night_mode_end_time", time_obj_from_string(night_mode_end_time))
            

            time = content_dict.get("time", "")
            if time:
                time_obj = time_obj_from_string(time)
                print(time_obj)
                rtc_handler = RTCHandler()
                rtc_handler.calibrate_rtc(time_obj)

            ssid = content_dict.get("wlan_ssid", "")
            password = content_dict.get("wlan_password", "")

            """if ssid_pattern.match(ssid) and password_pattern.match(password):
                self.config.set("wlan_ssid", ssid)
                self.config.set("wlan_password", password)
                self.config.set("wlan_mode", "client")
                self.config.save_config()
                machine.reset()"""

            self.config.save_config()
            return Response("OK", headers={'Content-Type': 'text/html'})

    async def run_webserver(self):
        print("run_webserver")
        await self.app.run()