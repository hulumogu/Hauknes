from picamera import PiCamera, Color
from time import sleep
from datetime import datetime
from datetime import date
import json

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
current_date = today.strftime("%d/%m/%Y")
#get hour. Will be our filename
current_hour = now.strftime("%H")


camera = PiCamera()
#camera.resolution = (4056, 3040)
#camera.framerate = 1
camera.start_preview(alpha=200)
sleep(5)
camera.capture('/home/pi/work/tmp/'+current_hour+'.jpg')
camera.stop_preview()
camera.close()



data = {}
data['imageinfo'] = []
data['imageinfo'].append({
    'rgb_average': 0.5,
    'time' : current_time,
    'date' : current_date
})


with open('/home/pi/work/tmp/'+ current_hour + '.json', 'w') as outfile:
    json.dump(data, outfile)


