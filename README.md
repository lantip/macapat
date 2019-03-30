Macapat Generator
===
This is a simple macapat generator using Markov-Chain ([Markovify](https://github.com/jsvine/markovify))

What is Macapat?
---
>Tembang Macapat (Macapat Song) is one type of Javanese art that combine poetry with music, advice, counsel, wisdom and a variety of Javanese philosophy of life. In addition, this song has another uniqueness, namely to be decorated with various symbols within which its meaning has to be interpreted. 
> -- from [ugm.ac.id](https://ugm.ac.id/en/news/6909-achieve.doctoral.degree.after.study.on.%E2%80%9Ctembang.macapat%E2%80%9D)

    Macapat yaiku tembang basa Jawa sing nduweni aturan ana ing siji lan sijining jinis tembang. 
    Aturan iku jenenge guru wilangan (jumlah silabel dalam satu baris) lan 
    guru lagu (vokal akhir dari kalimat terakhir tiap baris)

Requirements
---
- Python 3
- Markovify

Installation
---
- `git clone https://github.com/lantip/macapat.git`
- `cd macapat`
- If you have `pipenv` in your python package, simply run `pipenv install`
- If you don't have `pipenv`, run:
    `pip install markovify` or `pip3 install markovify`

Usage
---
    Notes:
    Jangan lupa membuat folder ./models
    $ mkdir models

    $ python tembang_generator.py -h # to print help
    
    For macapat type, you can choose one of these:
    ['maskumambang', 'mijil', 'sinom', 'kinanthi', 'asmarandana', 'gambuh', 'dhandhanggula', 'durma',
     'pangkur', 'megatruh', 'pocung', 'jurudemung', 'wirangrong']

    catatan: jurudemung dan wirangrong masuknya sekar madya, bukan macapat

    So for example, you can run:
    $ python tembang_generator.py -t pocung

    To generate more than one stanza, you can define the number like so:
    $ python tembang_generator.py -t pocung -n 3



Thanks To
---
- Paksi Raras Alit
- Mas Bekel Setya Amrih Prasaja
- Tim Behrend 
- [sastra.org](https://www.sastra.org) -- for the corpus
- [Wesley](https://twitter.com/pengelana) -- for suggestion using get