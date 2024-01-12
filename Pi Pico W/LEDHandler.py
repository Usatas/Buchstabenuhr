class LEDHandler():
    def __init__(self, pin,amount_leds):
        self.pin = pin
        self.amount_leds = amount_leds

    def set_leds(self, value):
        if len(value) == 0:
            return