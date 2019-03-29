#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@lantip"
__date__        =   "2019/03/29"
__description__ =   "Sastra.org Scrapper"
""" 

import requests
import json
from bs4 import BeautifulSoup

base_url = 'https://www.sastra.org'

first_params = {
    'babad':'["koleksi",1,0,0,0,0,0,0,1,0,0,"",5,0,"","11","46",100,0,"",10,0,0,0,"",10,0,"5c9c33dc3daf7"]',
    'babad_giyanti':'["koleksi",1,0,0,0,0,0,0,1,0,0,"",5,0,"","11","43",100,0,"",10,0,0,0,"",10,0,"5c9c33dc3daf7"]',
    'babad_tanah_jawi':'["koleksi",1,0,0,0,0,0,0,1,0,0,"",5,0,"","11","42",100,0,"",10,0,0,0,"",10,0,"5c9c33dc3daf7"]',
    'cerita':'["koleksi",1,0,0,0,0,0,0,1,0,0,"",5,0,"","11","47",100,0,"",10,0,0,0,"",10,0,"5c9c33dc3daf7"]',
    'mahabharata':'["koleksi",1,0,0,0,0,0,0,1,0,0,"",5,0,"","11","72",100,0,"",10,0,0,0,"",10,0,"5c9c33dc3daf7"]',
    'menak':'["koleksi",1,0,0,0,0,0,0,1,0,0,"",5,0,"","11","73",100,0,"",10,0,0,0,"",10,0,"5c9c33dc3daf7"]',
    'riwayat':'["koleksi",1,0,0,0,0,0,0,1,0,0,"",5,0,"","11","25",100,0,"",10,0,0,0,"",10,0,"5c9c33dc3daf7"]',
    'centhini':'["koleksi",1,0,0,0,0,0,0,1,0,0,"",5,0,"","11","34",100,0,"",10,0,0,0,"",10,0,"5c9c33dc3daf7"]'
}

datalinks = {}
next_params = {}
for key, first_param in first_params.items():
    r = requests.get(base_url+'/sastra/koleksi/koleksi.inc.php?param='+first_param, verify=False)

    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    btns = soup.find_all('button', {'class':'ysl-btn-nav'})

    for btn in btns:
        if btn.get('onclick'):
            prms = btn.get('onclick').replace('ajaxData(','').replace(")","")
            if not key in next_params.keys():
                next_params[key] = []
            if not prms in next_params[key]:
                next_params[key].append(prms)

    links = soup.find_all('a', href=True)
    for lnk in links:
        if not key in datalinks.keys():
            datalinks[key] = []
        if not lnk['href'] in datalinks[key]:
            datalinks[key].append(lnk['href'])

for key, params in next_params.items():
    for param in params:
        r = requests.get(base_url+'/sastra/koleksi/koleksi.inc.php?param='+param, verify=False)
        soups = BeautifulSoup(r.text, 'html.parser')

        lnks = soups.find_all('a', href=True)
        for lnk in lnks:
            if not key in datalinks.keys():
                datalinks[key] = []
            if not lnk['href'] in datalinks[key]:
                datalinks[key].append(lnk['href'])

print(len(datalinks))
with open('links.json', 'w') as fle:
    fle.write(json.dumps(datalinks, indent=4))