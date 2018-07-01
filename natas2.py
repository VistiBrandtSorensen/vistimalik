import requests
import re

usrname = 'natas2'
passwd = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = "http://%s.natas.labs.overthewire.org/files/users.txt" % usrname

response = requests.get(url, auth = (usrname, passwd))
content = response.text

#print(content)

print re.findall('natas3:(.*)', content)[0]
