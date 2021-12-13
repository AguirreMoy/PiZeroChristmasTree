import json
import time
starttime = time.time()

time_delay = 0.1



file_name = "C:/Users/Aguir/Documents/GitHub/PiZeroChristmasTree/VideoPrep/porter.json"
f = open(file_name, 'r')
playData = json.load(f)

for i in playData:
    frame_data = playData[i]
    for count, i in enumerate(frame_data):
        # color_data = frame_data[i]
        # print(i, frame_data[i])
        strip.setPixelColor(count, Color(color_data[1],color_data[0], color_data[2]))
    strip.show()
    time.sleep(time_delay - ((time.time() - starttime) % time_delay))
