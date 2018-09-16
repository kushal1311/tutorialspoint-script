import requests
import random
import json
from bs4 import BeautifulSoup

with open('agent.json') as data_file:
	data = json.load(data_file)
with open("new1.txt","r") as file:
    for link in file:
        random_user_agent = random.choice(data["user_agents"])
        headers = {'user-agent': random_user_agent}
        print(headers)
        connect = requests.get("https://www.tutorialspoint.com"+link, headers=headers, timeout=5)
        soup = BeautifulSoup(connect.text,'html.parser')
        print(soup.text)




#connect = requests.get("https://www.tutorialspoint.com/python/python_questions_answers.htm")

#soup = BeautifulSoup(connect.text,'html.parser')


#with open('data.txt','w') as f:
	#f.write(soup.get('p')) # saving the links to a text file named new.txt
        




#data=soup.prettify()
#print (data) 
