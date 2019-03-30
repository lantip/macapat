#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@lantip"
__date__        =   "2019/03/29"
__description__ =   "Tembang Generator"
""" 
import argparse
import markovify
import random
import os
import json

def load_model(tipe):
    '''
    loading models pure based on markov-chain rules.
    TO DO: extend the markovify text method using pos tagged models
    '''
    if os.path.isfile('./models/'+tipe.lower()+'.json'):
        text_model = markovify.Text.from_json(json.loads(open('./models/'+tipe.lower()+'.json','r').read()))
    else:
        if os.path.isdir('./corpus/'+tipe.lower()):
            text_model = None
            for (dirpath, _, filenames) in os.walk('./corpus/'+tipe.lower()):
                for filename in filenames:
                    with open(os.path.join(dirpath, filename)) as f:
                        model = markovify.Text(f, retain_original=False)
                        if text_model:
                            text_model = markovify.combine(models=[text_model, model])
                        else:
                            text_model = model 
            with open('./models/'+tipe.lower()+'.json','w') as fle:
                fle.write(json.dumps(text_model.to_json()))
        else:
            text_model = None
    return text_model


def syllable_count(word):
    '''
    More simple way is just count the vowels, 
    but I choose this method in case I'm gonna add some rules here
    '''
    words = word.lower()
    vowels = "aeiouéèê"
    wdict = {}
    get = wdict.get
    for wrd in words:
        if wrd in vowels:
            wdict[word] = get(word, 0) + 1
    count = sum(wdict.values())
    if count < 1:
        count = 1
    return count


def config_tembang(tipe):
    '''
    According to Tim Behrend. 
    Thanks Mas Paksi Raras Alit!
    '''
    if tipe.lower() == 'gambuh':
        config = ['7-u', '10-u','12-i','8-u', '8-o']
    elif tipe.lower() == 'asmarandana':
        configs = [
            ['8-i', '8-a', '8-e', '7-a', '8-u', '8-a'],
            ['8-i', '8-a', '8-é', '7-a', '8-u', '8-a'],
            ['8-i', '8-a', '8-o', '7-a', '8-u', '8-a']
        ]
        config = random.choice(configs)
    elif tipe.lower() == 'dhandhanggula':
        configs = [
            ['10-i', '10-a', '8-e', '7-u', '9-i', '7-a', '6-u', '8-a', '12-i', '7-a'],
            ['10-i', '10-a', '8-é', '7-u', '9-i', '7-a', '6-u', '8-a', '12-i', '7-a'],
            ['10-i', '10-a', '8-o', '7-u', '9-i', '7-a', '6-u', '8-a', '12-i', '7-a']
        ]
        config = random.choice(configs)
    elif tipe.lower() == 'durma':
        config = ['12-a', '7-i', '6-a', '7-a', '8-i', '5-a', '7-i']
    elif tipe.lower() == 'girisa':
        configs = [
                ['8-a', '8-a', '8-a', '8-a', '8-a'],
                ['8-a', '8-a', '8-a', '8-a', '8-a', '8-a', '8-a', '8-a']
            ]
        config = random.choice(configs)
    elif tipe.lower() == 'jurudemung':
        config = ['8-a', '8-u', '8-u', '8-a', '8-u', '8-a', '8-u']
    elif tipe.lower() == 'kinanthi':
        config = ['8-u', '8-i', '8-a', '8-i', '8-a', '8-i']
    elif tipe.lower() == 'maskumambang':
        config = ['12-i', '6-a', '8-i', '8-a']
    elif tipe.lower() == 'megatruh':
        config = ['12-u', '8-i', '8-u', '8-i', '8-o']
    elif tipe.lower() == 'mijil':
        configs = [
            ['10-i', '6-o', '10-e', '10-i', '6-i', '6-u'],
            ['10-i', '6-o', '10-é', '10-i', '6-i', '6-u'],
        ]
        config = random.choice(configs)
    elif tipe.lower() == 'pangkur':
        config = ['8-a', '11-i', '8-u', '7-a', '12-u', '8-a', '8-i']
    elif tipe.lower() == 'pocung':
        configs = [
            ['12-u', '6-a', '8-i', '12-a'],
            ['12-u', '6-a', '8-u', '12-a'],
            ['12-u', '6-a', '8-e', '12-a'],
            ['12-u', '6-a', '8-é', '12-a'],
            ['12-u', '6-a', '8-o', '12-a'],
            ['4-u', '8-u', '6-a', '8-i', '12-a'],
            ['4-u', '8-u', '6-a', '8-u', '12-a'],
            ['4-u', '8-u', '6-a', '8-e', '12-a'],
            ['4-u', '8-u', '6-a', '8-é', '12-a'],
            ['4-u', '8-u', '6-a', '8-o', '12-a'],
        ]
        config = random.choice(configs)
    elif tipe.lower() == 'sinom':
        config = ['8-a', '8-i', '8-a', '8-i', '7-i', '8-u', '7-a', '8-i', '12-a']
    elif tipe.lower() == 'wirangrong':
        configs = [
            ['8-i', '8-o', '10-u', '6-i', '7-a', '8-a'],
            ['8-i', '8-o', '10-a', '6-i', '7-a', '8-a']
        ]
        config = random.choice(configs)
    else:
        config = None

    return config

def generate_tembang(tipe):
    #load markov-chain models
    combined_model = load_model(tipe)
    if combined_model:
        song_generated = []
        # generate song, following syllable count and vowels rules for each song
        for i,v in enumerate(config_tembang(tipe)):
            syl = int(v.split('-')[0])
            vow = v.split('-')[1]
            match = False
            while not match:
                sentences = combined_model.make_sentence()
                # checking the last vowel
                try:
                    last_vowel = [a for a in sentences if a in "aeiouéèê"][-1]
                except:
                    last_vowel = ""
                if syllable_count(sentences) == syl and last_vowel == vow:
                    song_generated.insert(i, sentences.replace('ê', 'e'))
                    match = True
        return '\n'.join(song_generated)
    else:
        return 'model not found for '+str(tipe)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.MetavarTypeHelpFormatter, description='''Generator Macapat.
        Jenis Tembang Macapat yang bisa digenerate:
        ['maskumambang', 'mijil', 'sinom', 'kinanthi', 'asmarandana', 'gambuh', 'dhandhanggula', 'durma',
          'pangkur', 'megatruh', 'pocung', 'jurudemung', 'wirangrong']''')

    parser.add_argument('-t', '--tipe', type=str, help="Nama/jenis tembang macapat yang ingin digenerate", required=True)
    parser.add_argument('-n', '--number', type=int, default="1", help="Jumlah bait yang ingin digenerate")

    args = parser.parse_args()

    number = args.number
    tipe = args.tipe

    if number:
        for i in range(int(number)):
            print(generate_tembang(tipe))
            print('\n')
    else:
        print(generate_tembang(tipe))

