
def scrambleTheWords(inputString):
    """Return the scrambled version of the input string. 
    From each word the first and the last charachter stays on the place
    the remaining characters are read in reversed order.
    For instance:
    
    thing - t nih g
    
    Works even on more sentences, not just one. 
    >>> scrambleTheWords("thing")
    'tnihg'
    >>> scrambleTheWords("Its okay really.")
    'Its oaky rllaey.'
    >>> scrambleTheWords("Its okay. Even with two sentences.")
    'Its oaky. Eevn wtih two secnetnes.'
    >>> scrambleTheWords("")
    Traceback (most recent call last):
        ...
    ValueError: inputString cannot be empty
    >>> scrambleTheWords(None)
    Traceback (most recent call last):
        ...
    ValueError: inputString cannot be None
    """
    if inputString == None:
        raise ValueError("inputString cannot be None")
    if len(inputString)==0:
        raise ValueError("inputString cannot be empty")
    
    
    
    scrambledString = ""
    words = inputString.split(" ")
    temp = ""
    
    for word in words:
        if word[-1] == ".":
            temp = word[1:-2]
            if len(word) > 2:
                scrambledString = scrambledString + word[0] + temp[::-1] + word[-2] + word[-1]
            else:
                scrambledString = scrambledString + word[0] + word[+1]
            
        else:
            temp = word[1:-1]
            if len(word) > 1:
                scrambledString = scrambledString + word[0] + temp[::-1] + word[-1]
            else:
                scrambledString = scrambledString + word[0]
                
        if words.index(word) != (len(words)-1):
            scrambledString = scrambledString + " "   
               
    return scrambledString

if __name__ == "__main__":
    import doctest
    doctest.testmod()