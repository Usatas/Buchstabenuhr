from ConfigHandler import ConfigHandler
from NetworkHandler import NetworkHandler
from RTCHandler import RTCHandler
from BuchstabenuhrSquare import BuchstabenuhrSquare
from LEDHandler import LEDHandler
import time
import uasyncio as asyncio 
import machine

LEDPIN = 25
AMOUNT_LEDS = 112 * 3  # (108 letter + 4 hearts) * 2 LEDs per letter and one (skipped) for space

WLAN_DEFAUT = {
    "wlan_ssid": "Buchstabenuhr",
    "wlan_password": "Buchstabenuhr",
    "wlan_mode": "host"
}

def main():
    print("main")
    config_handler = ConfigHandler("config.json")
    config_handler.load_config_from_file()
    led_handler = LEDHandler(config_handler)
    led_handler.set_state(led_handler.STATE_WARNING)
    network_handler = NetworkHandler(config_handler)
    is_connected = network_handler.connect_to_wlan()
    print(f"Connected to WLAN: {is_connected}")
    if not is_connected:
        print("Not connected to WLAN - wait 10s and try again")
        time.sleep(10)
        is_connected = network_handler.connect_to_wlan()
        print(f"Connected to WLAN: {is_connected}")
    rtc_handler = RTCHandler()
    uhr = BuchstabenuhrSquare(config_handler, network_handler, rtc_handler, led_handler)
    try:
        print("Start main try")

        print(f"Connected to WLAN: {network_handler.wlan.isconnected()}")
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
        loop = asyncio.get_event_loop()
        loop.create_task(uhr.run())
        # loop.create_task(network_handler.startWebServer())
        # loop.run_until_complete(asyncio.gather(network_handler.startWebServer(), uhr.run()))
        loop.run_until_complete(asyncio.gather(uhr.run()))
        # loop.run_forever()

    except Exception as e:
        print(f"Exception while running Buchstabenuhr: {e}")

    finally:
        led_handler.set_state(led_handler.STATE_ERROR)
        network_handler.wlan.disconnect()
        print("Disconnected from WLAN")
        print(network_handler.wlan.status())
        print(network_handler.wlan.isconnected())
        print(network_handler.wlan.ifconfig())
        print("End main try")
        time.sleep(1)
        print("Restarting")
        machine.reset()

if __name__ == "__main__":
    main()