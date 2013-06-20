from __future__ import with_statement
import urllib, os, time
from bs4 import BeautifulSoup
from collections import defaultdict


# constant directories and files
DATA_DIR = 'data/'
IMG_DIR = 'data/images/'
DATA = 'data/data'
DATA_LABELS = 'data/labels'

# constant outcome types that HeTexted.com presents us with
INTO_YOU = 'into you'
NOT_INTO_YOU = 'not into you'
VERDICT_STILL_OUT = 'verdict still out'

# mapping our internal representation of the outcomes to the strings that
# designate them in the website
VERDICT_MAP = {"He's into you": INTO_YOU, "He's not into you": NOT_INTO_YOU,
               "Verdict is still out": VERDICT_STILL_OUT}


def mk_file_if_ne (fname):
    if not os.path.exists(fname):
        os.makedirs(fname)

def setup_env ():
    """Creates all dirs if needed"""
    mk_file_if_ne(DATA_DIR)
    mk_file_if_ne(IMG_DIR)

def get_data ():
    """Gets all raw data as text"""
    with open(DATA) as f:
        raw = f.read()
    return raw

def iter_thru_valid_divs (raw):
    """Iterates through parsed HTML and yields: (1) the URL at which a text can
    be found, and (2) the dictionary representing the user votes"""
    soup = BeautifulSoup(raw)
    for div in soup.findAll('div', {'class': 'post-content'}):
        img_src = None
        for match in div.findAll('div', {'class': 'field-text-image'}):
            img_src = match.img['src']
            break

        countmap = defaultdict(lambda: 0)
        for match in div.findAll('div', {'class': 'the-verdict'}):
            for li in match.div.ul.findAll('li'):
                count_type = li.a.text
                count = int(li.text.replace(li.a.text, ""))
                countmap[VERDICT_MAP[count_type]] = count

        if img_src != None:
            yield img_src, countmap

def setup_data ():
    setup_env()
    raw = get_data()

    with open(DATA_LABELS, 'wb') as labelswriter:
        labelswriter.write("id\tinto you\tnot into you\tverdict still out\n")
        for i,(url,labels) in enumerate(iter_thru_valid_divs(raw)):
            print 'processing file %d' % i
            filename = "%stxt_msg%d.jpg" % (IMG_DIR, i)

            with open(filename, 'wb') as w:
                w.write(urllib.urlopen(url).read())
                time.sleep(0.25)
                labelswriter.write("%d\t%d\t%d\t%d\n" %
                                   (i, labels[INTO_YOU],
                                    labels[NOT_INTO_YOU],
                                    labels[VERDICT_STILL_OUT]))


if __name__ == '__main__':
    setup_data()
