#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@lantip"
__date__        =   "2019/03/29"
__description__ =   "Sastra.org Content Scrapper"
""" 

import requests
import json
from bs4 import BeautifulSoup
import re
import os

data = json.loads(open('links.json','r').read())

tembang = ['dhangdhanggula', 'dhandanggula', 'dhandhanggula', 'kinanthi', 
            'asmarandana', 'asmardana', 'pangkur', 'durma', 'gambuh', 'dudukwuluh', 'girisa', 
            'jurudêmung', 'jurudemung', 'maskumambang', 'makumambang', 'megatruh', 'mêgatruh',
            'mijil', 'pocung', 'pucung', 'sinom', 'wirangrong', 'balabak']

ddgl = ['dhangdhanggula', 'dhandanggula', 'dhandhanggula']
jrdm = ['jurudêmung', 'jurudemung']
mskm = ['maskumambang', 'makumambang']
mgtrh = ['megatruh', 'mêgatruh']
asmrd = ['asmarandana', 'asmardana']
pcng = ['pocung', 'pucung']

re1='(.)'   # Any Single Character 1
re2='( )'   # White Space 1
re3='(\\d+)'    # Integer Number 1
re4='( )'   # White Space 2
re5='(-)'   # Any Single Character 2
re6='(-)'   # Any Single Character 3
re7='(-)'   # Any Single Character 4

rg = re.compile(re1+re2+re3+re4+re5+re6+re7,re.IGNORECASE|re.DOTALL)


re8='(\\d+)'    # Integer Number 1
re9='(.)'   # Any Single Character 1
re10='(\\s+)'    # White Space 1

rgn = re.compile(re8+re9+re10,re.IGNORECASE|re.DOTALL)

for key, value in data.items():
    for idk, url in enumerate(value):
        if 'https://' in url:
            link = url
        else:
            link = 'https://www.sastra.org'+url

        r = requests.get(link, verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')

        juduls = soup.find_all('h3')
        for idx, jdl in enumerate(juduls):
            if not jdl.get('class'):
                if jdl.text.strip() != "":
                    node = jdl.text.replace('[','').replace(']','').lstrip('0123456789.- ').split('Teks asli:')[0].split('Nama pupuh tambahan')[0].split('Pada teks asli')[0].split('Untuk konvensi')[0].split('Girisa terdiri dari')[0].split('Nama pupuh asli')[0].split('Semestinya nomor')[0].rstrip('0123456789.- ')
                    print(node)
                    if  node.lower() in tembang:
                        nxt = jdl.find_all_next('p')
                        txt = ''
                        for nx in nxt:
                            for span in nx.find_all('span'):
                                span.decompose()
                            for button in nx.find_all('button'):
                                button.decompose()
                            curtext = re.sub("[\(\[].*?[\)\]]", "", nx.text).lstrip('0123456789.- ')
                            curtext = re.sub(rg, '', curtext)
                            curtext = re.sub(rgn, '', curtext)
                            if not 'catatan ' in curtext.lower():
                                if not 'pratelan kalêpataning panyithakipun.' in curtext.lower():
                                    if not 'nyandhak jilid' in curtext.lower():
                                        if not 'Lajêng nyandhak' in curtext:
                                            txt = txt + curtext
                        if node.lower() in ddgl:
                            ttl = 'dhangdhanggula'
                        elif node.lower() in jrdm:
                            ttl = 'jurudemung'
                        elif node.lower() in mskm:
                            ttl = 'maskumambang'
                        elif node.lower() in mgtrh:
                            ttl = 'megatruh'
                        elif node.lower() in asmrd:
                            ttl = 'asmarandana'
                        elif node.lower() in pcng:
                            ttl = 'pocung'
                        else:
                            ttl = node.lower()
                        if not os.path.exists('corpus/'+ttl.lower()):
                            os.makedirs('corpus/'+ttl.lower())
                        text = txt.replace(' | ','\n').replace(' ||', '\n\n').replace(' |','\n').split('IsinipunKaca')[0].split('IsinipunBêbuka')[0].replace(':  ---','').split('TAMAT JILID ')[0].split('IsinipunBakisar')[0].split('Isinipun')[0].split('AsanapunKangjêng')[0].split('Taksih wontên candhakipun')[0].replace('--','').replace('||', '\n\n')
                        with open('corpus/'+ttl.lower()+'/'+key+'_'+str(idk)+'_'+str(idx)+'.txt', 'w') as fle:
                            fle.write(text)
                        

