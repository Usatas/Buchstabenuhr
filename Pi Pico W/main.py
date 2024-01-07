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


    def setup__wlan_config_web_server():
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