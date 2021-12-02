import secrets
import string


def gen_key(parts = 4, chars_per_part = 8):
    alphabet = string.ascii_letters + string.digits
    key = ''
    for i in range(parts):
        key += ''.join(secrets.choice(alphabet).upper() for i in range(chars_per_part)) + '-'
    key.rstrip("-")
    return key[:-1]
