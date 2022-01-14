#!/usr/bin/env python3
# playback python in .json
# Author: Moises Aguirre (aguirre.moy@gmail.com)
#

import time
import glob
from pick import pick
from natsort import natsorted
from rpi_ws281x import *
import argparse
 
# LED strip configuration:
LED_COUNT      = 100      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#Playback configuration
TIME_DELAY = 0.1 #Wait 100 ms per frame


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
 
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
 
    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
 
        while True:
            import json
            import time
            starttime = time.time()


            json_list = natsorted(glob.glob("./json_files/*.json"))
            option, _ = pick(json_list, "Select file to play: ")
            file_name = option
            f = open(file_name, 'r')
            playData = json.load(f)
            print("playing in 3 seconds")
            time.sleep(3)
            for i in playData:
                frame_data = playData[i]
                for count, i in enumerate(frame_data):
                    color_data = frame_data[i]
                    #print(i, frame_data[i])
                    strip.setPixelColor(count, Color(color_data[1],color_data[0], color_data[2]))
                strip.show()
                time.sleep(TIME_DELAY - ((time.time() - starttime) % TIME_DELAY))

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
 