import time

# 0,1, 2,3, X, 5,6
#
#
#
#
#
#
#
#

# LED Addresses
# Reihe 1: 0 - 11 (links nach rechts)
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

# Reihe 2: 12 - 23 (rechts nach links)
Z_2_1 = [22, 23][42, 43]
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

# Reihe 3: 24 - 35 (links nach rechts)
D_3_1 = [44, 45]
R_3_2 = [46, 47]
E_3_3 = [48, 49]
I_3_4 = [50,51]
DREI_3 = D_3_1 + R_3_2 + E_3_3 + I_3_4
V_3_5 = [52, 53]
I_3_6 = [54, 55]
E_3_7 = [56,57]
R_3_8 = [58, 59]
VIER_3 = V_3_5 + I_3_6 + E_3_7 + R_3_8
T_3_9 = [60, 61] 
E_3_10 = [62,63]
L_3_11 = [64, 65]
TEL_3 = T_3_9 + E_3_10 + L_3_11
# Reihe 4: 36 - 47 (rechts nach links) # TODO Hier weiter die Buchstaben anpassen
V_4_1 = []  # 106
O_4_2 = [107, 108]  # 109
R_4_3 = [110, 111]  # 112
VOR_4 = V_4_1 + O_4_2 + R_4_3
N_4_4 = [113, 114]  # 115
A_4_5 = [116, 117]  # 118
C_4_6 = [119, 120]  # 121
H_4_7 = [122, 123]  # 124
NACH_4 = N_4_4 + A_4_5 + C_4_6 + H_4_7
K_4_8 = [125, 126]  # 127
H_4_9 = [128, 129]  # 130
A_4_10 = [131, 132]  # 133
L_4_11 = [134, 135]  # 136
B_4_12 = [1, 138]
HALB_4 = H_4_9 + A_4_10 + L_4_11 + B_4_12
# Reihe 5: 48 - 59
E_5_1 = [139, 140]  # 141
L_5_2 = [142, 143]  # 144
F_5_3 = [145, 146]  # 147
ELF_5 = E_5_1 + L_5_2 + F_5_3
K_5_4 = [148, 149]  # 150
Z_5_5 = [151, 152]  # 153
E_5_6 = [154, 155]  # 156
H_5_7 = [157, 158]  # 159
N_5_8 = [160, 161]  # 162
ZEHN_5 = Z_5_5 + E_5_6 + H_5_7 + N_5_8
E_5_9 = [163, 164]  # 165
I_5_10 = [166, 167]  # 168
N_5_11 = [169, 170]  # 171
EIN_5 = E_5_9 + I_5_10 + N_5_11
S_5_12 = [172, 173]
# Reihe 6: 60 - 71
K_6_1 = [174, 175]  # 176
N_6_2 = [177, 178]  # 179
E_6_3 = [180, 181]  # 182
U_6_4 = [183, 184]  # 185
N_6_5 = [186, 187]  # 188
NEUN_6 = N_6_2 + E_6_3 + U_6_4 + N_6_5
K_6_6 = [189, 190]  # 191
S_6_7 = [192, 193]  # 194
E_6_8 = [195, 196]  # 197
C_6_9 = [198, 199]  # 200
H_6_10 = [201, 202]  # 203
S_6_11 = [204, 205]  # 206
SECHS_6 = S_6_7 + E_6_8 + C_6_9 + H_6_10 + S_6_11
K_6_12 = [207, 208]
# Reihe 7: 72 - 83
D_7_1 = [209, 210]  # 211
R_7_2 = [212, 213]  # 214
E_7_3 = [215, 216]  # 217
I_7_4 = [218, 219]  # 220
DREI_7 = D_7_1 + R_7_2 + E_7_3 + I_7_4
V_7_5 = [221, 222]  # 223
I_7_6 = [224, 225]  # 226
E_7_7 = [237, 238]  # 239
R_7_8 = [231, 232]  # 233
VIER_7 = V_7_5 + I_7_6 + E_7_7 + R_7_8
A_7_9 = [234, 235]  # 236
C_7_10 = [237, 238]  # 239
H_7_11 = [240, 241]  # 242
T_7_12 = [243, 244]
ACHT_7 = A_7_9 + C_7_10 + H_7_11 + T_7_12
# Reihe 8: 84 - 95
S_8_1 = [245, 246]  # 247
I_8_2 = [248, 249]  # 250
E_8_3 = [251, 252]  # 253
B_8_4 = [254, 255]  # 256
E_8_5 = [257, 258]  # 259
N_8_6 = [260, 261]  # 262
SIEBEN_8 = S_8_1 + I_8_2 + E_8_3 + B_8_4 + E_8_5 + N_8_6
K_8_7 = [263, 264]  # 265
Z_8_8 = [266, 267]  # 268
W_8_9 = [269, 270]  # 271
OE_8_10 = [272, 273]  # 274
L_8_11 = [275, 276]  # 277
F_8_12 = [278, 279]
ZWOELF_8 = Z_8_8 + W_8_9 + OE_8_10 + L_8_11 + F_8_12
# Reihe 9: 96 - 107
Z_9_1 = [280, 281]  # 282
W_9_2 = [283, 284]  # 285
E_9_3 = [286, 287]  # 288
I_9_4 = [289, 290]  # 291
ZWEI_9 = Z_9_1 + W_9_2 + E_9_3 + I_9_4
F_9_5 = [292, 293]  # 294
UE_9_6 = [295, 296]  # 297
N_9_7 = [298, 299]  # 300
F_9_8 = [301, 302]  # 303
FUENF_9 = F_9_5 + UE_9_6 + N_9_7 + F_9_8
K_9_9 = [304, 305]  # 306
U_9_10 = [307, 308]  # 309
H_9_11 = [310, 311]  # 312
R_9_12 = [313, 314]
UHR_9 = U_9_10 + H_9_11 + R_9_12
# Reihe 10: 108 - 111
HERZ_MIN_10_1 = [315, 316]  # 317
HERZ_MIN_10_2 = [318, 319]  # 320
HERZ_MIN_10_3 = [321, 322]  # 323
HERZ_MIN_10_4 = [324, 325]


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
        self.led_handler.set_disabled_leds(DISABLED)

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
        print("run Buchstabenuhr")
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
                    error_leds += C_1_1
                else:
                    # todo update RTC
                    min = temp_min
                    hour = temp_hour
                    just_updated = True

            if min == 5 and just_updated:
                just_updated = False

            # TODO load time from RTC
            (second, minute, hour) = self.rtc_handler.DS3231_ReadTime(0)
            on_leds = self.interpret_time_to_led(minute, hour)
            # TODO Show LEDs
            self.led_handler.pixels_fill_and_show_expert_mode(on_leds, self.led_handler.RED, self.led_handler.GREEN,
                                                              0.8, 0.1)
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
        if min < 0 or hour < 0:
            return False

        hearts = min % 5
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
            on_leds += FUENF_1 + VOR_4 + HALB_4
        elif min < 35:
            # HALB_4
            hour += 1
            on_leds += HALB_4
        elif min < 40:
            # FUENF_1 NACH_4 HALB_4
            hour += 1
            on_leds += FUENF_1 + NACH_4 + HALB_4
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
            on_leds += EIN_5
            if min >= 5:
                # EINS_5 S_5
                on_leds += S_5_12
        elif hour == 2:
            # ZWEI_9
            on_leds += ZWEI_9
        elif hour == 3:
            # DREI_7
            on_leds += DREI_7
        elif hour == 4:
            # VIER_7
            on_leds += VIER_7
        elif hour == 5:
            # FUENF_9
            on_leds += FUENF_9
        elif hour == 6:
            # SECHS_6
            on_leds += SECHS_6
        elif hour == 7:
            # SIEBEN_8
            on_leds += SIEBEN_8
        elif hour == 8:
            # ACHT_7
            on_leds += ACHT_7
        elif hour == 9:
            # NEUN_6
            on_leds += NEUN_6
        elif hour == 10:
            # ZEHN_5
            on_leds += ZEHN_5
        elif hour == 11:
            # ELF_5
            on_leds += ELF_5
        else:
            # ZWOELF_8
            on_leds += ZWOELF_8

        if hearts >= 1:
            on_leds += HERZ_MIN_10_1
        if hearts >= 2:
            on_leds += HERZ_MIN_10_2
        if hearts >= 3:
            on_leds += HERZ_MIN_10_3
        if hearts >= 4:
            on_leds += HERZ_MIN_10_4

        return on_leds

    # Example 1. Make a GET request for google.com and print HTML
    # Print the html content from google.com
    # print("1. Querying google.com:")
    # r = urequests.get("http://www.google.com")
    # print(r.content)
    # r.close()
