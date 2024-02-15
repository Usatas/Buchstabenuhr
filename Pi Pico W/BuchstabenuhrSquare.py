import time

# LED Addresses
# Reihe 1: 0 - 21 (links nach rechts)
E_1_1 = [0, 1]  
S_1_2 = [2, 3]  
ES_1 = E_1_1 + S_1_2

K_1_3 = [4, 5]

I_1_4 = [6, 7]  
S_1_5 = [8, 9]
T_1_6 = [10, 11]
IST_1 = I_1_4 + S_1_5 + T_1_6

A_1_7 = [12, 13]

F_1_8 = [14, 15]
UE_1_9 = [16,17]
N_1_10 = [18, 19]
F_1_11 = [20, 21] 
FUENF_1 = F_1_8 + UE_1_9 + N_1_10 + F_1_11

# Reihe 2: 21 - 43 (rechts nach links)
Z_2_1 = [42, 43]
E_2_2 = [40, 41]
H_2_3 =  [38, 39]
N_2_4 = [36, 37]
ZEHN_2 = Z_2_1 + E_2_2 + H_2_3 + N_2_4

Z_2_5 = [34, 35]
W_2_6 = [32, 33]
A_2_7 = [30, 31]
N_2_8 = [28, 29]
Z_2_9 = [26, 27]
I_2_10 = [24, 25]
G_2_11 = [22, 23]
ZWANZIG_2 = Z_2_5 + W_2_6 + A_2_7 + N_2_8 + Z_2_9 + I_2_10 + G_2_11

# Reihe 3: 44 - 65 (links nach rechts)
D_3_1 = [44, 45]
R_3_2 = [46, 47]
E_3_3 = [48, 49]
I_3_4 = [50,51]
DREI_3 = D_3_1 + R_3_2 + E_3_3 + I_3_4
V_3_5 = [52, 53]
I_3_6 = [54, 55]
E_3_7 = [56, 57]
R_3_8 = [58, 59]
VIER_3 = V_3_5 + I_3_6 + E_3_7 + R_3_8
T_3_9 = [60, 61] 
E_3_10 = [62, 63]
L_3_11 = [64, 65]
TEL_3 = T_3_9 + E_3_10 + L_3_11

# Reihe 4: 66 - 87 (rechts nach links) # TODO Hier weiter die Buchstaben anpassen
V_4_1 = [86, 87] 
O_4_2 = [84, 85] 
R_4_3 = [82, 83] 
VOR_4 = V_4_1 + O_4_2 + R_4_3
F_4_4 = [80, 81] 
U_4_5 = [78, 79] 
N_4_6 = [76, 77] 
K_4_7 = [74, 75] 
FUNK_4 = F_4_4 + U_4_5 + N_4_6 + K_4_7
N_4_8 = [72, 73] 
A_4_9 = [70, 71] 
C_4_10 = [68, 69]
H_4_11 = [66, 67]
NACH_4 = N_4_8 + A_4_9 + C_4_10 + H_4_11

# Reihe 5: 88 - 109 (links nach rechts)
H_5_1 = [88, 89]
A_5_2 = [90, 91]
L_5_3 = [92, 93] 
B_5_4 = [94, 95]  
HALB_5 = H_5_1 + A_5_2 + L_5_3 + B_5_4
A_5_5 = [96, 97]
E_5_6 = [98, 99]
L_5_7 = [100, 101]  
F_5_8 = [102, 103]  
ELF_5 = E_5_6 + L_5_7 + F_5_8
UE_5_9 = [104, 105]  
N_5_10 = [106, 107]  
F_5_11 = [108, 109]  
FUENF_5 = F_5_8+ UE_5_9 + N_5_10 + F_5_11

# Reihe 6: 110 - 131 (rechts nach links)
E_6_1 = [130, 131]  
I_6_2 = [128, 129]  
N_6_3 = [126, 127]  
S_6_4 = [124, 125]  
EIN_6 = E_6_1+ I_6_2 + N_6_3 
EINS_6 = E_6_1+ I_6_2 + N_6_3 + S_6_4
X_6_5 = [122, 123]  
A_6_6 = [120, 121]  
M_6_7 = [118, 119]  
Z_6_8 = [116, 117]  
W_6_9 = [114, 115]  
E_6_10 = [112, 113] 
I_6_11 = [110, 111] 
ZWEI_6 = Z_6_8 + W_6_9 + E_6_10 + I_6_11

# Reihe 7: 132 - 153 (links nach rechts)
D_7_1 = [132, 133]  
R_7_2 = [134, 135]  
E_7_3 = [136, 137]  
I_7_4 = [138, 139]  
DREI_7 = D_7_1 + R_7_2 + E_7_3 + I_7_4
P_7_5 = [140, 141]
M_7_6 = [142, 143] 
J_7_7 = [144, 145] 
V_7_8 = [146, 147] 
I_7_9 = [148, 149] 
E_7_10 = [150, 151]
R_7_11 = [152, 153]
VIER_7 = V_7_8 + I_7_9 + E_7_10 + R_7_11

# Reihe 8: 154 - 175 (rechts nach links)
S_8_1 = [174, 175]  
E_8_2 = [172, 173]  
C_8_3 = [170, 171]  
H_8_4 = [168, 169]  
S_8_5 = [166,167]  
SECHS_8 = S_8_1 + E_8_2 + C_8_3 + H_8_4 + S_8_5
N_8_6 = [164, 165]  
L_8_7 = [162, 163]  
A_8_8 = [160, 161]  
C_8_9 = [158, 159]  
H_8_10 = [156, 157] 
T_8_11 = [154, 155] 
ACHT_8 = A_8_8 + C_8_9 + H_8_10 + T_8_11 

# Reihe 9: 176 - 197 (links nach rechts)
S_9_1 = [176, 177]  
I_9_2 = [178, 179]  
E_9_3 = [180, 181]  
B_9_4 = [182, 183]  
E_9_5 = [184, 185]  
N_9_6 = [186, 187]  
SIEBEN_9 = S_9_1 + I_9_2 + E_9_3 + B_9_4 + E_9_5 + N_9_6
Z_9_7 = [188, 189]  
W_9_8 = [190, 191]  
OE_9_9 = [192, 193]  
L_9_10 = [194, 195]  
F_9_11 = [196, 197]  
ZWOELF_9 = Z_9_7 + W_9_8 + OE_9_9 + L_9_10 + F_9_11

# Reihe 10: 198 - 219 (rechts nach links)
Z_10_1 = [218, 219]
E_10_2 = [216, 217]
H_10_3 = [214, 215]
N_10_4 = [212, 213]
ZEHN_10 = Z_10_1 + E_10_2 + H_10_3 + N_10_4
E_10_5 = [210, 211]
U_10_6 = [208, 209]
N_10_7 = [206, 207]
NEUN_10 = N_10_4 + E_10_5 + U_10_6 + N_10_7
K_10_8 = [204, 205]
U_10_9 = [202, 203]
H_10_10 = [200, 201]
R_10_11 = [198, 199]
UHR_10 = U_10_9 + H_10_10 + R_10_11


# Minuten LEDs 220 - 223
MINUTE_1 = [223]
MINUTE_2 = [222] 
MINUTE_3 = [221]
MINUTE_4 = [220]

NUM_LEDS = 224
MAX_BRIGHTNESS = 255/2 # 50% brightness

class BuchstabenuhrSquare():
    config = {}
    default_config = {"wlan_ssid": "BuchstabenuhrSquare",
                      "wlan_password": "BuchstabenuhrSquare",
                      "wlan_mode": "host",
                      "time_zone": "Europe/Berlin",
                      "available_time_zones": ["Africa/Abidjan", "Africa/Accra", "Africa/Addis_Ababa", "Africa/Algiers",
                                               "Africa/Asmara", "Africa/Asmera", "Africa/Bamako", "Africa/Bangui",
                                               "Africa/Banjul", "Africa/Bissau", "Africa/Blantyre",
                                               "Africa/Brazzaville", "Africa/Bujumbura", "Africa/Cairo",
                                               "Africa/Casablanca", "Africa/Ceuta", "Africa/Conakry", "Africa/Dakar",
                                               "Africa/Dar_es_Salaam", "Africa/Djibouti", "Africa/Douala",
                                               "Africa/El_Aaiun", "Africa/Freetown", "Africa/Gaborone", "Africa/Harare",
                                               "Africa/Johannesburg", "Africa/Juba", "Africa/Kampala",
                                               "Africa/Khartoum", "Africa/Kigali", "Africa/Kinshasa", "Africa/Lagos",
                                               "Africa/Libreville", "Africa/Lome", "Africa/Luanda", "Africa/Lubumbashi",
                                               "Africa/Lusaka", "Africa/Malabo", "Africa/Maputo", "Africa/Maseru",
                                               "Africa/Mbabane", "Africa/Mogadishu", "Africa/Monrovia",
                                               "Africa/Nairobi", "Africa/Ndjamena", "Africa/Niamey",
                                               "Africa/Nouakchott", "Africa/Ouagadougou", "Africa/Porto-Novo",
                                               "Africa/Sao_Tome", "Africa/Timbuktu", "Africa/Tripoli", "Africa/Tunis",
                                               "Africa/Windhoek", "America/Adak", "America/Anchorage",
                                               "America/Anguilla", "America/Antigua", "America/Araguaina",
                                               "America/Argentina/Buenos_Aires", "America/Argentina/Catamarca",
                                               "America/Argentina/ComodRivadavia", "America/Argentina/Cordoba",
                                               "America/Argentina/Jujuy", "America/Argentina/La_Rioja",
                                               "America/Argentina/Mendoza", "America/Argentina/Rio_Gallegos",
                                               "America/Argentina/Salta", "America/Argentina/San_Juan",
                                               "America/Argentina/San_Luis", "America/Argentina/Tucuman",
                                               "America/Argentina/Ushuaia", "America/Aruba", "America/Asuncion",
                                               "America/Atikokan", "America/Atka", "America/Bahia",
                                               "America/Bahia_Banderas", "America/Barbados", "America/Belem",
                                               "America/Belize", "America/Blanc-Sablon", "America/Boa_Vista",
                                               "America/Bogota", "America/Boise", "America/Buenos_Aires",
                                               "America/Cambridge_Bay", "America/Campo_Grande", "America/Cancun",
                                               "America/Caracas", "America/Catamarca", "America/Cayenne",
                                               "America/Cayman", "America/Chicago", "America/Chihuahua",
                                               "America/Coral_Harbour", "America/Cordoba", "America/Costa_Rica",
                                               "America/Creston", "America/Cuiaba", "America/Curacao",
                                               "America/Danmarkshavn", "America/Dawson", "America/Dawson_Creek",
                                               "America/Denver", "America/Detroit", "America/Dominica",
                                               "America/Edmonton", "America/Eirunepe", "America/El_Salvador",
                                               "America/Ensenada", "America/Fort_Nelson", "America/Fort_Wayne",
                                               "America/Fortaleza", "America/Glace_Bay", "America/Godthab",
                                               "America/Goose_Bay", "America/Grand_Turk", "America/Grenada",
                                               "America/Guadeloupe", "America/Guatemala", "America/Guayaquil",
                                               "America/Guyana", "America/Halifax", "America/Havana",
                                               "America/Hermosillo", "America/Indiana/Indianapolis",
                                               "America/Indiana/Knox", "America/Indiana/Marengo",
                                               "America/Indiana/Petersburg", "America/Indiana/Tell_City",
                                               "America/Indiana/Vevay", "America/Indiana/Vincennes",
                                               "America/Indiana/Winamac", "America/Indianapolis", "America/Inuvik",
                                               "America/Iqaluit", "America/Jamaica", "America/Jujuy", "America/Juneau",
                                               "America/Kentucky/Louisville", "America/Kentucky/Monticello",
                                               "America/Knox_IN", "America/Kralendijk", "America/La_Paz",
                                               "America/Lima", "America/Los_Angeles", "America/Louisville",
                                               "America/Lower_Princes", "America/Maceio", "America/Managua",
                                               "America/Manaus", "America/Marigot", "America/Martinique",
                                               "America/Matamoros", "America/Mazatlan", "America/Mendoza",
                                               "America/Menominee", "America/Merida", "America/Metlakatla",
                                               "America/Mexico_City", "America/Miquelon", "America/Moncton",
                                               "America/Monterrey", "America/Montevideo", "America/Montreal",
                                               "America/Montserrat", "America/Nassau", "America/New_York",
                                               "America/Nipigon", "America/Nome", "America/Noronha",
                                               "America/North_Dakota/Beulah", "America/North_Dakota/Center",
                                               "America/North_Dakota/New_Salem", "America/Nuuk", "America/Ojinaga",
                                               "America/Panama", "America/Pangnirtung", "America/Paramaribo",
                                               "America/Phoenix", "America/Port_of_Spain", "America/Port-au-Prince",
                                               "America/Porto_Acre", "America/Porto_Velho", "America/Puerto_Rico",
                                               "America/Punta_Arenas", "America/Rainy_River", "America/Rankin_Inlet",
                                               "America/Recife", "America/Regina", "America/Resolute",
                                               "America/Rio_Branco", "America/Rosario", "America/Santa_Isabel",
                                               "America/Santarem", "America/Santiago", "America/Santo_Domingo",
                                               "America/Sao_Paulo", "America/Scoresbysund", "America/Shiprock",
                                               "America/Sitka", "America/St_Barthelemy", "America/St_Johns",
                                               "America/St_Kitts", "America/St_Lucia", "America/St_Thomas",
                                               "America/St_Vincent", "America/Swift_Current", "America/Tegucigalpa",
                                               "America/Thule", "America/Thunder_Bay", "America/Tijuana",
                                               "America/Toronto", "America/Tortola", "America/Vancouver",
                                               "America/Virgin", "America/Whitehorse", "America/Winnipeg",
                                               "America/Yakutat", "America/Yellowknife", "Antarctica/Casey",
                                               "Antarctica/Davis", "Antarctica/DumontDUrville", "Antarctica/Macquarie",
                                               "Antarctica/Mawson", "Antarctica/McMurdo", "Antarctica/Palmer",
                                               "Antarctica/Rothera", "Antarctica/South_Pole", "Antarctica/Syowa",
                                               "Antarctica/Troll", "Antarctica/Vostok", "Arctic/Longyearbyen",
                                               "Asia/Aden", "Asia/Almaty", "Asia/Amman", "Asia/Anadyr", "Asia/Aqtau",
                                               "Asia/Aqtobe", "Asia/Ashgabat", "Asia/Ashkhabad", "Asia/Atyrau",
                                               "Asia/Baghdad", "Asia/Bahrain", "Asia/Baku", "Asia/Bangkok",
                                               "Asia/Barnaul", "Asia/Beirut", "Asia/Bishkek", "Asia/Brunei",
                                               "Asia/Calcutta", "Asia/Chita", "Asia/Choibalsan", "Asia/Chongqing",
                                               "Asia/Chungking", "Asia/Colombo", "Asia/Dacca", "Asia/Damascus",
                                               "Asia/Dhaka", "Asia/Dili", "Asia/Dubai", "Asia/Dushanbe",
                                               "Asia/Famagusta", "Asia/Gaza", "Asia/Harbin", "Asia/Hebron",
                                               "Asia/Ho_Chi_Minh", "Asia/Hong_Kong", "Asia/Hovd", "Asia/Irkutsk",
                                               "Asia/Istanbul", "Asia/Jakarta", "Asia/Jayapura", "Asia/Jerusalem",
                                               "Asia/Kabul", "Asia/Kamchatka", "Asia/Karachi", "Asia/Kashgar",
                                               "Asia/Kathmandu", "Asia/Katmandu", "Asia/Khandyga", "Asia/Kolkata",
                                               "Asia/Krasnoyarsk", "Asia/Kuala_Lumpur", "Asia/Kuching", "Asia/Kuwait",
                                               "Asia/Macao", "Asia/Macau", "Asia/Magadan", "Asia/Makassar",
                                               "Asia/Manila", "Asia/Muscat", "Asia/Nicosia", "Asia/Novokuznetsk",
                                               "Asia/Novosibirsk", "Asia/Omsk", "Asia/Oral", "Asia/Phnom_Penh",
                                               "Asia/Pontianak", "Asia/Pyongyang", "Asia/Qatar", "Asia/Qostanay",
                                               "Asia/Qyzylorda", "Asia/Rangoon", "Asia/Riyadh", "Asia/Saigon",
                                               "Asia/Sakhalin", "Asia/Samarkand", "Asia/Seoul", "Asia/Shanghai",
                                               "Asia/Singapore", "Asia/Srednekolymsk", "Asia/Taipei", "Asia/Tashkent",
                                               "Asia/Tbilisi", "Asia/Tehran", "Asia/Tel_Aviv", "Asia/Thimbu",
                                               "Asia/Thimphu", "Asia/Tokyo", "Asia/Tomsk", "Asia/Ujung_Pandang",
                                               "Asia/Ulaanbaatar", "Asia/Ulan_Bator", "Asia/Urumqi", "Asia/Ust-Nera",
                                               "Asia/Vientiane", "Asia/Vladivostok", "Asia/Yakutsk", "Asia/Yangon",
                                               "Asia/Yekaterinburg", "Asia/Yerevan", "Atlantic/Azores",
                                               "Atlantic/Bermuda", "Atlantic/Canary", "Atlantic/Cape_Verde",
                                               "Atlantic/Faeroe", "Atlantic/Faroe", "Atlantic/Jan_Mayen",
                                               "Atlantic/Madeira", "Atlantic/Reykjavik", "Atlantic/South_Georgia",
                                               "Atlantic/St_Helena", "Atlantic/Stanley", "Australia/ACT",
                                               "Australia/Adelaide", "Australia/Brisbane", "Australia/Broken_Hill",
                                               "Australia/Canberra", "Australia/Currie", "Australia/Darwin",
                                               "Australia/Eucla", "Australia/Hobart", "Australia/LHI",
                                               "Australia/Lindeman", "Australia/Lord_Howe", "Australia/Melbourne",
                                               "Australia/North", "Australia/NSW", "Australia/Perth",
                                               "Australia/Queensland", "Australia/South", "Australia/Sydney",
                                               "Australia/Tasmania", "Australia/Victoria", "Australia/West",
                                               "Australia/Yancowinna", "Brazil/Acre", "Brazil/DeNoronha", "Brazil/East",
                                               "Brazil/West", "Canada/Atlantic", "Canada/Central", "Canada/Eastern",
                                               "Canada/Mountain", "Canada/Newfoundland", "Canada/Pacific",
                                               "Canada/Saskatchewan", "Canada/Yukon", "CET", "Chile/Continental",
                                               "Chile/EasterIsland", "CST6CDT", "Cuba", "EET", "Egypt", "Eire", "EST",
                                               "EST5EDT", "Etc/GMT", "Etc/GMT-0", "Etc/GMT-1", "Etc/GMT-10",
                                               "Etc/GMT-11", "Etc/GMT-12", "Etc/GMT-13", "Etc/GMT-14", "Etc/GMT-2",
                                               "Etc/GMT-3", "Etc/GMT-4", "Etc/GMT-5", "Etc/GMT-6", "Etc/GMT-7",
                                               "Etc/GMT-8", "Etc/GMT-9", "Etc/GMT+0", "Etc/GMT+1", "Etc/GMT+10",
                                               "Etc/GMT+11", "Etc/GMT+12", "Etc/GMT+2", "Etc/GMT+3", "Etc/GMT+4",
                                               "Etc/GMT+5", "Etc/GMT+6", "Etc/GMT+7", "Etc/GMT+8", "Etc/GMT+9",
                                               "Etc/GMT0", "Etc/Greenwich", "Etc/UCT", "Etc/Universal", "Etc/UTC",
                                               "Etc/Zulu", "Europe/Amsterdam", "Europe/Andorra", "Europe/Astrakhan",
                                               "Europe/Athens", "Europe/Belfast", "Europe/Belgrade", "Europe/Berlin",
                                               "Europe/Bratislava", "Europe/Brussels", "Europe/Bucharest",
                                               "Europe/Budapest", "Europe/Busingen", "Europe/Chisinau",
                                               "Europe/Copenhagen", "Europe/Dublin", "Europe/Gibraltar",
                                               "Europe/Guernsey", "Europe/Helsinki", "Europe/Isle_of_Man",
                                               "Europe/Istanbul", "Europe/Jersey", "Europe/Kaliningrad", "Europe/Kiev",
                                               "Europe/Kirov", "Europe/Kyiv", "Europe/Lisbon", "Europe/Ljubljana",
                                               "Europe/London", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta",
                                               "Europe/Mariehamn", "Europe/Minsk", "Europe/Monaco", "Europe/Moscow",
                                               "Europe/Nicosia", "Europe/Oslo", "Europe/Paris", "Europe/Podgorica",
                                               "Europe/Prague", "Europe/Riga", "Europe/Rome", "Europe/Samara",
                                               "Europe/San_Marino", "Europe/Sarajevo", "Europe/Saratov",
                                               "Europe/Simferopol", "Europe/Skopje", "Europe/Sofia", "Europe/Stockholm",
                                               "Europe/Tallinn", "Europe/Tirane", "Europe/Tiraspol", "Europe/Ulyanovsk",
                                               "Europe/Uzhgorod", "Europe/Vaduz", "Europe/Vatican", "Europe/Vienna",
                                               "Europe/Vilnius", "Europe/Volgograd", "Europe/Warsaw", "Europe/Zagreb",
                                               "Europe/Zaporozhye", "Europe/Zurich", "GB", "GB-Eire", "GMT", "GMT-0",
                                               "GMT+0", "GMT0", "Greenwich", "Hongkong", "HST", "Iceland",
                                               "Indian/Antananarivo", "Indian/Chagos", "Indian/Christmas",
                                               "Indian/Cocos", "Indian/Comoro", "Indian/Kerguelen", "Indian/Mahe",
                                               "Indian/Maldives", "Indian/Mauritius", "Indian/Mayotte",
                                               "Indian/Reunion", "Iran", "Israel", "Jamaica", "Japan", "Kwajalein",
                                               "Libya", "MET", "Mexico/BajaNorte", "Mexico/BajaSur", "Mexico/General",
                                               "MST", "MST7MDT", "Navajo", "NZ", "NZ-CHAT", "Pacific/Apia",
                                               "Pacific/Auckland", "Pacific/Bougainville", "Pacific/Chatham",
                                               "Pacific/Chuuk", "Pacific/Easter", "Pacific/Efate", "Pacific/Enderbury",
                                               "Pacific/Fakaofo", "Pacific/Fiji", "Pacific/Funafuti",
                                               "Pacific/Galapagos", "Pacific/Gambier", "Pacific/Guadalcanal",
                                               "Pacific/Guam", "Pacific/Honolulu", "Pacific/Johnston", "Pacific/Kanton",
                                               "Pacific/Kiritimati", "Pacific/Kosrae", "Pacific/Kwajalein",
                                               "Pacific/Majuro", "Pacific/Marquesas", "Pacific/Midway", "Pacific/Nauru",
                                               "Pacific/Niue", "Pacific/Norfolk", "Pacific/Noumea", "Pacific/Pago_Pago",
                                               "Pacific/Palau", "Pacific/Pitcairn", "Pacific/Pohnpei", "Pacific/Ponape",
                                               "Pacific/Port_Moresby", "Pacific/Rarotonga", "Pacific/Saipan",
                                               "Pacific/Samoa", "Pacific/Tahiti", "Pacific/Tarawa", "Pacific/Tongatapu",
                                               "Pacific/Truk", "Pacific/Wake", "Pacific/Wallis", "Pacific/Yap",
                                               "Poland", "Portugal", "PRC", "PST8PDT", "ROC", "ROK", "Singapore",
                                               "Turkey", "UCT", "Universal", "US/Alaska", "US/Aleutian", "US/Arizona",
                                               "US/Central", "US/East-Indiana", "US/Eastern", "US/Hawaii",
                                               "US/Indiana-Starke", "US/Michigan", "US/Mountain", "US/Pacific",
                                               "US/Samoa", "UTC", "W-SU", "WET", "Zulu"]
                      }
    time_zone = ""

    def __init__(self, config_handler, network_handler, rtc_handler, led_handler):
        print("Init Buchstabenuhr")
        self.config_handler = config_handler
        self.network_handler = network_handler
        self.rtc_handler = rtc_handler
        self.led_handler = led_handler
        self.led_handler.set_max_brightness(MAX_BRIGHTNESS)
        self.led_handler.set_num_leds(NUM_LEDS)
        self.led_handler.set_leds_disabled([])

        self.config_handler.initialize_default_config(
            self.default_config)  # TODO think about a better solution to prevent inconsistent default configs (maybe a class that holds the default config and the config handler just uses that)
        self.config = self.config_handler.load_config_from_file()
        self.apply_loaded_config()
        self.show_start_up_animation()

    def apply_loaded_config(self):
        self.time_zone = self.config.get("time_zone", "Europe/Berlin")
        self.available_time_zones = self.config.get("available_time_zones", ["Europe/Berlin"])
        # self.config_handler.save_config(self.config) # save the loaded config just in case there are some new keys with default values

    def set_config_to_default(self):
        print("set config to default")
        self.config_handler.set_config_to_default()
        self.apply_loaded_config()
        self.network_handler.apply_loaded_config()

    def show_start_up_animation(self):
        print("show_start_up_animation")

    # TODO show start up animation

    def run(self):
        print("run BuchstabenuhrSquare")
        # If no network configurated or unable to connect => host WLAN Buchstabenuhr
        # runtime as initial time ...
        min = 00
        hour = 00
        error_leds = []
        just_updated = True  # to prevent reloading time every 10s
        while True:
            # Reload time every 12h
            if min == 0 and hour % 12 == 0 and just_updated == False:
                time_json = self.network_handler.request_current_time(self.time_zone)
                temp_min = time_json.get("min", -1)
                temp_hour = time_json.get("hour", -1)
                # TODO Error if loading time failed => maybe set a C as indicator

                if temp_min < 0 or temp_hour < 0:
                    error_leds += K_1_3
                else:
                    # todo update RTC
                    min = temp_min
                    hour = temp_hour
                    just_updated = True

            if min == 5 and just_updated:
                just_updated = False

            # Get time from RTC
            (second, minute, hour) = self.rtc_handler.DS3231_ReadTime(0)
            print("Time: " + str(hour) + ":" + str(minute) + ":" + str(second))
            on_leds = self.interpret_time_to_led(minute, hour)
            # Show LEDs
            # self.led_handler.pixels_fill_and_show_expert_mode(on_leds, self.led_handler.RED, self.led_handler.GREEN, 1, 0.1)
            self.led_handler.pixels_fill_and_show(on_leds)
            time.sleep(10)  # sleep for 10s => Time scale is min so... this is fine

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
        print(f"interpret_time_to_led: {hour}:{min}")
        if min < 0 or hour < 0:
            return False

        minute = min % 5
        on_leds = []

        # ES_1 IST_1
        on_leds += ES_1 + IST_1
        if min < 10:
            # FUENF_1 NACH_4
            on_leds += FUENF_1 + NACH_4
        elif min < 15:
            # ZEHN_2 NACH_4
            on_leds += ZEHN_2 + NACH_4
        elif min < 20:
            # VIER_3 TEL_3 NACH_4
            on_leds += VIER_3 + TEL_3 + NACH_4
        elif min < 25:
            # ZWANZIG_2 NACH_4
            on_leds += ZWANZIG_2 + NACH_4
        elif min < 30:
            # FUENF_1 VOR_4 HALB_4
            hour += 1
            on_leds += FUENF_1 + VOR_4 + HALB_5
        elif min < 35:
            # HALB_4
            hour += 1
            on_leds += HALB_5
        elif min < 40:
            # FUENF_1 NACH_4 HALB_4
            hour += 1
            on_leds += FUENF_1 + NACH_4 + HALB_5
        elif min < 45:
            # ZWANZIG_2 VOR_4
            hour += 1
            on_leds += ZWANZIG_2 + VOR_4
        elif min < 50:
            # VIER_3 TEL_3 VOR_4
            hour += 1
            on_leds += VIER_3 + TEL_3 + VOR_4
        elif min < 55:
            # ZEHN_2 VOR_4
            hour += 1
            on_leds += ZEHN_2 + VOR_4
        elif min < 60:
            # FUENF_1 VOR_4
            on_leds += FUENF_1 + VOR_4

        # limitet to 1 - 12
        if hour > 24:
            hour -= 12
        if hour > 12:
            hour -= 12
        # now a switch case on hour
        if hour == 1:
            # EIN_5
            on_leds += EIN_6
            if min >= 5:
                # EINS_5 S_5
                on_leds += S_6_4
        elif hour == 2:
            # ZWEI_9
            on_leds += ZWEI_6
        elif hour == 3:
            # DREI_7
            on_leds += DREI_7
        elif hour == 4:
            # VIER_7
            on_leds += VIER_7
        elif hour == 5:
            # FUENF_9
            on_leds += FUENF_5
        elif hour == 6:
            # SECHS_6
            on_leds += SECHS_8
        elif hour == 7:
            # SIEBEN_8
            on_leds += SIEBEN_9
        elif hour == 8:
            # ACHT_7
            on_leds += ACHT_8
        elif hour == 9:
            # NEUN_6
            on_leds += NEUN_10
        elif hour == 10:
            # ZEHN_5
            on_leds += ZEHN_10
        elif hour == 11:
            # ELF_5
            on_leds += ELF_5
        else:
            # ZWOELF_8
            on_leds += ZWOELF_9

        if minute >= 1:
            on_leds += MINUTE_1
        if minute >= 2:
            on_leds += MINUTE_2
        if minute >= 3:
            on_leds += MINUTE_3
        if minute >= 4:
            on_leds += MINUTE_4

        return on_leds

    # Example 1. Make a GET request for google.com and print HTML
    # Print the html content from google.com
    # print("1. Querying google.com:")
    # r = urequests.get("http://www.google.com")
    # print(r.content)
    # r.close()
