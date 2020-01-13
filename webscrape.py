from bs4 import BeautifulSoup
import requests
import pandas as pd

pagelist = []
page = requests.get("https://fangj.github.io/friends/")
soup = BeautifulSoup(page.text, 'html.parser').find_all('a')

href_list = []
for i in soup:    
    href = i['href']
    href_list.append(href)

scripts = []
texts = []
for i in href_list:
    page = "https://fangj.github.io/friends/"+str(i)
    script = requests.get(page)
    soup = BeautifulSoup(script.text, 'html.parser').find_all('p')
    for p in soup:
        txt = p.text
        texts.append(txt)

persons = []
dialogues = []
for i in texts:
    if '[' in i:
        persons.append('scene change')
        dialogues.append('NA')
    elif ':' in i and '[' not in i:
        person = i.split(':')[0]
        dialogue = i.split(':')[1]
        persons.append(person)
        dialogues.append(dialogue)
    
    
new_table = pd.DataFrame(
        {'person': persons,
        'dialogue': dialogues,
        'txt': texts
        })

sentences = []
script = scripts[0]
for i in script:
    sentences.append(i)
    
print(sentences)