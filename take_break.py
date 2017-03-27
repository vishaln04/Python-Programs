#!/usr/bin/env python3
import subprocess
import sys
import time

awaketime = int(float(sys.argv[1])*60)
sleeptime = int(float(sys.argv[2])*60)

message = "Break in 15 seconds"

def take_a_break():
    get = subprocess.check_output(["xrandr"]).decode("utf-8").split()
    screens = [get[i-1] for i in range(len(get)) if get[i] == "connected"]
    for scr in screens:
        # uncomment either one of the commands below [1]
        # darken the screen, or...
        subprocess.call(["xrandr", "--output", scr, "--brightness", "0"])
        # turn it upside down :)
        # subprocess.call(["xrandr", "--output", scr, "--rotate", "inverted"])
    time.sleep(sleeptime)
    for scr in screens:
        # back to "normal"
        subprocess.call(["xrandr", "--output", scr, "--brightness", "1"])
        subprocess.call(["xrandr", "--output", scr, "--rotate", "normal"])

while True:
    time.sleep(awaketime-15)
    subprocess.Popen(["notify-send", message])
    time.sleep(15)
    take_a_break()
