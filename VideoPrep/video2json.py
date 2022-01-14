#!/usr/bin/env python3
# generate .json for playback
# Author: Moises Aguirre (aguirre.moy@gmail.com)
#
from ast import Str
import sys
import argparse
import numpy as np
from skimage import data, util, io
import matplotlib.pyplot as plt
import glob
from natsort import natsorted
import json
import cv2
import os
print(cv2.__version__)


#Configure NUM of leds and how many LEDS per row
NUM_LED = 100 #Total LED Num
ROWBLANK = range(0,6) #Leading "blank" LEDs in event some LED bulbs are leading from power supply to the tree
ROW1 = range(6,26)
ROW2 = range(26,46)
ROW3 = range(46,61)
ROW4 = range(61,76)
ROW5 = range(76,88)
ROW6 = range(88,93)
ROW7 = range(93,97)
ROW8 = range(97,99)
ROW9 = range(99,100)

def extractImages(pathIn: Str, pathOut: Str):
    #extracts mp4 into jpegs
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*100))    # set time in ms between frames
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        try:
            cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
            count = count + 1
        except:
            pass


def gen_json(img_list: list, output_file_path: str):
    ### Used to generate a json from a list of jpeg images
    data = {}
    for count, img_path in enumerate(img_list):
        img_data = io.imread(img_path)
        blocks = util.view_as_blocks(img_data, (9, 16, 3))
        #Create image blocks for each jpeg

        mean_color = np.mean(blocks, axis=(2, 3, 4))

        my_dict = {}
        for led_count, i in enumerate(ROWBLANK):
            my_dict["LED" + str(i)] = [0,0,0]
        for led_count, i in enumerate(ROW1):
            my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[11][int(led_count/len(ROW1)*15)].tolist()
        for led_count, i in enumerate(ROW2):
            my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[10][int(led_count/len(ROW2)*15)].tolist()
        for led_count, i in enumerate(ROW3):
            my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[9][int(led_count/len(ROW3)*15)].tolist()
        for led_count, i in enumerate(ROW4):
            my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[8][int(led_count/len(ROW4)*15)].tolist()
        for led_count, i in enumerate(ROW5):
            my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[7][int(led_count/len(ROW5)*15)].tolist()
        for led_count, i in enumerate(ROW6):
            my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[6][int(led_count/len(ROW6)*15)].tolist()
        for led_count, i in enumerate(ROW7):
            my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[5][int(led_count/len(ROW7)*15)].tolist()
        for led_count, i in enumerate(ROW8):
            my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[4][int(led_count/len(ROW8)*15)].tolist()
        for led_count, i in enumerate(ROW9):
            my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[3][7].tolist()
        data['frame' + str(count)] = my_dict

    with open(output_file_path, 'w') as fout:
        json.dump(data, fout, sort_keys=False, indent=4)


if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    #extractImages(args.pathIn, args.pathOut)
    input_path = input("Please enter mp4 location: ")
    base_directory = os.path.dirname(input_path)
    file_name = os.path.basename(input_path)
    jpeg_folder =  os.path.join(base_directory, os.path.splitext(file_name)[0]+"\\") #where folders will be generated to hold all jpegs
    #check if folder exists if not create

    # If folder doesn't exist, then create it.
    if not os.path.isdir(jpeg_folder):
        os.makedirs(jpeg_folder)
        print("created folder : ", jpeg_folder)

    else:
        print(jpeg_folder, "folder already exists.")
    
    extractImages( os.path.join(base_directory, file_name) , jpeg_folder)
    
    img_list = natsorted(glob.glob(jpeg_folder + "*.jpg"))
    output_file_path = os.path.join(base_directory, os.path.splitext(file_name)[0]+".json")
    gen_json(img_list, output_file_path)