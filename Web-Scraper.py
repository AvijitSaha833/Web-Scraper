import requests
import time
from bs4 import BeautifulSoup as bs

url = input("Enter the Facebook profile page url from mbasic page\n")  #work on "mbasic" mode
pname=input("Enter your profile name(case sensitive)\n")
alt=pname+", profile picture"
time.sleep(1)
r = requests.get(url)
doc = bs(r.text, "html.parser")
img = doc.find("img",{"alt":alt})["src"]
print(img)
