import requests
import re

usrname = 'natas8'
passwd = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = "http://%s.natas.labs.overthewire.org/" % usrname

session = requests.Session()

#response = session.get(url, auth = (usrname, passwd))
response = session.post(url, data = {"secret" : "oubWYf2kBq", "submit" : "submit"}, auth = (usrname, passwd))
content = response.text

#print(content)

print re.findall('The password for natas9 is (.*)' , content)[0]
