from bs4 import BeautifulSoup
import json
import requests

class Dataset:
    sno=1
    policy_list=[]
    def __init__(self):
        self.total=0
    
    def progress_bar(self,progress,total):
        percent=100*(progress/float(total))
        bar=    "█" * int(percent) + "-" * (100-int(percent))
        print(f"\r |{bar}| {percent:.2f}%",end="\r")

    def get_total(self):
        for i in ['Delhi/delhi.html','Haryana/hr.html','Maharashtra/maharashtra.html','Rajasthan/rajasthan.html','UP/up.html']:
            filepath='./Dataset/RawHTMlfiles/'+i
            with open(filepath,"rb") as f:
                data=f.read()
                
            soup=BeautifulSoup(data,'html.parser')
            target_div = soup.find_all('div', class_='flex flex-col')
            self.total+=len(target_div)
        print("Total number of schemes to be compiled: ",self.total)
        
            
        
    
    def get_scheme_details(self,path):
        url="https://www.myscheme.gov.in"+path
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        rep=soup.find('div', id='details')
        details=rep.find('div').text
        
        rep2=soup.find('div', id='benefits')
        benefits=rep2.find('div').text
        
        rep3=soup.find('div', id='eligibility')
        eligibility=rep3.find('div').text
        
        return {"details":details,"benefits":benefits,"eligibility":eligibility}
    
    def get_scheme_list(self,path,state):
        filepath='./Dataset/RawHTMlfiles'+path
        with open(filepath,"rb") as f:
            data=f.read()
            
        soup=BeautifulSoup(data,'html.parser')
        
        target_div = soup.find_all('div', class_='flex flex-col')
        self.progress_bar(0,self.total)
        for divs in target_div:
            h2_element = divs.find('h2')
            a_element = divs.find('a')
            policyname=" ".join(a_element.text.replace('\r\n', ' ').split())
            ministry=" ".join(h2_element.text.replace('\r\n', '').split())
            scheme_description=self.get_scheme_details(a_element.get("href"))
            Dataset.policy_list.append({"Sno":Dataset.sno,"Policy name":policyname,"Description":scheme_description,"Ministry":ministry,"State":state})
            Dataset.sno+=1
            self.progress_bar(Dataset.sno,self.total)
            
        return 
    def compiling_rawHTML_files(self):
        print("Compiling Raw HTML files...")
        self.get_scheme_list("/Delhi/delhi.html","Delhi")
        self.get_scheme_list("/Haryana/hr.html","Harayana")
        self.get_scheme_list("/Maharashtra/maharashtra.html","Maharashtra")
        self.get_scheme_list("/Rajasthan/rajasthan.html","Rajasthan")
        self.get_scheme_list("/UP/up.html","UP")
        print("\r\nCompilation completed......\n")
        with open("government_schemes.json","w") as f:
            json.dump(Dataset.policy_list,f)
        
        
        
        
        
        


if __name__ == "__main__":
    obj=Dataset()
    obj.get_total()
    obj.compiling_rawHTML_files()
            
   