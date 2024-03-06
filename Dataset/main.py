from bs4 import BeautifulSoup
import json

with open("./Dataset/RawHTMLfiles/Delhi/delhi.html","rb") as f:
    data=f.read()
soup=BeautifulSoup(data,'html.parser')
# print(soup.prettify())

target_div = soup.find_all('div', class_='flex flex-col')

# Extract h2 and a elements inside the div
list=[]
for divs in target_div:
    h2_element = divs.find('h2')
    a_element = divs.find('a')
    list.append({"Ministry":" ".join(h2_element.text.replace('\r\n', '').split())," ".join(a_element.text.replace('\r\n', ' ').split()):a_element.get("href")})
# spans=soup.find_all('a')

for h2 in h2_element:
    print(h2.text)
# delhi_dict={}
# for anc in spans:
#     delhi_dict[anc.text]=anc.get("href")
    
with open("./Dataset/delhi.json","w") as f:
    json.dump(list,f)
    
print(list[0])
