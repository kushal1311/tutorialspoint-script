import requests
import time
import test
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

links=str()

def fun():
	with open("new1.txt","r") as file:
		for link in file:
			links="https://www.tutorialspoint.com"+link
			print(links)
			#test.data(links)
			new(links)


def new( links ):
	connection = requests.get(links,headers=header)
	print(connection)
	print(links)
	print(connection.text)


fun()
   		
