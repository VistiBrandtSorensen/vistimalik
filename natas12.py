import requests
import re

usrname = 'natas12'
passwd = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = "http://%s.natas.labs.overthewire.org/" % usrname

session = requests.Session()

response = session.get(url, auth = (usrname, passwd))
#response = session.post(url, data = {}, auth = (usrname, passwd))
content = response.text

#print base64.b64decode(urllib.unquote(session.cookies['data'])).encode('hex')

print(content)

#print re.findall('The password for natas12 is (.*)<' , content)[0]
