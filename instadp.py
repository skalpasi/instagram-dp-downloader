from bs4 import BeautifulSoup 
import urllib.request
import random 
import requests

print('Welcome to instadp CLI!')
print('-----------------------------')
username = input('Enter Username: ')
url = 'https://www.instadp.com/fullsize/'+username

source_code = requests.get(url)

plain_text = source_code.text

soup = BeautifulSoup(plain_text, 'lxml')

for link in soup.find_all("img"):
        href = link.get('src')
    
        img_name = username+str(random.randint(1,500))+'.jpg'

        urllib.request.urlretrieve(href, img_name)
        print('----------------------------')
        print('Image Saved as '+img_name)

