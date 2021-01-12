from ftplib import FTP
from pathlib import Path
from datetime import datetime
import json

# Get ftp login data from json file
with open('ftp_credentials.json') as json_file:
  data = json.load(json_file)
  for p in data['ftp_credentials']:
    site = p['site']
    user = p['user']
    password = p['password']

# copy file to ftp server
now = datetime.now()
current_hour = now.strftime("%H")
file_path_json = Path('tmp/'+ current_hour + '.json')
file_path_image = Path('tmp/'+ current_hour + '.jpeg')

with FTP(site, user, password) as ftp, open(file_path_json, 'rb') as file:
        ftp.storbinary(f'STOR images/royslia/{file_path_json.name}', file)

with FTP(site, user, password) as ftp, open(file_path_image, 'rb') as file:
        ftp.storbinary(f'STOR images/royslia/{file_path_image.name}', file)