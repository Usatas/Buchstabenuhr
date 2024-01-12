import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests
import time

# LED Addresses
# Reihe 1: 0 - 11
ES_1 = list(range(0,2))
C_1_1 = [2]
IST_1 = list(range(3,6))
C_1_2 = [6]
FUENF_1=list(range(7,11))
C_1_3 = [11]
# Reihe 2: 12 - 23
ZEHN_2 = list(range(12,16))
C_2_1 = [16]
ZWANZIG_2 = list(range(17,24))
# Reihe 3: 24 - 35
C_3_1 = [24]
DREI_3 = list(range(25,29))
VIER_3 = list(range(29,33))
TEL_3 = list(range(33,36))
# Reihe 4: 36 - 47
VOR_4 = list(range(36,39))
NACH_4 = list(range(39,43))
C_4_1 = [43]
HALB_4 = list(range(44,48))
# Reihe 5: 48 - 59
ELF_5 = list(range(48,51))
C_5_1 = [51]
ZEHN_5 = list(range(52,56))
EIN_5 = list(range(56,59))
S_5 = [59]
# Reihe 6: 60 - 71
C_6_1 = [60]
NEUN_6 = list(range(61,65))
C_6_2 = [65]
SECHS_6 = list(range(66,71))
C_6_3 = [71]
# Reihe 7: 72 - 83
DREI_7 = list(range(72,76))
VIER_7 = list(range(76,80))
ACHT_7 = list(range(80,84))
# Reihe 8: 84 - 95
SIEBEN_8 = list(range(84,90))
C_8_1 = [90]
ZWOELF_8 = list(range(91,96))
# Reihe 9: 96 - 107
ZWEI_9 = list(range(96,100))
FUENF_9 = list(range(100,104))
C_9_1 = [104]
UHR_9 = list(range(105,108))
# Reihe 10: 108 - 111
HERZ_MIN_10_1 = [108]
HERZ_MIN_10_2 = [109]
HERZ_MIN_10_3 = [110]
HERZ_MIN_10_4 = [111]



class Buchstabenuhr():
    config ={}
    default_config = {"wlan_ssid":"Buchstabenuhr",
        "wlan_password":"Buchstabenuhr",
        "wlan_mode":"host",
        "time_zone":"Europe/Berlin",
        "available_time_zones":["Africa/Abidjan","Africa/Accra","Africa/Addis_Ababa","Africa/Algiers","Africa/Asmara","Africa/Asmera","Africa/Bamako","Africa/Bangui","Africa/Banjul","Africa/Bissau","Africa/Blantyre","Africa/Brazzaville","Africa/Bujumbura","Africa/Cairo","Africa/Casablanca","Africa/Ceuta","Africa/Conakry","Africa/Dakar","Africa/Dar_es_Salaam","Africa/Djibouti","Africa/Douala","Africa/El_Aaiun","Africa/Freetown","Africa/Gaborone","Africa/Harare","Africa/Johannesburg","Africa/Juba","Africa/Kampala","Africa/Khartoum","Africa/Kigali","Africa/Kinshasa","Africa/Lagos","Africa/Libreville","Africa/Lome","Africa/Luanda","Africa/Lubumbashi","Africa/Lusaka","Africa/Malabo","Africa/Maputo","Africa/Maseru","Africa/Mbabane","Africa/Mogadishu","Africa/Monrovia","Africa/Nairobi","Africa/Ndjamena","Africa/Niamey","Africa/Nouakchott","Africa/Ouagadougou","Africa/Porto-Novo","Africa/Sao_Tome","Africa/Timbuktu","Africa/Tripoli","Africa/Tunis","Africa/Windhoek","America/Adak","America/Anchorage","America/Anguilla","America/Antigua","America/Araguaina","America/Argentina/Buenos_Aires","America/Argentina/Catamarca","America/Argentina/ComodRivadavia","America/Argentina/Cordoba","America/Argentina/Jujuy","America/Argentina/La_Rioja","America/Argentina/Mendoza","America/Argentina/Rio_Gallegos","America/Argentina/Salta","America/Argentina/San_Juan","America/Argentina/San_Luis","America/Argentina/Tucuman","America/Argentina/Ushuaia","America/Aruba","America/Asuncion","America/Atikokan","America/Atka","America/Bahia","America/Bahia_Banderas","America/Barbados","America/Belem","America/Belize","America/Blanc-Sablon","America/Boa_Vista","America/Bogota","America/Boise","America/Buenos_Aires","America/Cambridge_Bay","America/Campo_Grande","America/Cancun","America/Caracas","America/Catamarca","America/Cayenne","America/Cayman","America/Chicago","America/Chihuahua","America/Coral_Harbour","America/Cordoba","America/Costa_Rica","America/Creston","America/Cuiaba","America/Curacao","America/Danmarkshavn","America/Dawson","America/Dawson_Creek","America/Denver","America/Detroit","America/Dominica","America/Edmonton","America/Eirunepe","America/El_Salvador","America/Ensenada","America/Fort_Nelson","America/Fort_Wayne","America/Fortaleza","America/Glace_Bay","America/Godthab","America/Goose_Bay","America/Grand_Turk","America/Grenada","America/Guadeloupe","America/Guatemala","America/Guayaquil","America/Guyana","America/Halifax","America/Havana","America/Hermosillo","America/Indiana/Indianapolis","America/Indiana/Knox","America/Indiana/Marengo","America/Indiana/Petersburg","America/Indiana/Tell_City","America/Indiana/Vevay","America/Indiana/Vincennes","America/Indiana/Winamac","America/Indianapolis","America/Inuvik","America/Iqaluit","America/Jamaica","America/Jujuy","America/Juneau","America/Kentucky/Louisville","America/Kentucky/Monticello","America/Knox_IN","America/Kralendijk","America/La_Paz","America/Lima","America/Los_Angeles","America/Louisville","America/Lower_Princes","America/Maceio","America/Managua","America/Manaus","America/Marigot","America/Martinique","America/Matamoros","America/Mazatlan","America/Mendoza","America/Menominee","America/Merida","America/Metlakatla","America/Mexico_City","America/Miquelon","America/Moncton","America/Monterrey","America/Montevideo","America/Montreal","America/Montserrat","America/Nassau","America/New_York","America/Nipigon","America/Nome","America/Noronha","America/North_Dakota/Beulah","America/North_Dakota/Center","America/North_Dakota/New_Salem","America/Nuuk","America/Ojinaga","America/Panama","America/Pangnirtung","America/Paramaribo","America/Phoenix","America/Port_of_Spain","America/Port-au-Prince","America/Porto_Acre","America/Porto_Velho","America/Puerto_Rico","America/Punta_Arenas","America/Rainy_River","America/Rankin_Inlet","America/Recife","America/Regina","America/Resolute","America/Rio_Branco","America/Rosario","America/Santa_Isabel","America/Santarem","America/Santiago","America/Santo_Domingo","America/Sao_Paulo","America/Scoresbysund","America/Shiprock","America/Sitka","America/St_Barthelemy","America/St_Johns","America/St_Kitts","America/St_Lucia","America/St_Thomas","America/St_Vincent","America/Swift_Current","America/Tegucigalpa","America/Thule","America/Thunder_Bay","America/Tijuana","America/Toronto","America/Tortola","America/Vancouver","America/Virgin","America/Whitehorse","America/Winnipeg","America/Yakutat","America/Yellowknife","Antarctica/Casey","Antarctica/Davis","Antarctica/DumontDUrville","Antarctica/Macquarie","Antarctica/Mawson","Antarctica/McMurdo","Antarctica/Palmer","Antarctica/Rothera","Antarctica/South_Pole","Antarctica/Syowa","Antarctica/Troll","Antarctica/Vostok","Arctic/Longyearbyen","Asia/Aden","Asia/Almaty","Asia/Amman","Asia/Anadyr","Asia/Aqtau","Asia/Aqtobe","Asia/Ashgabat","Asia/Ashkhabad","Asia/Atyrau","Asia/Baghdad","Asia/Bahrain","Asia/Baku","Asia/Bangkok","Asia/Barnaul","Asia/Beirut","Asia/Bishkek","Asia/Brunei","Asia/Calcutta","Asia/Chita","Asia/Choibalsan","Asia/Chongqing","Asia/Chungking","Asia/Colombo","Asia/Dacca","Asia/Damascus","Asia/Dhaka","Asia/Dili","Asia/Dubai","Asia/Dushanbe","Asia/Famagusta","Asia/Gaza","Asia/Harbin","Asia/Hebron","Asia/Ho_Chi_Minh","Asia/Hong_Kong","Asia/Hovd","Asia/Irkutsk","Asia/Istanbul","Asia/Jakarta","Asia/Jayapura","Asia/Jerusalem","Asia/Kabul","Asia/Kamchatka","Asia/Karachi","Asia/Kashgar","Asia/Kathmandu","Asia/Katmandu","Asia/Khandyga","Asia/Kolkata","Asia/Krasnoyarsk","Asia/Kuala_Lumpur","Asia/Kuching","Asia/Kuwait","Asia/Macao","Asia/Macau","Asia/Magadan","Asia/Makassar","Asia/Manila","Asia/Muscat","Asia/Nicosia","Asia/Novokuznetsk","Asia/Novosibirsk","Asia/Omsk","Asia/Oral","Asia/Phnom_Penh","Asia/Pontianak","Asia/Pyongyang","Asia/Qatar","Asia/Qostanay","Asia/Qyzylorda","Asia/Rangoon","Asia/Riyadh","Asia/Saigon","Asia/Sakhalin","Asia/Samarkand","Asia/Seoul","Asia/Shanghai","Asia/Singapore","Asia/Srednekolymsk","Asia/Taipei","Asia/Tashkent","Asia/Tbilisi","Asia/Tehran","Asia/Tel_Aviv","Asia/Thimbu","Asia/Thimphu","Asia/Tokyo","Asia/Tomsk","Asia/Ujung_Pandang","Asia/Ulaanbaatar","Asia/Ulan_Bator","Asia/Urumqi","Asia/Ust-Nera","Asia/Vientiane","Asia/Vladivostok","Asia/Yakutsk","Asia/Yangon","Asia/Yekaterinburg","Asia/Yerevan","Atlantic/Azores","Atlantic/Bermuda","Atlantic/Canary","Atlantic/Cape_Verde","Atlantic/Faeroe","Atlantic/Faroe","Atlantic/Jan_Mayen","Atlantic/Madeira","Atlantic/Reykjavik","Atlantic/South_Georgia","Atlantic/St_Helena","Atlantic/Stanley","Australia/ACT","Australia/Adelaide","Australia/Brisbane","Australia/Broken_Hill","Australia/Canberra","Australia/Currie","Australia/Darwin","Australia/Eucla","Australia/Hobart","Australia/LHI","Australia/Lindeman","Australia/Lord_Howe","Australia/Melbourne","Australia/North","Australia/NSW","Australia/Perth","Australia/Queensland","Australia/South","Australia/Sydney","Australia/Tasmania","Australia/Victoria","Australia/West","Australia/Yancowinna","Brazil/Acre","Brazil/DeNoronha","Brazil/East","Brazil/West","Canada/Atlantic","Canada/Central","Canada/Eastern","Canada/Mountain","Canada/Newfoundland","Canada/Pacific","Canada/Saskatchewan","Canada/Yukon","CET","Chile/Continental","Chile/EasterIsland","CST6CDT","Cuba","EET","Egypt","Eire","EST","EST5EDT","Etc/GMT","Etc/GMT-0","Etc/GMT-1","Etc/GMT-10","Etc/GMT-11","Etc/GMT-12","Etc/GMT-13","Etc/GMT-14","Etc/GMT-2","Etc/GMT-3","Etc/GMT-4","Etc/GMT-5","Etc/GMT-6","Etc/GMT-7","Etc/GMT-8","Etc/GMT-9","Etc/GMT+0","Etc/GMT+1","Etc/GMT+10","Etc/GMT+11","Etc/GMT+12","Etc/GMT+2","Etc/GMT+3","Etc/GMT+4","Etc/GMT+5","Etc/GMT+6","Etc/GMT+7","Etc/GMT+8","Etc/GMT+9","Etc/GMT0","Etc/Greenwich","Etc/UCT","Etc/Universal","Etc/UTC","Etc/Zulu","Europe/Amsterdam","Europe/Andorra","Europe/Astrakhan","Europe/Athens","Europe/Belfast","Europe/Belgrade","Europe/Berlin","Europe/Bratislava","Europe/Brussels","Europe/Bucharest","Europe/Budapest","Europe/Busingen","Europe/Chisinau","Europe/Copenhagen","Europe/Dublin","Europe/Gibraltar","Europe/Guernsey","Europe/Helsinki","Europe/Isle_of_Man","Europe/Istanbul","Europe/Jersey","Europe/Kaliningrad","Europe/Kiev","Europe/Kirov","Europe/Kyiv","Europe/Lisbon","Europe/Ljubljana","Europe/London","Europe/Luxembourg","Europe/Madrid","Europe/Malta","Europe/Mariehamn","Europe/Minsk","Europe/Monaco","Europe/Moscow","Europe/Nicosia","Europe/Oslo","Europe/Paris","Europe/Podgorica","Europe/Prague","Europe/Riga","Europe/Rome","Europe/Samara","Europe/San_Marino","Europe/Sarajevo","Europe/Saratov","Europe/Simferopol","Europe/Skopje","Europe/Sofia","Europe/Stockholm","Europe/Tallinn","Europe/Tirane","Europe/Tiraspol","Europe/Ulyanovsk","Europe/Uzhgorod","Europe/Vaduz","Europe/Vatican","Europe/Vienna","Europe/Vilnius","Europe/Volgograd","Europe/Warsaw","Europe/Zagreb","Europe/Zaporozhye","Europe/Zurich","GB","GB-Eire","GMT","GMT-0","GMT+0","GMT0","Greenwich","Hongkong","HST","Iceland","Indian/Antananarivo","Indian/Chagos","Indian/Christmas","Indian/Cocos","Indian/Comoro","Indian/Kerguelen","Indian/Mahe","Indian/Maldives","Indian/Mauritius","Indian/Mayotte","Indian/Reunion","Iran","Israel","Jamaica","Japan","Kwajalein","Libya","MET","Mexico/BajaNorte","Mexico/BajaSur","Mexico/General","MST","MST7MDT","Navajo","NZ","NZ-CHAT","Pacific/Apia","Pacific/Auckland","Pacific/Bougainville","Pacific/Chatham","Pacific/Chuuk","Pacific/Easter","Pacific/Efate","Pacific/Enderbury","Pacific/Fakaofo","Pacific/Fiji","Pacific/Funafuti","Pacific/Galapagos","Pacific/Gambier","Pacific/Guadalcanal","Pacific/Guam","Pacific/Honolulu","Pacific/Johnston","Pacific/Kanton","Pacific/Kiritimati","Pacific/Kosrae","Pacific/Kwajalein","Pacific/Majuro","Pacific/Marquesas","Pacific/Midway","Pacific/Nauru","Pacific/Niue","Pacific/Norfolk","Pacific/Noumea","Pacific/Pago_Pago","Pacific/Palau","Pacific/Pitcairn","Pacific/Pohnpei","Pacific/Ponape","Pacific/Port_Moresby","Pacific/Rarotonga","Pacific/Saipan","Pacific/Samoa","Pacific/Tahiti","Pacific/Tarawa","Pacific/Tongatapu","Pacific/Truk","Pacific/Wake","Pacific/Wallis","Pacific/Yap","Poland","Portugal","PRC","PST8PDT","ROC","ROK","Singapore","Turkey","UCT","Universal","US/Alaska","US/Aleutian","US/Arizona","US/Central","US/East-Indiana","US/Eastern","US/Hawaii","US/Indiana-Starke","US/Michigan","US/Mountain","US/Pacific","US/Samoa","UTC","W-SU","WET","Zulu"]
        }
    time_zone =""

    def __init__(self,config_handler, network_handler, rtc_handler,led_handler):
        print("Init Buchstabenuhr")
        self.config_handler = config_handler 
        self.network_handler = network_handler
        self.rtc_handler=rtc_handler
        self.led_handler = led_handler

        self.config_handler.initialize_default_config(self.default_config) # TODO think about a better solution to prevent inconsistent default configs (maybe a class that holds the default config and the config handler just uses that)
        self.config = self.config_handler.load_config_from_file()
        self.apply_loaded_config()
        self.show_start_up_animation()
          
            
    def apply_loaded_config(self):
        self.time_zone = self.config.get("time_zone","Europe/Berlin")
        self.available_time_zones = self.config.get("available_time_zones",["Europe/Berlin"])
        self.config_handler.save_config(self.config) # save the loaded config just in case there are some new keys with default values

    def set_config_to_default(self):
        print("set config to default")
        self.config_handler.set_config_to_default()
        self.apply_loaded_config()
        self.network_handler.apply_loaded_config()
        
    def show_start_up_animation(self):
         print("show_start_up_animation")
            # TODO show start up animation

    def run(self):
        # If no network configurated or unable to connect => host WLAN Buchstabenuhr
        is_connected = self.network_handler.connect_to_wlan()
        if is_connected == False:
            print(f"Connecting to \"{self.network_handler.wlan_ssid}\" faild - opening own access point \"Buchstabenuhr\"!")
            self.network_handler.connect_to_wlan("Buchstabenuhr","Buchstabenuhr", "host")
        # runtime as initial time ...
        min = 00
        hour = 00
        error_leds = []
        # TODO load time from RTC
        time_json = self.network_handler.request_current_time(self.time_zone)
        temp_min = time_json.get("min",-1)
        temp_hour = time_json.get("hour",-1)
        # TODO Error if loading time failed => maybe set a C as indicator
        
        if temp_min <0 or temp_hour <0:
            error_leds += C_1_1
        else:
            # todo update RTC
            min = temp_min
            hour= temp_hour
            
        just_updated = True # to prevent reloading time every 10s
        while True:
            # Reload time every 12h
            if min == 0 and hour %12 ==0 and just_updated == False:
                time_json = self.network_handler.request_current_time(self.time_zone)
                temp_min = time_json.get("min",-1)
                temp_hour = time_json.get("hour",-1)
                # TODO Error if loading time failed => maybe set a C as indicator
                
                if temp_min <0 or temp_hour <0:
                    error_leds += C_1_1
                else:
                    # todo update RTC
                    min = temp_min
                    hour= temp_hour
                    just_updated = True

            if min ==5 and just_updated:
                 just_updated = False

            # TODO load time from RTC
            on_leds = self.interpret_time_to_led(min, hour)
            # TODO Show LEDs
            time.sleep(10) # sleep for 10s => Time scale is min so... this is fine

    def setup__wlan_config_web_server(self):
        html = """<!DOCTYPE html>
    <html>
    <head><title>Wi-Fi Setup</title></head>
    <body>
    <h1>Wi-Fi Setup</h1>
    <form action="/save" method="post">
        <label for="ssid">Wi-Fi SSID:</label>
        <input type="text" id="ssid" name="ssid" required><br>
        <label for="password">Wi-Fi Password:</label>
        <input type="password" id="password" name="password" required><br>
        <input type="submit" value="Save and Connect">
    </form>
    </body>
    </html>
    """
    
    def interpret_time_to_led(self, min, hour):
        if min <0 or hour <0:
            return False
        
        hearts = min %5
        on_leds = []
        
        # ES_1 IST_1
        on_leds += ES_1 + IST_1
        if min <10:
            # FUENF_1 NACH_4
            on_leds += FUENF_1 + NACH_4
        elif min <15:
            # ZEHN_2 NACH_4
            on_leds += ZEHN_2 + NACH_4
        elif min < 20:
            # VIER_3 TEL_3 NACH_4
            on_leds += VIER_3 +TEL_3 + NACH_4
        elif min < 25:
            # ZWANZIG_2 NACH_4
            on_leds += ZWANZIG_2 + NACH_4
        elif min <30:
            # FUENF_1 VOR_4 HALB_4
            hour +=1
            on_leds += FUENF_1+ VOR_4+ HALB_4
        elif min <35:
            # HALB_4
            hour +=1
            on_leds += HALB_4
        elif min <40:
            # FUENF_1 NACH_4 HALB_4
            hour +=1
            on_leds += FUENF_1+ NACH_4+ HALB_4
        elif min <45:
            # ZWANZIG_2 VOR_4
            hour +=1
            on_leds += ZWANZIG_2 + VOR_4
        elif min <50:
            # VIER_3 TEL_3 VOR_4
            hour +=1
            on_leds += VIER_3 +TEL_3 + VOR_4
        elif min<55:
            # ZEHN_2 VOR_4
            hour +=1
            on_leds += ZEHN_2 + VOR_4
        elif min < 60:
            # FUENF_1 VOR_4
            on_leds += FUENF_1 + VOR_4
        
        # limitet to 1 - 12
        if hour >24:
            hour -=12
        if hour >12:
            hour -=12
        # now a switch case on hour
        if hour == 1:
                # EIN_5
                on_leds += EIN_5
                if min >=5:
                    # EINS_5 S_5
                    on_leds += S_5 
        elif hour == 2:
                # ZWEI_9
                on_leds +=ZWEI_9
        elif hour == 3:
                # DREI_7
                on_leds += DREI_7
        elif hour == 4:
                # VIER_7
                on_leds += VIER_7
        elif hour == 5:
                # FUENF_9
                on_leds += FUENF_9
        elif hour ==  6:
                # SECHS_6
                on_leds += SECHS_6
        elif hour ==  7:
                # SIEBEN_8
                on_leds += SIEBEN_8
        elif hour ==  8:
                # ACHT_7
                on_leds += ACHT_7
        elif hour ==  9:
                # NEUN_6
                on_leds += NEUN_6
        elif hour ==  10:
                # ZEHN_5
                on_leds += ZEHN_5
        elif hour ==  11:
                # ELF_5
                on_leds += ELF_5
        else:
                # ZWOELF_8
                on_leds += ZWOELF_8

        if hearts >=1:
             on_leds +=HERZ_MIN_10_1
        if hearts >=2:
             on_leds +=HERZ_MIN_10_2
        if hearts >=3:
             on_leds +=HERZ_MIN_10_3
        if hearts >=4:
             on_leds +=HERZ_MIN_10_4
        
        return on_leds

    # Example 1. Make a GET request for google.com and print HTML
    # Print the html content from google.com
    #print("1. Querying google.com:")
    #r = urequests.get("http://www.google.com")
    #print(r.content)
    #r.close()
    def calibrate_rtc(self):
        print("calibrate_rtc")
        current_time = self.network_handler.request_current_time(self.time_zone)
        print(current_time)
        # TODO set RTC to current time


