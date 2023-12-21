def encode(string):
    encodestring = ''
    for s in string:
        encodestring+= str(ord(s))
    return encodestring
