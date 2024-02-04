from machine import Pin
import rp2
import time
import array


class LEDHandler():
    background_color = (0, 0, 0)
    foreground_color = (255, 255, 255)
    brightness = 0.1
    DISABLED = []
    NUM_LEDS = 325
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)
    WHITE = (255, 255, 255)
    COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

    def __init__(self, config_handler):
        print("LEDHandler init")
        self.config_handler = config_handler
        self.config = self.config_handler.config
        self.apply_loaded_config()


    def apply_loaded_config(self, config=None):
        if config is None:
            config = self.config_handler.config
        print("LEDHandler apply_loaded_config")
        self.brightness = self.config.get("brightness",100) # TODO Hier prüfen ob die Keys vorhanden sind
        self.PIN_NUM = self.config.get("pin_num",0)
        self.theLEDs = [0 for _ in range(self.NUM_LEDS)]

    def set_leds(self, value):
        if len(value) == 0:
            return

    def pixels_show(self):
        # dimmer_ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])
        # for i, c in enumerate(self.theLEDs):
        #     r = int(((c >> 8) & 0xFF) * self.brightness)
        #     g = int(((c >> 16) & 0xFF) * self.brightness)
        #     b = int((c & 0xFF) * self.brightness)
        #     dimmer_ar[i] = (g << 16) + (r << 8) + b
        time.sleep_ms(10)

    def pixels_set(self, i, color):
        self.theLEDs[i] = (color[1] << 16) + (color[0] << 8) + color[2]

    def pixels_fill_custom(self, on_leds, foreground_color, background_color):
        for i in range(len(self.theLEDs)):
            if i in on_leds:
                self.pixels_set(i, foreground_color)
            else:
                self.pixels_set(i, background_color)

    # prefered method
    def pixels_fill_and_show_expert_mode(self, on_leds, foreground_color, background_color, foreground_brightness, background_brightness):    
        dimmer_ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])    
        for i in range(len(self.theLEDs)):
            if i in on_leds:
                r = int(((foreground_color >> 8) & 0xFF) * foreground_brightness)
                g = int(((foreground_color >> 16) & 0xFF) * foreground_brightness)
                b = int((foreground_color & 0xFF) * foreground_brightness)
                dimmer_ar[i] = (g << 16) + (r << 8) + b
            else:
                if i in self.DISABLED:
                    r = int((((0, 0, 0) >> 8) & 0xFF) * 0)
                    g = int((((0, 0, 0) >> 16) & 0xFF) * 0)
                    b = int(((0, 0, 0) & 0xFF) * 0)
                    dimmer_ar[i] = (g<<16) + (r<<8) + b
                else:
                    r = int(((background_color >> 8) & 0xFF) * background_brightness)
                    g = int(((background_color >> 16) & 0xFF) * background_brightness)
                    b = int((background_color & 0xFF) * background_brightness)
                    dimmer_ar[i] = (g<<16) + (r<<8) + b
            
        # self.sm.put(dimmer_ar, 8)
        time.sleep_ms(10)

    def pixels_fill(self,on_leds):
        self.pixels_fill_custom(on_leds, self.foreground_color,self.background_color)

    def set_disabled_leds(self,DISABLED):
        self.DISABLED = DISABLED

    def pixels_fill_and_show_test(self):    
        dimmer_ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])    
        for c in self.COLORS:

            for i in range(len(self.theLEDs)):
                r = int(((c >> 8) & 0xFF) * 0.5)
                g = int(((c >> 16) & 0xFF) * 0.5)
                b = int((c & 0xFF) * 0.5)
                dimmer_ar[i] = (g<<16) + (r<<8) + b
            # self.sm.put(dimmer_ar, 8)
            time.sleep_ms(100)
