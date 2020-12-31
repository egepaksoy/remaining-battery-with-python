import os
import time
x = 0
os.system("echo '' > battery.txt")
os.system("clear")
while x < 7:
    os.system("date +%R >> battery.txt")
    os.system("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep 'percentage' >> battery.txt")
    time.sleep(600)
    x+=1