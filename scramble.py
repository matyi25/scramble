
def scrambleTheWords(inputString):
    scrambledString = ""
    words = inputString.split(" ")
    temp = ""
    for word in words:
        temp = word[1:-1]
        if len(word) > 1:
            scrambledString = scrambledString + word[0] + temp[::-1] + word[-1] + " "
        else:
            scrambledString = scrambledString + word[0] + " "
            
    return scrambledString

print(scrambleTheWords("Atraktam ezt a szavat"))
    