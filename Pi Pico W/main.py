import uasyncio as asyncio
import time
import machine

from ConfigHandler import Config
from NetworkHandler import NetworkHandler
from RTCHandler import RTCHandler
from BuchstabenuhrSquare import BuchstabenuhrSquare
from LEDHandler import LEDHandler

async def main():
    config_handler = Config()
    config_handler.load_config_from_file()
    led_handler = LEDHandler()
    led_handler.set_state(led_handler.STATE_WARNING)
    network_handler = NetworkHandler()
    is_connected = network_handler.connect_to_wlan()
    print(f"Connected to WLAN: {is_connected}")
    if not is_connected:
        print("Not connected to WLAN - wait 10s and try again")
        time.sleep(10)
        is_connected = network_handler.connect_to_wlan()
        print(f"Connected to WLAN: {is_connected}")
    rtc_handler = RTCHandler()
    uhr = BuchstabenuhrSquare(network_handler, rtc_handler, led_handler)
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

        asyncio.create_task(uhr.run())
        print(f"Web server started on http://{network_handler.wlan.ifconfig()[0]}:5000/")
        await network_handler.run_webserver()


    except OSError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Exception while running Buchstabenuhr: {e}")

    finally:
        led_handler.clear_all_pixels()
        led_handler.set_state(led_handler.STATE_ERROR)
        network_handler.wlan.disconnect()
        print("Disconnected from WLAN")
        print(network_handler.wlan.status())
        print(network_handler.wlan.isconnected())
        print(network_handler.wlan.ifconfig())
        print("End main try")
        time.sleep(1)
        print("Restarting")
        # machine.reset()

if __name__ == "__main__":
    asyncio.run(main())