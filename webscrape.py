import enum
from unittest.mock import NonCallableMagicMock
from bs4 import BeautifulSoup
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


def get_word(text):
    
    urls = "https://www.ldoceonline.com/dictionary/" + text
    longman = requests.get(urls, headers=headers)
    soup = BeautifulSoup(longman.text, features='lxml')
    tanim = soup.find_all('span', class_= 'Sense')
    return tanim

def real_word_check(object):
    return bool(object)

def spell_check(text):
    check_url = "https://www.ldoceonline.com/spellcheck/english/?q=" + text
    checker = requests.get(check_url, headers=headers)
    checker_soup = BeautifulSoup(checker.text, features='lxml')
    did_you_mean = checker_soup.find_all('ul', class_='didyoumean')
    for j in did_you_mean:
        wordlist = []
        lists = j.find_all("li")
        for i in lists:
            try:
                complete_word = ''
                
                for j in i.text:
                    if 97<=ord(j) <= 122 or 65<=ord(j) <= 90:
                        complete_word += j
                wordlist.append(complete_word)
            except:
                None
        
    return wordlist


text = input("Enter: ")
word = get_word(text)
is_real = real_word_check(word)

while not is_real:
    did_you_mean = spell_check(text)
    for index, word__ in enumerate(did_you_mean, start= 0):
        print(f'{index} => {word__}')
    print("If you meant any of these, you can select it by It's number, or else you can try to spell correctly")
    text = input("Enter: ")
    try:
        num_text = int(text)
        word = get_word(did_you_mean[num_text])
        text = did_you_mean[num_text]
        break
    except:
        word = get_word(text)
        is_real = real_word_check(word)


t = "LONGMAN DICTIONARY"
print("*"*len(t))
print(t)
print("*"*len(t))
print()



for j,i in enumerate(iterable=word, start= 1):
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
    


    