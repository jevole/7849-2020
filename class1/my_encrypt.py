# myShift adds shift to characters in text
# for shift: use positive 3 to encrypt, negative 3 to decrypt
# text is text to encrypt -- expects letters only (no spaces, etc)
def myShift(shift, text):
    result = ''
    # go through each letter
    for letter in text.lower():
        # interpunction (spaces etc) will be outside 97-122 range
        if (ord(letter) < 97 or ord(letter) > 122):
            # just add it
            result += letter
            # continue with next letter
            continue
        # add shift to character number of the letter
        enc = ord(letter) + shift
        # encrypted letter after 'z', subtract 26
        if (enc > 122):
            enc -= 26
        # encrypted letter moves before 'a', add 26
        if (enc < 97):
            enc += 26
        # add to result
        result += chr(enc)         
    return (result)

# to decrypt, use -3 
def decrypt(text):
    return (myShift(-3, text))

# to decrypt, use +3 
def encrypt(text):
    return (myShift(3, text))