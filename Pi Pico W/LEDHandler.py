from machine import Pin
import rp2
import time
import array

class LEDHandler():
    background_color = (0, 0, 0)
    foreground_color = (255, 255, 255)
    brightness = 0.1
    def __init__(self, config_handler):
        print("LEDHandler init")
        self.config_handler = config_handler
        self.config = self.config_handler.config
        self.apply_loaded_config()
    
    @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)

    def ws2812(self):
        T1 = 2
        T2 = 5
        T3 = 3
        wrap_target()
        label("bitloop")
        out(x, 1)               .side(0)    [T3 - 1]
        jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
        jmp("bitloop")          .side(1)    [T2 - 1]
        label("do_zero")
        nop()                   .side(0)    [T2 - 1]
        wrap()
        
    def apply_loaded_config(self, config = None):
        if config is None:
            config = self.config_handler.config
        print("LEDHandler apply_loaded_config")
        self.brightness = self.config["brightness"]
        self.NUM_LEDS = self.config["num_leds"]
        self.PIN_NUM = self.config["pin_num"]
        self.theLEDs = [0 for _ in range(self.NUM_LEDS)]
        # Create the StateMachine with the ws2812 program, outputting on Pin(16).
        self.sm = rp2.StateMachine(0, self.ws2812, freq=8_000_000, sideset_base=Pin(self.PIN_NUM))
        self.sm.active(1)

    def set_leds(self, value):
        if len(value) == 0:
            return
        
    
    
    def pixels_show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])
        for i,c in enumerate(self.theLEDs):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g<<16) + (r<<8) + b
        self.sm.put(dimmer_ar, 8)
        time.sleep_ms(10)
    
    def pixels_set(self, i, color):
        self.theLEDs[i] = (color[1]<<16) + (color[0]<<8) + color[2]
    
    def pixels_fill_custom(self, on_leds, foreground_color, background_color):        
        for i in range(len(self.theLEDs)):
            if i in on_leds:
                self.pixels_set(i, foreground_color)
            else:
                self.pixels_set(i, background_color)

    def pixels_fill_and_show_expert_mode(self, on_leds, foreground_color, background_color, foreground_brightness, background_brightness):    
        dimmer_ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])    
        for i in range(len(self.theLEDs)):
            if i in on_leds:
                r = int(((foreground_color >> 8) & 0xFF) * foreground_brightness)
                g = int(((foreground_color >> 16) & 0xFF) * foreground_brightness)
                b = int((foreground_color & 0xFF) * foreground_brightness)
                dimmer_ar[i] = (g<<16) + (r<<8) + b
            else:
                r = int(((background_color >> 8) & 0xFF) * background_brightness)
                g = int(((background_color >> 16) & 0xFF) * background_brightness)
                b = int((background_color & 0xFF) * background_brightness)
                dimmer_ar[i] = (g<<16) + (r<<8) + b
            
        self.sm.put(dimmer_ar, 8)
        time.sleep_ms(10)

    def pixels_fill(self,on_leds):
        self.pixels_fill_custom(on_leds, self.foreground_color,self.background_color)