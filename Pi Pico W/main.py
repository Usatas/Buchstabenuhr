# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server
import json
import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests

class Buchstabenuhr():
    config ={}
    wlan_ssid =""
    wlan_password=""
    wlan_mode =""
    # LED Addresses
    # Reihe 1: 0 - 11
    ES_1 = list(range(0,2))
    C_1_1 = [2]
    IST_1 = list(range(3,6))
    C_1_2 = [6]
    FUENF_1=list(range(7,11))
    C_1_3 = [11]
    # Reihe 2: 12 - 23
    ZEHN_2 = list(range(12,16))
    C_2_1 = [16]
    ZWANZIG_2 = list(range(17,24))
    # Reihe 3: 24 - 35
    C_3_1 = [24]
    DREI_3 = list(range(25,29))
    VIERTEL_3 = list(range(29,36))
    # Reihe 4: 36 - 47
    VOR_4 = list(range(36,39))
    NACH_4 = list(range(39,43))
    C_4_1 = [43]
    HALB_4 = list(range(44,48))
    # Reihe 5: 48 - 59
    ELF_5 = list(range(48,51))
    C_5_1 = [51]
    ZEHN_5 = list(range(52,56))
    EINS_5 = list(range(56,60))
    # Reihe 6: 60 - 71
    C_6_1 = [60]
    NEUN_6 = list(range(61,65))
    C_6_2 = [65]
    SECHS_6 = list(range(66,71))
    C_6_3 = [71]
    # Reihe 7: 72 - 83
    DREI_7 = list(range(72,76))
    VIERTEL_7 = list(range(76,80))
    ACHT_7 = list(range(80,84))
    # Reihe 8: 84 - 95
    SIEBEN_8 = list(range(84,90))
    C_8_1 = [90]
    ZWOELF_8 = list(range(91,96))
    # Reihe 9: 96 - 107
    ZWEI_9 = list(range(96,100))
    FUENF_9 = list(range(100,104))
    C_9_1 = [104]
    UHR_9 = list(range(105,108))
    # Reihe 10: 108 - 111
    HERZ_MIN_10_1 = [108]
    HERZ_MIN_10_2 = [109]
    HERZ_MIN_10_3 = [110]
    HERZ_MIN_10_4 = [111]

    def __init__(self):
        print("Init Buchstabenuhr")
        self.load_config_from_file()
        self.apply_loaded_config()
        self.initialize_wlan()
          
    def save_config(self, config):    
        print("save the config file to flash")
        with open("config.json", "w") as configFile:
            json.dump(config, configFile)

    def set_config_to_default(self):
        print("setting config to default")
        self.config = {"wlan_ssid":"Buchstabenuhr",
        "wlan_password":"Buchstabenuhr",
        "wlan_mode":"host" }# create a network other clients can connect to 
        self.save_config(self.config)
        
    def load_config_from_file(self):
        # init config
        try: 
            print("load the config file from flash")
            with open("config.json", "r") as configFile:  # exception, it config does not exist
                print("config file found")
                self.config = json.load(configFile)
                print("config file loaded")
                print(self.config)
        except: # if not exist
            print("config.json does not exist")
            self.set_config_to_default()

        if self.config is None:
            self.set_config_to_default()
            
    def apply_loaded_config(self):
        self.wlan_ssid = self.config.get("wlan_ssid", "Buchstabenuhr") 
        self.wlan_password = self.config.get("wlan_password","Buchstabenuhr")
        self.wlan_mode = self.config.get("wlan_mode","host")
        self.save_config(self.config) # save the loaded config just in case there are some new keys with default values


            
    # Connect to network
    def connect_to_wlan(self,ssid, password,mode):
        print(f"connect_to_wlan: ssid: \"{ssid}\", password: \"{password}\", mode: \"{mode}\"")
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

    def initialize_wlan(self):
        self.connect_to_wlan(self.wlan_ssid, self.wlan_password, self.wlan_mode)
        if self.wlan.isconnected == False:
            print(f"Connecting to \"{self.wlan_ssid}\" faild - opening own access point \"Buchstabenuhr\"!")
            self.connect_to_wlan("Buchstabenuhr","Buchstabenuhr", "host")


    def setup__wlan_config_web_server(self):
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
    def interpret_time_to_led(self, current_time):
        if current_time is None:
            return False
        min = current_time.get("minute",-1)
        hour = current_time.get("hour",-1)
        if min <0 || hour <0:
            return False
        
        hearts = min %5
        on_leds = []
        # ES_1 IST_1
        on_leds += ES_1 + IST_1
        if min <10:
            # FUENF_1 NACH_4
            on_leds += FUENF_1 + NACH_4
        elif min <15:
            # ZEHN_2 NACH_4
            on_leds += ZEHN_2 + NACH_4
        elif min < 20:
            # VIERTEL_3 NACH_4
            on_leds += VIERTEL_3 + NACH_4
        alif min < 25:
            # ZWANZIG_2 NACH_4
            on_leds += ZWANZIG_2 + NACH_4
            
    # Example 1. Make a GET request for google.com and print HTML
    # Print the html content from google.com
    #print("1. Querying google.com:")
    #r = urequests.get("http://www.google.com")
    #print(r.content)
    #r.close()

    # Example 2. urequests can also handle basic json support! Let's get the current time from a server
    #print("\n\n2. Querying the current GMT+0 time:")
    #r = urequests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/Berlin") # Server that returns the current GMT+0 time.
    #print(r.json())

def main():
    uhr = Buchstabenuhr()

if __name__ == "__main__":
    main()
