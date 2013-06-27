import numpy as np
import cv
from pytesser import *
from common import *


def proc_ex (ex):
    try:
        text = (image_file_to_string(img_filename(ex[0])),)
    except IOError:
        print "Exception thrown"
        text = ("",)

    return text + tuple(ex)

def write_txt (fname, txt):
    with open(fname, 'wb') as w:
        w.write(txt)

def all_data (dataset):
    """Gets all data for i'th training set"""
    for i in xrange(CV_SEGMENTS):
        fname = data_filename(dataset, i)
        with open(fname) as f:
            f.readline()
            lines = map(lambda x: map(int, x.strip().split()), f.readlines())

        exs = map(lambda x: proc_ex(x), lines)

        yield exs #(image_file_to_string('data/images/txt_msg0.jpg'), exs)

def all_training_data ():
    return all_data('train')

def all_testing_data ():
    return all_data('test')

def put_img_text ():
    for exs in all_training_data():
        for ex in exs:
            fname = txt_filename(ex[1])
            print "Writing %s" % fname
            write_txt(fname, ex[0])


if __name__ == '__main__':
    #text = image_file_to_string('data/images/txt_msg0.jpg')
    #print text
    mk_folder_if_ne(TXT_DIR)
    put_img_text()
    """
    img = cv.imread('data/images/txt_msg0.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(gray, 1, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL,
                                          cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x,y,w,h = cv.boundyRect(cnt)
    """
