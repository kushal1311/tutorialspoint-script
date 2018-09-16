import requests
import random
import json
from bs4 import BeautifulSoup

connect = requests.get("https://www.tutorialspoint.com/data_communication_computer_network/index.htm")

soup = BeautifulSoup(connect.text,'html.parser')

print(soup.text)
