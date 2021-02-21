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
current_time = now.strftime("%H:%M:%S")
today = date.today()
current_date = today.strftime("%d/%m/%Y")
#get hour. Will be our filename
current_hour = now.strftime("%H")
dayofweek = today.weekday()

# Take the picture
camera = PiCamera()
#camera.start_preview(alpha=200)
camera.resolution = (400, 300)
sleep(5)
pictureFileName = '/home/pi/work/tmp/'+str(dayofweek + 1)+'_'+current_hour 
camera.capture(pictureFileName + '_thumbnail.jpg')

# below two setting needed to increase(double) video size on raspberry to work
camera.resolution = (4056, 3040)
camera.framerate = 1
sleep(5)
pictureFileName = '/home/pi/work/tmp/'+str(dayofweek + 1)+'_'+current_hour 
camera.capture(pictureFileName + '.jpg')
camera.stop_preview()
camera.close()

# Create json file with metadata
data = {}
data['imageinfo'] = []
data['imageinfo'].append({
    'rgb_average': 0.5,
    'time' : current_time,
    'date' : current_date
})


with open(pictureFileName + '.json', 'w') as outfile:
    json.dump(data, outfile)


# Make a thumbnail for picture
# this did not work with the 4056, 3040, but works with lower resolutions
#pictureFileNameThumbnail = pictureFileName + '_thumbnail.jpg' 
#fd_image = open(pictureFileName + '.jpg', 'r')
#img = Image.open(fd_image)
#img.thumbnail((400,300))
#img.save(pictureFileNameThumbnail)
#fd_image.close()

