#!/usr/bin/python3

import psutil
import argparse

parser = argparse.ArgumentParser(
        description='Get battery info'
    )
parser.add_argument('-i', dest='icon', action='store_true', help='get an icon corresponding to the charge and state of battery')
parser.add_argument('-c', dest='charge', action='store_true', help='get the charge percentage of battery')

args = parser.parse_args()

battery = psutil.sensors_battery()
charge = int(battery.percent)
isPlugged = battery.power_plugged
output = [] 

def getIcon(charge):
    if isPlugged:
        if charge <= 15:
            return ""
        elif charge <= 30:
            return ""
        elif charge <= 50:
            return ""
        elif charge <= 65:
            return ""
        elif charge <= 80:
            return ""
        elif charge <= 95:
            return ""
        else:
            return ""
    else:
        if charge <= 10:
            return ""
        elif charge <= 20:
            return ""
        elif charge <= 30:
            return ""
        elif charge <= 40:
            return ""
        elif charge <= 50:
            return ""
        elif charge <= 60:
            return ""
        elif charge <= 70:
            return ""
        elif charge <= 80:
            return ""
        elif charge <= 95:
            return ""
        else:
            return ""
    
if args.icon:
    output.append(getIcon(charge))

if args.charge:
    output.append(str(charge)+"%")

print(" ".join(output), end="")
