from bs4 import BeautifulSoup
from urllib.request import urlopen
# name = [["Ten", nick]]
for na,nick in name:
  f = urlopen("https://codeforces.com/profile/"+nick)
  soup = BeautifulSoup(f)
  li = soup.find_all("li")
  for i in li:
    if "Contest rating" in str(i):
      rate = i.find("span").contents
     maxx []
      for x in i.find("span", class ="smaller").find_all("span"):
       maxx = x.contents
      print([na]+rate + maxx)