from bs4 import BeautifulSoup


with open("./RawHTMLfiles/Delhi/delhi.html","rb") as f:
    data=f.read()
soup=BeautifulSoup(data,'html.parser')
# print(soup.prettify())
spans=soup.find_all('a')

for anc in spans:
    print(anc.text)
    print(anc.get("href"))
    print("******************************")