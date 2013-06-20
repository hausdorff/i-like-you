from __future__ import with_statement
import urllib2, os, cStringIO
from bs4 import BeautifulSoup
from collections import defaultdict


DATA_DIR = 'data/'
IMG_DIR = 'data/images/'
DATA = 'data/testdata'
INTO_YOU = 'into you'
NOT_INTO_YOU = 'not into you'
VERDICT_STILL_OUT = 'verdict still out'
verdict_map = {"He's into you": INTO_YOU, "He's not into you": NOT_INTO_YOU,
               "Verdict is still out": VERDICT_STILL_OUT}

def mk_file_if_ne (fname):
    if not os.path.exists(fname):
        os.makedirs(fname)

if __name__ == '__main__':
    # make data dirs if needed
    mk_file_if_ne(DATA_DIR)
    mk_file_if_ne(IMG_DIR)

    # get data
    with open(DATA) as f:
        raw = f.read()

    # get all pics and votings
    soup = BeautifulSoup(raw)
    for div in soup.findAll('div', {'class': 'post-content'}):
        img_src = None
        print "COW"
        for match in div.findAll('div', {'class': 'field-text-image'}):
            img_src = match.img['src']
            print img_src
            break

        countmap = defaultdict(lambda: 0)
        for match in div.findAll('div', {'class': 'the-verdict'}):
            for li in match.div.ul.findAll('li'):
                count_type = li.a.text
                count = int(li.text.replace(li.a.text, ""))
                countmap[verdict_map[count_type]] = count
                print count
        print countmap

        if img_src != None:
            break
