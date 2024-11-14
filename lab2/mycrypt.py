import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    
    if len(s) > 1000:
        raise ValueError
    
    # Pad string to max length
    s = s.ljust(1000, 'a')
    
    # Set of allowed characters
    allowed_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"#€%&/()=')
    
    # Check if all characters are allowed
    for c in s:
        if c not in allowed_chars:
            raise ValueError(f"Invalid character: {c}")
    
    for c in s: 
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]

    return crypted[:origlen]

def decode(s):
    return encode(s).lower()