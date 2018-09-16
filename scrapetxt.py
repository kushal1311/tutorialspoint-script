import re
from tutorialsPoints_1 import urls
data =[]
# clean the links from the new.txt and save them to new1.txt
with open('new.txt','r') as f:
    for match in f:
        if match.startswith(urls[30:]):
            data.append(match)

with open('new1.txt','w')as f1:
    for lines in data:
        f1.write(lines)

    
