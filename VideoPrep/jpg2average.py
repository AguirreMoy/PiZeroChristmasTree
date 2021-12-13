import numpy as np
from skimage import data, util, io
import matplotlib.pyplot as plt
import glob
from natsort import natsorted
import json
# All files ending with .txt
img_list = natsorted(glob.glob("C:/Users/Aguir/Documents/GitHub/PiZeroCHristmasTree/VideoPrep/tennis_courts/*.jpg"))

output_file_path = "C:/Users/Aguir/Documents/GitHub/PiZeroCHristmasTree/json_files/flume_tennis_courts.json"

data = {}

NUM_LED = 100
ROWBLANK = range(0,6)
ROW1 = range(6,26)
ROW2 = range(26,46)
ROW3 = range(46,61)
ROW4 = range(61,76)
ROW5 = range(76,88)
ROW6 = range(88,93)
ROW7 = range(93,97)
ROW8 = range(97,99)
ROW9 = range(99,100)


for count, img_path in enumerate(img_list):
    img_data = io.imread(img_path)
    blocks = util.view_as_blocks(img_data, (9, 16, 3))

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


    #fig, ax = plt.subplots()
    #ax.imshow(mean_color.astype(np.uint8)) 
    #plt.show()
    data['frame' + str(count)] = my_dict


with open(output_file_path, 'w') as fout:
    json.dump(data, fout, sort_keys=False, indent=4)