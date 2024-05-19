import uasyncio as asyncio
from ConfigHandler import Config

# LED Addresses

DISABLED = [ 2,5,8,11,14,17,20,23,26,29,32,
67,64,61,58,55,52,49,46,43,40,37,
72,75,78,81,84,87,90,93,96,99,102,
137,134,131,128,125,122,119,116,113,110,107,
142,145,148,151,154,157,160,163,166,169,172,
207,204,201,198,195,192,189,186,183,180,177,
212,215,218,221,224,227,230,233,236,239,242,
277,274,271,268,265,262,259,256,253,250,247,
282,285,288,291,294,297,300,303,306,309,312,
323,320,317]
# Reihe 1: (links nach rechts)
E_1_1 = [0, 1]  # 2
S_1_2 = [3, 4]  # 5
ES_1 = E_1_1 + S_1_2

C_1_3 = [6, 7]  # 8

I_1_4 = [9, 10]  # 11
S_1_5 = [12, 13]  # 14
T_1_6 = [15, 16]  # 17
IST_1 = I_1_4 + S_1_5 + T_1_6

C_1_7 = [18, 19]  # 20

F_1_8 = [21, 22]  # 23
UE_1_9 = [24, 25]  # 26
N_1_10 = [27, 28]  # 29
F_1_11 = [30, 31]  # 32
FUENF_1 = F_1_8 + UE_1_9 + N_1_10 + F_1_11

C_1_12 = [33, 34]

# Reihe 2: (rechts nach links)
Z_2_1 = [68, 69]
E_2_2 = [65, 66]  # 67
H_2_3 = [62, 63]  # 64
N_2_4 = [59, 60]  # 61
ZEHN_2 = Z_2_1 + E_2_2 + H_2_3 + N_2_4
C_2_5 =  [56, 57]  # 58
Z_2_6 =  [53, 54]  # 55
W_2_7 = [50, 51]  # 52
A_2_8 =[47, 48]  # 49 
N_2_9 = [44, 45]  # 46 
Z_2_10 = [41, 42]  # 43 
I_2_11 = [38, 39]  # 40 
G_2_12 = [35, 36]  # 37
ZWANZIG_2 = Z_2_6 + W_2_7 + A_2_8 + N_2_9 + Z_2_10 + I_2_11 + G_2_12

# Reihe 3: (links nach rechts)
C_3_1 = [70, 71]  # 72
D_3_2 = [73, 74]  # 75
R_3_3 = [76, 77]  # 78
E_3_4 = [79, 80]  # 81
I_3_5 = [82, 83]  # 84
DREI_3 = D_3_2 + R_3_3 + E_3_4 + I_3_5
V_3_6 = [85, 86]  # 87
I_3_7 = [88, 89]  # 90
E_3_8 = [91, 92]  # 93
R_3_9 = [94, 95]  # 96
VIER_3 = V_3_6 + I_3_7 + E_3_8 + R_3_9
T_3_10 = [97, 98]  # 99
E_3_11 = [100, 101]  # 102
L_3_12 = [103, 104]
TEL_3 = T_3_10 + E_3_11 + L_3_12

# Reihe 4: (rechts nach links) 
V_4_1 = [138, 139]
O_4_2 = [135, 136]  # 137
R_4_3 =  [132, 133]  # 134
VOR_4 = V_4_1 + O_4_2 + R_4_3
N_4_4 = [129, 130]  # 131
A_4_5 = [126, 127]  # 128
C_4_6 =  [123, 124]  # 125
H_4_7 =   [120, 121]  # 122
NACH_4 = N_4_4 + A_4_5 + C_4_6 + H_4_7
C_4_8 = [117, 118]  # 119
H_4_9 = [114, 115]  # 116 
A_4_10 = [111, 112]  # 113
L_4_11 = [108, 109]  # 110
B_4_12 =  [105, 106]  # 107
HALB_4 = H_4_9 + A_4_10 + L_4_11 + B_4_12

# Reihe 5: 48 - 59 (links nach rechts)
E_5_1 = [140, 141]  # 142
L_5_2 = [143, 144]  # 145
F_5_3 = [146, 147]  # 148
ELF_5 = E_5_1 + L_5_2 + F_5_3
C_5_4 = [149, 150]  # 151
Z_5_5 = [152, 153]  # 154
E_5_6 = [155, 156]  # 157
H_5_7 = [158, 159]  # 160
N_5_8 = [161, 162]  # 163
ZEHN_5 = Z_5_5 + E_5_6 + H_5_7 + N_5_8
E_5_9 = [164, 165]  # 166
I_5_10 = [167, 168]  # 169
N_5_11 = [170, 171]  # 172
EIN_5 = E_5_9 + I_5_10 + N_5_11
S_5_12 = [173, 174]

# Reihe 6: (rechts nach links)
C_6_1 = [208, 209]
N_6_2 = [205, 206]  # 207
E_6_3 =  [202, 203]  # 204
U_6_4 =  [199, 200]  # 201
N_6_5 = [196, 197]  # 198
NEUN_6 = N_6_2 + E_6_3 + U_6_4 + N_6_5
C_6_6 =[193, 194]  # 195
S_6_7 =  [190, 191]  # 192 
E_6_8 = [187, 188]  # 189 
C_6_9 = [184, 185]  # 186
H_6_10 = [181, 182]  # 183
S_6_11 = [178, 179]  # 180 
SECHS_6 = S_6_7 + E_6_8 + C_6_9 + H_6_10 + S_6_11
C_6_12 = [175, 176]  # 177 

# Reihe 7: (links nach rechts)
D_7_1 = [210, 211]  # 212
R_7_2 = [213, 214]  # 215
E_7_3 = [216, 217]  # 218
I_7_4 = [219, 220]  # 221
DREI_7 = D_7_1 + R_7_2 + E_7_3 + I_7_4
V_7_5 = [222, 223]  # 224
I_7_6 = [225, 226]  # 227
E_7_7 = [228, 229]  # 230
R_7_8 = [231, 232]  # 233
VIER_7 = V_7_5 + I_7_6 + E_7_7 + R_7_8
A_7_9 = [234, 235]  # 236
C_7_10 = [237, 238]  # 239
H_7_11 = [240, 241]  # 242
T_7_12 = [243, 244]
ACHT_7 = A_7_9 + C_7_10 + H_7_11 + T_7_12

# Reihe 8: (rechts nach links)
S_8_1 = [278, 279]
I_8_2 = [275, 276]  # 277
E_8_3 = [272, 273]  # 274
B_8_4 = [269, 270]  # 271
E_8_5 = [266, 267]  # 268
N_8_6 = [263, 264]  # 265
SIEBEN_8 = S_8_1 + I_8_2 + E_8_3 + B_8_4 + E_8_5 + N_8_6
C_8_7 = [260, 261]  # 262 
Z_8_8 = [257, 258]  # 259 
W_8_9 = [254, 255]  # 256 
OE_8_10 = [251, 252]  # 253
L_8_11 = [248, 249]  # 250 
F_8_12 = [245, 246]  # 247 
ZWOELF_8 = Z_8_8 + W_8_9 + OE_8_10 + L_8_11 + F_8_12

# Reihe 9: 96 - 107 (links nach rechts)
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
C_9_9 = [304, 305]  # 306
U_9_10 = [307, 308]  # 309
H_9_11 = [310, 311]  # 312
R_9_12 = [313, 314]
UHR_9 = U_9_10 + H_9_11 + R_9_12

# Reihe 10 Minuten LEDs: 108 - 111 (rechts nach links)
HERZ_MIN_10_1 = [324, 325]
HERZ_MIN_10_2 = [321, 322]  # 323
HERZ_MIN_10_3 = [318, 319]  # 320
HERZ_MIN_10_4 = [315, 316]  # 317 

NUM_LEDS = 326

class Buchstabenuhr():

    def __init__(self,  network_handler, rtc_handler, led_handler):
        print("Init Buchstabenuhr")
        self.config = Config()
        self.network_handler = network_handler
        self.rtc_handler = rtc_handler
        self.led_handler = led_handler
        self.led_handler.set_num_leds(NUM_LEDS)
        self.led_handler.set_disabled_leds(DISABLED)

        self.time_zone = self.config.get("time_zone")
        self.available_time_zones = self.config.get("available_time_zones")
        # self.show_start_up_animation()

    def show_start_up_animation(self):
        # TODO show start up animation
        print("show_start_up_animation")

    async def run(self):
        print("run Buchstabenuhr")
        # If no network configurated or unable to connect => host WLAN Buchstabenuhr
        # runtime as initial time ...
        minute = 0
        hour = 0
        error_leds = []
        just_updated = True  # to prevent reloading time every 10s
        while True:
            # Reload time every 12h
            if minute == 0 and hour % 12 == 0 and just_updated == False:
                time_json = self.network_handler.request_current_time(self.time_zone)
                temp_min = time_json.get("min", -1)
                temp_hour = time_json.get("hour", -1)

                if temp_min < 0 or temp_hour < 0:
                    error_leds += C_1_3
                else:
                    # todo update RTC
                    minute = temp_min
                    hour = temp_hour
                    just_updated = True

            if minute == 5 and just_updated:
                just_updated = False

            # Get time from RTC
            (second, minute, hour) = self.rtc_handler.DS3231_ReadTime()
            print("Time: " + str(hour) + ":" + str(minute) + ":" + str(second))
            on_leds = self.interpret_time_to_led(minute, hour)
            # Show LEDs
            self.led_handler.pixels_fill_and_show(on_leds)
            await asyncio.sleep(1)  # sleep for 10s => Time scale is min so... this is fine

    def interpret_time_to_led(self, min, hour):
        min = int(min)
        hour = int(hour)
        if min < 0 or hour < 0:
            return False

        on_leds = ES_1 + IST_1
        min_dict = {
            tuple(range(0,5)): UHR_9,
            tuple(range(5, 10)): FUENF_1 + NACH_4,
            tuple(range(10, 15)): ZEHN_2 + NACH_4,
            tuple(range(15, 20)): VIER_3 + TEL_3 + NACH_4,
            tuple(range(20, 25)): ZWANZIG_2 + NACH_4,
            tuple(range(25, 30)): FUENF_1 + VOR_4 + HALB_4,
            tuple(range(30, 35)): HALB_4,
            tuple(range(35, 40)): FUENF_1 + NACH_4 + HALB_4,
            tuple(range(40, 45)): ZWANZIG_2 + VOR_4,
            tuple(range(45, 50)): VIER_3 + TEL_3 + VOR_4,
            tuple(range(50, 55)): ZEHN_2 + VOR_4,
            tuple(range(55, 60)): FUENF_1 + VOR_4
        }
        on_leds += next(min_dict[key] for key in min_dict if min in key)
        
        if min >= 25:
            hour += 1

        # convert to 12h format
        hour = hour % 12 if hour > 12 else hour
        hour_dict = {
            0: ZWOELF_8,
            1: EIN_5 + (S_5_12 if min >= 5 else []),
            2: ZWEI_9,
            3: DREI_7,
            4: VIER_7,
            5: FUENF_9,
            6: SECHS_6,
            7: SIEBEN_8,
            8: ACHT_7,
            9: NEUN_6,
            10: ZEHN_5,
            11: ELF_5,
            12: ZWOELF_8
        }

        on_leds += hour_dict.get(hour, [])

        min_list = HERZ_MIN_10_1+ HERZ_MIN_10_2+ HERZ_MIN_10_3+ HERZ_MIN_10_4
        minutes_left = min % 5

        if minutes_left > 0:
            if minutes_left >= 1:
                on_leds += HERZ_MIN_10_1
            if minutes_left >= 2:
                on_leds += HERZ_MIN_10_2
            if minutes_left >= 3:
                on_leds += HERZ_MIN_10_3
            if minutes_left >= 4:
                on_leds += HERZ_MIN_10_4

        return on_leds