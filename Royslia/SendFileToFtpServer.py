from ftplib import FTP
from pathlib import Path
from datetime import datetime
from datetime import date
import json

# Get ftp login data from json file
with open('/home/pi/work/ftp_credentials.json') as json_file:
  data = json.load(json_file)
  for p in data['ftp_credentials']:
    site = p['site']
    user = p['user']
    password = p['password']

# copy file to ftp server
now = datetime.now()
today = date.today()
current_date = today.strftime("%Y-%m-%d")
#get hour. Will be our filename
current_hour = now.strftime("%H")

basefileName = '/home/pi/work/tmp/'+current_date+'-'+current_hour
file_path_json = Path(basefileName + '.json')
file_path_image = Path(basefileName + '.jpg')
file_path_image_thumbnail = Path(basefileName + '_thumbnail.jpg')

with FTP(site, user, password) as ftp, open(file_path_json, 'rb') as file:
        ftp.storbinary(f"STOR www/images/royslia/{file_path_json.name}", file)

with FTP(site, user, password) as ftp, open(file_path_image, 'rb') as file:
        ftp.storbinary(f"STOR www/images/royslia/"+file_path_image.name+"", file)
        
with FTP(site, user, password) as ftp, open(file_path_image_thumbnail, 'rb') as file:
        ftp.storbinary(f"STOR www/images/royslia/"+file_path_image_thumbnail.name+"", file)