################################################################################ 
#  
#       AUTHOR: 
#           Brigham Thornock 
#  DESCRIPTION: 
#           Parses a wiki page about the American Revolutionary War and tags all
#           word POS
#
#           Adapted from Human Language Technologies assignment
# DEPENDENCIES: 
#           Created with Python 3.11.5 
#           re, nltk, requests, bs4
# 
################################################################################

import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
import requests
from bs4 import BeautifulSoup

def divider(text="", char="=", divider_length=80):
    if not (text==""):
        text = ' ' + text + ' '
    return text.center(divider_length, char)

def clean_text(text):
    text = text.strip()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('<.*?>', '', text)
    return text

url = 'https://en.wikipedia.org/wiki/American_Revolutionary_War'
requestObj = requests.get(url)
html_source = requestObj.text

soupObj = BeautifulSoup(html_source, 'html.parser')

p_tags = soupObj.find_all('p')

text = '. '.join([clean_text(tag.get_text()) for tag in p_tags if not tag.get_text().isspace()])
text = re.sub('\.+', '.', text)
sent_list = sent_tokenize(text)

sent_list = [sent.lower() for sent in sent_list]

for index, sent in enumerate(sent_list):
    print(divider(f'sentence {index+1}') + f'\n{sent}\n{nltk.pos_tag(word_tokenize(sent))}\n\n')