PUNCT = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    mystring = ''
    for mychar in input_string:
        if mychar not in PUNCT:
            mystring += mychar
    return mystring

