import requests
import re

usrname = 'natas1'
passwd = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

url = "http://%s.natas.labs.overthewire.org" % usrname

response = requests.get(url, auth = (usrname, passwd))
content = response.text

print re.findall('password for natas2 is (.*) -->', content)[0]
