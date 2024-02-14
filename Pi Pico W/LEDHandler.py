import machine, neopixel
import rp2
import time
import array


class LEDHandler():
    background_color = (0, 0, 0)
    foreground_color = (255, 255, 255)
    brightness = 0.1
    DISABLED = []
    NUM_LEDS = 11*2*10+4 # QlockTwo
    #NUM_LEDS = (12*2+11)*9+8+3 # BigBoyBuchstabenUhr
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)
    WHITE = (255, 255, 255)
    COLORS = [BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]
    PIN_NUM = 28

    def __init__(self, config_handler):
        print("LEDHandler init")
        self.config_handler = config_handler
        self.config = self.config_handler.config
        self.apply_loaded_config()
        
        self.neo_di = machine.Pin(28)
        self.leds = neopixel.NeoPixel(self.neo_di, self.NUM_LEDS)


    def apply_loaded_config(self, config=None):
        if config is None:
            config = self.config_handler.config
        print("LEDHandler apply_loaded_config")
        self.brightness = self.config.get("brightness",100) # TODO Hier prüfen ob die Keys vorhanden sind
        
    def set_max_brightness(self, max_brigthness):
        self.max_brigthness = max_brigthness
    
    def set_num_leds(self, num_leds):
        self.NUM_LEDS = num_leds
        self.leds = neopixel.NeoPixel(self.neo_di, self.NUM_LEDS)
    
    def set_leds_disabled(self, leds_disabled):
        self.DISABLED = leds_disabled

    def pixels_set(self, i, color):
        self.leds[i] = (color[1] << 16) + (color[0] << 8) + color[2]

    def pixels_fill_custom(self, on_leds, foreground_color, background_color):
        for i in range(len(self.theLEDs)):
            if i in on_leds:
                self.pixels_set(i, foreground_color)
            else:
                self.pixels_set(i, background_color)

    # prefered method
    def pixels_fill_and_show_expert_mode(self, on_leds, foreground_color, background_color, foreground_brightness, background_brightness):
        """
        Fills the specified LEDs with the given colors and brightness levels, and shows the updated LED display.

        Args:
            on_leds (list): A list of integers representing the indices of the LEDs to be turned on.
            foreground_color (int): The color of the foreground LEDs in RGB format (e.g., 0xFF0000 for red).
            background_color (int): The color of the background LEDs in RGB format.
            foreground_brightness (float): The brightness level of the foreground LEDs (0.0 to 1.0).
            background_brightness (float): The brightness level of the background LEDs (0.0 to 1.0).
        """
        # dimmer_ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])
        for i in range(self.NUM_LEDS):
            if i in on_leds:
                # r = int(((foreground_color[0] >> 8) & 0xFF) * foreground_brightness)
                # g = int(((foreground_color[1] >> 16) & 0xFF) * foreground_brightness)
                # b = int((foreground_color[2] & 0xFF) * foreground_brightness)

                # self.leds[i] = (g << 16) + (r << 8) + b
                self.leds[i] = foreground_color# * foreground_brightness
            else:
                if i in self.DISABLED:
                    # r = int(((0 >> 8) & 0xFF) * 0)
                    # g = int(((0 >> 16) & 0xFF) * 0)
                    # b = int((0 & 0xFF) * 0)
                    # self.leds[i] = (g << 16) + (r << 8) + b
                    self.leds[i] = (0,0,0)
                else:
                    # r = int(((background_color[0] >> 8) & 0xFF) * background_brightness)
                    # g = int(((background_color[1] >> 16) & 0xFF) * background_brightness)
                    # b = int((background_color[2] & 0xFF) * background_brightness)
                    # self.leds[i] = (g << 16) + (r << 8) + b
                    self.leds[i] = background_color# * background_brightness

        self.leds.write()
        time.sleep_ms(10)

    def pixels_fill(self,on_leds):
        self.pixels_fill_custom(on_leds, self.foreground_color,self.background_color)

    def set_disabled_leds(self,DISABLED):
        self.DISABLED = DISABLED


    def pixels_fill_and_show_test(self):
        """
        Fills the LED strip with colors from the COLORS list and shows the updated colors on the LEDs.

        This method iterates over the COLORS list and sets the color of each LED in the strip to a dimmed version of the color.
        The dimmed color is calculated by reducing the intensity of each RGB component by 50%.
        After setting the colors, the method updates the LEDs and waits for 1000 milliseconds before proceeding to the next color.
        """
        # dimmer_ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])
        for c in self.COLORS:
            for i in range(len(self.leds)):
                r = int(((c >> 8) & 0xFF) * 0.5)
                g = int(((c >> 16) & 0xFF)* 0.5) 
                b = int((c & 0xFF)* 0.5) 
                self.leds[i] = (g << 16) + (r << 8) + b
            self.leds.write()
            time.sleep_ms(1000)

    def ledtest(self):
        """
        Test function for controlling an LED strip.

        This function initializes the LED strip, sets the color of the first LED to red,
        and updates the LED strip to display the new color.
        """
        num_pixels = 12
        neo_di = machine.Pin(28)
        np = neopixel.NeoPixel(neo_di, num_pixels)
        
        np[0] = (255,0,0)
        np.write()