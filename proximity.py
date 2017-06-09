#!/usr/bin/env python

import sys
import time
import subprocess

from time import sleep
from apds9930 import APDS9930

SHUTOFF_DELAY = 20  # seconds


def main():
	a = APDS9930(1)

	a.mode = 2
	a.proximity_gain = 1
	a.proximity_sensor = True
	a.ambient_light_sensor = False
	a.power = True
	turned_off = False
	last_motion_time = time.time()


	while True:
		dist = a.proximity
	        if dist > 200:
        		last_motion_time = time.time()
		        sys.stdout.flush()
            		if turned_off:
				turned_off = False
				turn_on()
        	else:
            		if not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY):
                		turned_off = True
                		turn_off()
        	time.sleep(.1)


def turn_on():
	subprocess.call("sh monitor_on.sh", shell=True)

def turn_off():
	subprocess.call("sh monitor_off.sh", shell=True)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		io.cleanup()

