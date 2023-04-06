from picamera import PiCamera, Color
from time import sleep
from datetime import datetime
from datetime import date
from PIL import Image
import json
import os
import glob

#remove old data in tmp folder
files = glob.glob('/home/pi/work/tmp/*')
for f in files:
    os.remove(f)


# date, time stuff
now = datetime.now()
today = date.today()
current_date = today.strftime("%Y-%m-%d")
#get hour. Will be our filename
current_hour = now.strftime("%H")
#dayofweek = today.weekday()

# Take the picture
camera = PiCamera()
#camera.start_preview(alpha=200)
camera.resolution = (400, 300)
sleep(5)
pictureFileName = '/home/pi/work/tmp/'+current_date+'-'+current_hour 
camera.capture(pictureFileName + '_thumbnail.jpg')

# below two setting needed to increase(double) video size on raspberry to work
camera.resolution = (4056, 3040)
camera.framerate = 1
sleep(5)
camera.capture(pictureFileName + '.jpg')
camera.stop_preview()
camera.close()

#now some code to find average rgb values in picture. Used to identify night pictures
pictureFileNameThumbnail = pictureFileName + '_thumbnail.jpg' 
im = Image.open(pictureFileNameThumbnail)
img = im.load()
width, height = im.size
RSum = 0
GSum = 0
BSum = 0
for x in range(width):
    for y in range(height):
        R,G,B=img[x,y]
        RSum += R
        GSum += G
        BSum += B
im.close()
RSum = RSum / (width * height)
GSum = GSum / (width * height)
BSum = BSum / (width * height)
rgb_average = ((RSum + GSum +BSum) / 3.0) / 255.0;

# Create json file with metadata
current_time = now.strftime("%H:%M:%S")
data = {}
data['imageinfo'] = []
data['imageinfo'].append({
    'rgb_average': rgb_average,
    'time' : current_time,
    'date' : current_date
})


with open(pictureFileName + '.json', 'w') as outfile:
    json.dump(data, outfile)
    
#remove files if night
if rgb_average < 0.1:
    files = glob.glob('/home/pi/work/tmp/*')
    for f in files:
        os.remove(f)



