import os


# constant directories and files
DATA_DIR = 'data/'
IMG_DIR = 'data/images/'
TXT_DIR = 'data/texts/'
DATA = 'data/data'
DATA_LABELS = 'data/labels'

IMG_FILE_PATTERN = IMG_DIR + "txt_msg%d.jpg"
TXT_FILE_PATTERN = TXT_DIR + "txt_msg%d.txt"
DATA_FILE_PATTERN = DATA_LABELS + "_%s_%d.txt"

CV_SEGMENTS = 10


def img_filename (ident):
    """Takes image id and outputs filename"""
    return IMG_FILE_PATTERN % ident

def txt_filename (ident):
    """Takes image id and outputs filename"""
    return TXT_FILE_PATTERN % ident

def data_filename (set_type, ident):
    """set_type indicates whether the data is test or train; ident is the id
    of the image"""
    return DATA_FILE_PATTERN % (set_type, ident)

def mk_folder_if_ne (fname):
    """Makes folder if does not exist"""
    if not os.path.exists(fname):
        os.makedirs(fname)

# constant outcome types that HeTexted.com presents us with
INTO_YOU = 'into you'
NOT_INTO_YOU = 'not into you'
VERDICT_STILL_OUT = 'verdict still out'

# mapping our internal representation of the outcomes to the strings that
# designate them in the website
VERDICT_MAP = {"He's into you": INTO_YOU, "He's not into you": NOT_INTO_YOU,
               "Verdict is still out": VERDICT_STILL_OUT}
