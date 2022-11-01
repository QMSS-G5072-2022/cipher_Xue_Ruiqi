def cipher(text, shift, encrypt=True):
    """
    this function replaces the input text with an encrpyted output that
    is based on the number of shift in the alphabet (i.e. if the letter is a
    and the shift is 1, the function should return b).
    Parameters
    ----------
    text : a text that you want to encrypt

    shift : an integer that you want the text to shift down the alphabet

    encrypt: a boolean that indicates whether you want the function to encrypt or decrypt

    Returns
    -------
    Encrypted or decrypted text

    Examples
    --------
    >>> cipher(abc,1)
    'bcd'
    >>> cipher(bcd,1,False)
    'abc'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
