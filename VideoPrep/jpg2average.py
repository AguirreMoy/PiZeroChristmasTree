import numpy as np
from skimage import data, util, io
import matplotlib.pyplot as plt
import glob
from natsort import natsorted
import json
# All files ending with .txt
img_list = natsorted(glob.glob("C:/Users/Aguir/Documents/GitHub/PiZeroCHristmasTree/VideoPrep/Porter/*.jpg"))

output_file_path = "C:/Users/Aguir/Documents/GitHub/PiZeroCHristmasTree/VideoPrep/porter.json"

data = {}

NUM_LED = 50


for count, img_path in enumerate(img_list):
    img_data = io.imread(img_path)
    blocks = util.view_as_blocks(img_data, (9, 16, 3))

    mean_color = np.mean(blocks, axis=(2, 3, 4))
    my_dict = {}
    for i in range(NUM_LED):
        my_dict["LED" + str(i)] = mean_color.astype(np.uint8)[7][7].tolist()

    data['frame' + str(count)] = my_dict

with open(output_file_path, 'w') as fout:
    json.dump(data, fout, sort_keys=False, indent=4)