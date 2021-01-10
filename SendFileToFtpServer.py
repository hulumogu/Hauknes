from ftplib import FTP
from pathlib import Path
import json

# Get ftp login data from json file
with open('C:/work/ftp_credentials.json') as json_file:
  data = json.load(json_file)
  for p in data['ftp_credentials']:
    site = p['site']
    user = p['user']
    password = p['password']

# copy file to ftp server
file_path = Path('C:/work/Presentasjon.pdf')

with FTP(site, user, password) as ftp, open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR images/royslia/{file_path.name}', file)