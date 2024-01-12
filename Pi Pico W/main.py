# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server


from ConfigHandler import ConfigHandler
from NetworkHandler import NetworkHandler
from RTCHandler import RTCHandler
from Buchstabenuhr import Buchstabenuhr
from LEDHandler import LEDHandler

LEDPIN = 25
AMOUNT_LEDS = 112*3 # 2 per letter and one (skipped) for space

def main():
    print("main")
    # TODO Load config from file
    config_handler = ConfigHandler("config.json")
    config_handler.load_config_from_file()
    # TODO Connect to network
    network_handler = NetworkHandler(config_handler)
    # TODO Initialize RCT
    rtc_handler = RTCHandler()
    led_handler = LEDHandler(LEDPIN, AMOUNT_LEDS)
    # TODO pass config, network and rtc to Buchstabenuhr
    uhr = Buchstabenuhr(config_handler, network_handler, rtc_handler,led_handler)
    # TODO run Buchstabenuhr
    try:
        uhr.calibrate_rtc()
        uhr.run()
    except:
        print("Exception while running Buchstabenuhr")
        # TODO Add handle of exceptions .. maybe blinking for 10s and restart 

if __name__ == "__main__":
    main()
