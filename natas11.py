import requests
import re
import urllib
import base64

cookies = {"data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

usrname = 'natas11'
passwd = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = "http://%s.natas.labs.overthewire.org/" % usrname

session = requests.Session()

response = session.get(url, auth = (usrname, passwd), cookies = cookies)
#response = session.post(url, data = {}, auth = (usrname, passwd))
content = response.text

#print base64.b64decode(urllib.unquote(session.cookies['data'])).encode('hex')

#print(content)

print re.findall('The password for natas12 is (.*)<' , content)[0]
