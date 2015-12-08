import requests
from bs4 import BeautifulSoup


print "Search word :",
word = raw_input()
r = requests.get("http://ejje.weblio.jp/content/"+word)
soup = BeautifulSoup(r.text, "lxml")
dicts = soup.find_all("div", class_="hideDictPrs")

if len(dicts) == 0:
    print "There's no such word."
else:
    top_dict = dicts[0]
    statements = top_dict.find_all("div", class_="level0")

    for s in statements:
        print s.get_text()
