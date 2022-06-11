from bs4 import BeautifulSoup
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

text = input("Enter word: ")
urls = "https://www.ldoceonline.com/dictionary/" + text
longman = requests.get(urls, headers=headers)



soup = BeautifulSoup(longman.text, features='lxml')
tanim = soup.find_all('span', class_= 'Sense')

while not tanim:
    print("Try to correct the spelling and try again")
    text = input("Enter word: ")
    urls = "https://www.ldoceonline.com/dictionary/" + text
    longman = requests.get(urls, headers=headers)
    soup = BeautifulSoup(longman.text, features='lxml')
    tanim = soup.find_all('span', class_= 'Sense')


t = "LONGMAN DICTIONARY"
print("*"*len(t))
print(t)
print("*"*len(t))
print()



for j,i in enumerate(iterable=tanim, start= 1):
        definition = i.find('span',class_='DEF')
        examples = i.find_all('span', class_='EXAMPLE')
        try:
            print(f'{j}.){definition.text}')
            for a in examples:
                m = a.text.replace("\n", "")
                print(f'   *{m}')
            
        except AttributeError:
            None
        print()


t = "CAMBRIDGE DICTIONARY"
print("*"*len(t))
print(t)
print("*"*len(t))
print()



urls = "https://dictionary.cambridge.org/dictionary/english/" + text
camb = requests.get(urls, headers=headers)
soup = BeautifulSoup(camb.text, features='lxml')
tanim = soup.find_all('div', class_='def-block ddef_block')


for j,i in enumerate(tanim,1):
    definition = i.find('div', class_="def ddef_d db")
    examples = i.find_all('div', class_='examp dexamp')
    print(j,definition.text)
    for j in examples:
        print(f'  *{j.text}')
    


    