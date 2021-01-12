from datetime import datetime
from datetime import date
import json

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
current_date = today.strftime("%d/%m/%Y")

data = {}
data['imageinfo'] = []
data['imageinfo'].append({
    'rgb_average': 0.5,
    'time' : current_time,
    'date' : current_date
})

#get hour. Will be our filename
current_hour = now.strftime("%H")

with open('tmp/'+ current_hour + '.json', 'w') as outfile:
    json.dump(data, outfile)


