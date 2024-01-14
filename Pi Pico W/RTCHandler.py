import machine
from machine import Pin
import rp2
import time

class RTCHandler():
    w = ["FRI","SAT","SUN","MON","TUE","WED","THU"] #if you want different names for Weekdays, feel free to add.
    w = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
    #initialisation of RTC object. Several settings are possible but everything is optional. If you meet this standards no parameter's needed.
    def __init__(self, sda_pin=16, scl_pin=17, port=0, speed=100000, address=0x68, register=0x00):
        print("RTCHandler init")
        self.rtc_address = address      #for using different i2c address
        self.rtc_register = register    #for using different register on device. DON'T change for DS3231
        sda=machine.Pin(sda_pin)        #configure the sda pin
        scl=machine.Pin(scl_pin)        #configure the scl pin
        self.i2c=machine.I2C(port,sda=sda, scl=scl, freq=speed) #configure the i2c interface with given parameters

    def calibrate_rtc(self, network_time):
        print("Calibrate RTC")
        # Ignore Date for now
        week = 1
        day = 1
        month = 1
        year = 21

        sec = self.dec2bcd(network_time.get("seconds",0))
        min = self.dec2bcd(network_time.get("minute",0))
        hour = self.dec2bcd(network_time.get("hour",0))
        week = self.dec2bcd(week)
        day = self.dec2bcd(day)
        month = self.dec2bcd(month)
        if year>2000:
            year-=2000
        year = self.dec2bcd(year)
        print(f"sec: {sec}, min: {min}, hour: {hour}, week: {week}, day: {day}, month: {month}, year: {year}")
        # Create a list of the values
        time_values = [sec, min, hour, week, day, month, year]
        print(f"time_values: {time_values}")
        # Convert the list to a bytes object
        new_time = bytes(time_values)
        print(f"new_time in byte: {new_time}")

        self.DS3231_SetTime(new_time)
        
        new_time = self.DS3231_ReadTime()
        print(f"new_time: {new_time}")
        # b'\x00\x23\x12\x28\x14\x07\x21'
        # sec min hour week day month year

    #function for setting the Time
    def DS3231_SetTime(self, NowTime = b'\x00\x45\x21\x50\x16\x12\x21'):
        hex_string = ''.join('\\x{:02x}'.format(b) for b in NowTime)
        print('b\'' + hex_string + '\'')
        # NowTime has to be in format like b'\x00\x23\x12\x28\x14\x07\x21'
        # It is encoded like this           sec min hour week day month year
        # Then it's written to the DS3231
        self.i2c.writeto_mem(int(self.rtc_address), int(self.rtc_register),NowTime)

    def dec2bcd(self, value):
        tens, units = divmod(value, 10)
        return (tens << 4) + units

    #the DS3231 gives data in bcd format. This has to be converted to binary format.
    def bcd2bin(self, value):
        return (value or 0) - 6 * ((value or 0) >> 4)

    #add a 0 in front of numbers smaler than 10
    def pre_zero(self, value):
        pre_zero = True #change to False if you don't want a "0" in fron of numbers smaler than 10
        if pre_zero:
            if value < 10:
                value = "0"+str(value)  #from now the value is a string!
        return value

    #read the Realtime from the DS3231 with errorhandling. Several output modes can be used.
    def DS3231_ReadTime(self,mode=0):
        try:
            buffer = self.i2c.readfrom_mem(self.rtc_address,self.rtc_register,7)    #read RT from DS3231 and write to the buffer variable. It's a list with 7 entries. Every entry needs to be converted from bcd to bin.
            # year = self.bcd2bin(buffer[6]) + 2000           #the year consists of 2 digits. Here 2000 years are added to get format like "2021"
            # month = self.bcd2bin(buffer[5])                 #just put the month value in the month variable and convert it.
            # day = self.bcd2bin(buffer[4])                   #same for the day value
            # weekday = self.w[self.bcd2bin(buffer[3])]       #weekday will be converted in the weekdays name or shortform like "Sunday" or "SUN"
            #weekday = self.bcd2bin(buffer[3])              #remove comment in this line if you want a number for the weekday and comment the line before.
            hour = self.pre_zero(self.bcd2bin(buffer[2]))   #convert bcd to bin and add a "0" if necessary
            minute = self.pre_zero(self.bcd2bin(buffer[1])) #convert bcd to bin and add a "0" if necessary
            second = self.pre_zero(self.bcd2bin(buffer[0])) #convert bcd to bin and add a "0" if necessary
            
            # time_string = str(hour) + ":" + str(minute) + ":" + str(second) + "      " + str(self.bcd2bin(buffer[3])) + " " + str(day) + "." + str(month) + "." + str(year)
           #  print(time_string)
            if mode == 0:   #mode 0 returns a list of second, minute, ...
                #return second, minute, hour, weekday, day, month, year
                return (second, minute, hour)
            if mode == 1:   #mode 1 returns a formated string with time, weekday and date
                time_string = str(hour) + ":" + str(minute) + ":" + str(second) + "      " + str(self.bcd2bin(buffer[3])) + " " + str(day) + "." + str(month) + "." + str(year)
                return time_string
            #if you need different format, feel free to add
        except Exception as ex:
            print(f"Error while reading time: {ex}")
            return "Error: is the DS3231 not connected?"   #exception occurs in any case of error.


