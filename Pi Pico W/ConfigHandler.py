import json

class ConfigHandler():
    
    def __init__(self, filePath):
        print("ConfigHandler init")
        self.filePath = filePath
        self.config = {}
        self.default_config = {}
    
    def initialize_default_config(self, default_config):
        self.default_config= default_config

    def set_config_to_default(self):
        print("set config to default")
        self.config = self.default_config
        self.save_config(self.config)


    def save_config(self, config):    
        print("save the config file to flash")
        with open("config.json", "w") as configFile:
            json.dump(config, configFile)

        
    def load_config_from_file(self, filePath = None):
        # init config
        if filePath is None:
            filePath = self.filePath
        
        self.config = {}
        try: 
            print("load the config file from flash")
            with open("config.json", "r") as configFile:  # exception, it config does not exist
                print("config file found")
                self.config = json.load(configFile)
                print("config file loaded")
                print(self.config)
        except: # if not exist
            print("config.json does not exist")
            self.set_config_to_default()

        if self.config == {}:
            self.set_config_to_default()

        return self.config