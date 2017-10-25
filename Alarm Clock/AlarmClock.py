import time
import os
my_file='F:\Certificates\cmpunkcult_9hrm2r8m.mp3'
alarm_time=input("Set the alarm as HH:MM:SS ")

current_time=time.strftime("%I:%M:%S")
while(current_time!=alarm_time):
    current_time=time.strftime("%I:%M:%S")
    time.sleep(1)

if(current_time==alarm_time):
    os.startfile(my_file)
