# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server


from ConfigHandler import ConfigHandler
from NetworkHandler import NetworkHandler
from RTCHandler import RTCHandler
from Buchstabenuhr import Buchstabenuhr
from LEDHandler import LEDHandler
import time

LEDPIN = 25
AMOUNT_LEDS = 112 * 3  # (108 letter + 4 hearts) * 2 LEDs per letter and one (skipped) for space

WLAN_DEFAUT = {
    "wlan_ssid": "Buchstabenuhr",
    "wlan_password": "Buchstabenuhr",
    "wlan_mode": "host"
}



def main():
    print("main")
    # TODO Load config from file
    config_handler = ConfigHandler("config.json")
    config_handler.load_config_from_file()
    # TODO Connect to network
    network_handler = NetworkHandler(config_handler)
    is_connected = network_handler.connect_to_wlan()
    print(f"Connected to WLAN: {is_connected}")
    if not is_connected:
        print("Not connected to WLAN - wait 10s and try again")
        time.sleep(10)
        is_connected = network_handler.connect_to_wlan()
        print(f"Connected to WLAN: {is_connected}")
    # TODO Initialize RCT
    rtc_handler = RTCHandler()
    led_handler = LEDHandler(config_handler)
    #led_handler.pixels_fill_and_show_test()
    # TODO pass config, network and rtc to Buchstabenuhr
    uhr = Buchstabenuhr(config_handler, network_handler, rtc_handler, led_handler)
    # TODO run Buchstabenuhr
    try:
        print("Start main try")

        print(f"Connected to WLAN: {network_handler.wlan.isconnected()}")
        network_handler.setup_web_server()
        if network_handler.wlan.isconnected():
            print("Connected to WLAN - load time from network")
            network_time = network_handler.request_current_time("Europe/Berlin")
            print (f"network_time: {network_time}")
            if network_time is not None:
                print("Calibrate RTC")
                rtc_handler.calibrate_rtc(network_time)
            else:
                print("No network time available")
        else:
            print("No network available - run offline")

        uhr.run()

    except Exception as e:
        print(f"Exception while running Buchstabenuhr: {e}")
        # TODO Add handle of exceptions .. maybe blinking for 10s and restart 


    finally:
        network_handler.wlan.disconnect()
        print("Disconnected from WLAN")
        print(network_handler.wlan.status())
        print(network_handler.wlan.isconnected())
        print(network_handler.wlan.ifconfig())
        print("End main try")

if __name__ == "__main__":
    main()
    print("end")