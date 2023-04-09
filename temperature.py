import os
import json
from pathlib import Path
from datetime import datetime
from datetime import date

def readTemperatureSensor(sensorName):
    tempfile = open("/sys/bus/w1/devices/" + sensorName + "/w1_slave")
    thetext = tempfile.read()
    tempfile.close()
    tempdata = thetext.split("\n")[1].split(" ")[9]
    temperature = float(tempdata[2:])
    temperature = temperature / 1000
    return temperature

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temperatureInside = readTemperatureSensor("28-01204ff7560c")
print(temperatureInside)   
temperatureOutside = readTemperatureSensor("28-01204fe4a25e")
print(temperatureOutside)   

# add temperature to json file
now = datetime.now()
today = date.today()
current_date = today.strftime("%Y-%m-%d")
current_hour = now.strftime("%H")

basefileName = '/home/pi/work/tmp/'+current_date+'-'+current_hour
file_path_json = Path(basefileName + '.json')

f = open(file_path_json) 
data = json.load(f)

data['imageinfo'].append({
    'temperature_inside': temperatureInside,
    'temperature_outside' : temperatureOutside
})

with open(file_path_json, 'w') as outfile:
    json.dump(data, outfile)

