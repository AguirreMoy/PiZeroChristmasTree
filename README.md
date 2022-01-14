# PiZero W video to lightstrip

I created this python script to allow me to automatically generate a 'lightshow' based upon the colors on the screen. 

```bash
pip install foobar
```

## Example
Please check the below reddit video link for an actual example

## Setup
Follow the instructions on [tutorials-raspberrypi.com](https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/) on how to get an LED strip working with your Pi Zero W
## Usage
```bash
python /videoprep/video2json.py
#Please enter mp4 location:
C:\MY MP4 LOCATION\my_mp4_file.mp4
# generates a .json file in the same directory, Place it in the 'json_files' directory
# default directory is C:\MY MP4 LOCATION\my_mp4_file.json
python run.py
#brings up a user selection on json files to play
```

## Contributing
Pull requests are welcome. This was thrown up as a request.

