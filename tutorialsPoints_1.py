# Connect with the Link and scrap all the webpages links assocaited to user provided link
import requests
from bs4 import BeautifulSoup

url_1 = input("Enter the url ")
url = url_1[:-9]
connect = requests.get(url)
urls = url
print(urls)
#print(connect.text)  

soup = BeautifulSoup(connect.text,'html.parser')
#print(soup)
# function to scrap all the links present in the webpage  
with open('new.txt','w') as f:
        for links in soup.find_all('a'):
                f.write(links.get('href')) # saving the links to a text file named new.txt
                f.write('\n')
       
        

#print(soup.title.string)
#for link in soup.find_all('a'):
#	print(link.get('href'))
