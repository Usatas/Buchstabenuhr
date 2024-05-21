import json

# class has to be a different name as file for singleton pattern
class Config():

    _instance = None
    _default_config = {"wlan_ssid": "Buchstabenuhr",
                      "wlan_password": "Buchstabenuhr",
                      "wlan_mode": "client",
                      "time_zone": "Europe/Berlin",
                      "max_brightness": 255/2,
                      "foreground_brightness": 0.5,
                      "background_brightness": 0.0,
                      "foreground_color": [255, 255, 255],
                      "background_color": [255, 255, 255],
                      "night_mode": True,
                      "night_mode_start_time": {'hour': 22, 'minute': 00},
                      "night_mode_end_time": {'hour': 7, 'minute': 00},
                      "night_mode_foreground_brightness": 0.0,
                      "night_mode_background_brightness": 0.0,
                      "night_mode_foreground_color": [255, 255, 255],
                      "night_mode_background_color": [255, 255, 255],
                      "available_time_zones": ["Europe/Berlin"]
                      }
    time_zone = ""

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.config = {}
            cls._instance.default_config = cls._default_config
        return cls._instance
    
    def set(self, key, value):
        self.config[key] = value


    def get(self, key):
        return self.config.get(key) or self.default_config.get(key)
    
    def get_config(self):
        return self.config

    def set_config_to_default(self):
        print("set config to default")
        self.config = self.default_config
        self.save_config()

    def save_config(self):
        print("save the config file to flash")
        with open("config.json", "w") as configFile:
            json.dump(self.config, configFile)

    def load_config_from_file(self):
        self.config = {}
        try:
            print("load the config file from flash")
            with open("config.json", "r") as configFile:  # exception, it config does not exist
                print("config file found")
                self.config = json.load(configFile)
                print("config file loaded")
                print(self.config)
        except:  # if not exist
            print("config.json does not exist")
            self.set_config_to_default()

        if self.config == {}:
            self.set_config_to_default()

        return self.config
