"""quick and dirty.

get-data.js results in a potentially very long HTML document rendered in a
browser as the main page of HeTexted.com. This contains `img` tags that link
to the actual texts of the people. This script grabs those texts, as well as the
votes from users on each text regarding whether the text indicates the boy likes
the person who received the text."""

from __future__ import with_statement
import urllib, os, time, random
from bs4 import BeautifulSoup
from collections import defaultdict

from common import *



def mk_file_if_ne (fname):
    """Makes file if does not exist"""
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

def cv_line_nums (li):
    """Generates cross validation sets"""
    random.shuffle(li)
    perc = int(0.1*len(li))
    for i in xrange(0, len(li), perc):
        yield li[i:i+perc], li[0:i] + li[i+perc:]

def write_data (lines, ident, datatype):
    """Writes our training/test/dev data to file"""
    with open(data_filename(datatype, ident), 'wb') as w:
        w.write("id\tinto you\tnot into you\tverdict still out\n")
        for line in lines:
            w.write(line)

def setup_data ():
    """Looks through HTML source for labels and URLs to images of text
    messages; then goes out and gets all the images; then writes all our
    data files."""
    setup_env()
    raw = get_data()

    labels_file_lines = []
    for i,(url,labels) in enumerate(iter_thru_valid_divs(raw)):
        print 'processing file %d' % i
        #filename = "%stxt_msg%d.jpg" % (IMG_DIR, i)
        filename = img_filename(i)

        with open(filename, 'wb') as w:
            try:
                dta = urllib.urlopen(url).read()
            except Exception as err:
                print err
                continue
            w.write(dta)
            #time.sleep(0.25)
            labels_file_lines.append("%d\t%d\t%d\t%d\n" %
                                     (i, labels[INTO_YOU],
                                      labels[NOT_INTO_YOU],
                                      labels[VERDICT_STILL_OUT]))

    for i,(train_chunk,test_chunk) in enumerate(cv_line_nums(labels_file_lines)):
        write_data(train_chunk, i, 'train')
        write_data(test_chunk, i, 'test')


if __name__ == '__main__':
    setup_data()
