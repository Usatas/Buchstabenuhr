import uasyncio as asyncio
from ConfigHandler import Config

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

# Reihe 4: 66 - 87 (rechts nach links)
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

class BuchstabenuhrSquare():

    def __init__(self, network_handler, rtc_handler, led_handler):
        print("Init Buchstabenuhr Square")
        self.config = Config()
        self.network_handler = network_handler
        self.rtc_handler = rtc_handler
        self.led_handler = led_handler
        self.led_handler.set_num_leds(NUM_LEDS)
        self.led_handler.set_leds_disabled([])

        self.time_zone = self.config.get("time_zone")
        self.available_time_zones = self.config.get("available_time_zones")
        # self.show_start_up_animation()

    def show_start_up_animation(self):
        # TODO show start up animation
        print("show_start_up_animation")

    async def run(self):
        print("run BuchstabenuhrSquare")
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
                    error_leds += K_1_3
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
            await asyncio.sleep(10)  # sleep for 10s => Time scale is min so... this is fine

    def interpret_time_to_led(self, min, hour):
        if min < 0 or hour < 0:
            return False

        on_leds = ES_1 + IST_1

        min_dict = {
            tuple(range(0, 5)): UHR_10,
            tuple(range(5, 10)): FUENF_1 + NACH_4,
            tuple(range(10, 15)): ZEHN_2 + NACH_4,
            tuple(range(15, 20)): VIER_3 + TEL_3 + NACH_4,
            tuple(range(20, 25)): ZWANZIG_2 + NACH_4,
            tuple(range(25, 30)): FUENF_1 + VOR_4 + HALB_5,
            tuple(range(30, 35)): HALB_5,
            tuple(range(35, 40)): FUENF_1 + NACH_4 + HALB_5,
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
            0: ZWOELF_9,
            1: EIN_6 + (S_6_4 if min >= 5 else []),
            2: ZWEI_6,
            3: DREI_7,
            4: VIER_7,
            5: FUENF_5,
            6: SECHS_8,
            7: SIEBEN_9,
            8: ACHT_8,
            9: NEUN_10,
            10: ZEHN_10,
            11: ELF_5,
            12: ZWOELF_9
        }

        on_leds += hour_dict.get(hour, [])

        min_list = MINUTE_1 + MINUTE_2 + MINUTE_3 + MINUTE_4
        minutes_left = min % 5
        on_leds += min_list[:minutes_left]

        return on_leds
