import requests
import re

usrname = 'natas0'
passwd = usrname

url = "http://%s.natas.labs.overthewire.org" % usrname

response = requests.get(url, auth = (usrname, passwd))
content = response.text

print re.findall('password for natas1 is (.*) -->', content)[0]
