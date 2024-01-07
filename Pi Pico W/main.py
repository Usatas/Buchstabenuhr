# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server
import json
import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests

config = None

def save_config(config):    
    print("save the config file to flash")
    with open("config.json", "w") as configFile:
        json.dump(config, configFile)

def set_default_config():
    print("setting config to default")
    config = {"wlan_ssid":"Buchstabenuhr",
    "wlan_password":"",
    "wlan_mode":"host" }# create a network other clients can connect to 
    return config

# init config
try: 
    print("load the config file from flash")
    with open("config.json", "r") as configFile:  # exception, it config does not exist
        print("config file found")
        config = json.load(configFile)
        print("config file loaded")
        print(config)
except: # if not exist
    print("config.json does not exist")
    config= set_default_config()
    save_config(config)

if config is None:
    config=set_default_config()
    save_config(config)

        

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Fill in your network name (ssid) and password here:
ssid = ''
password = ''
wlan.connect(ssid, password)


# Example 1. Make a GET request for google.com and print HTML
# Print the html content from google.com
print("1. Querying google.com:")
r = urequests.get("http://www.google.com")
print(r.content)
r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("\n\n2. Querying the current GMT+0 time:")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json())