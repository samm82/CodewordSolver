# Main.py
# 4/3/2019

from GUI     import entryGUI
from Process import extractWords, getLetsNums, oneDtoTwoDArray
from Solve   import solveWords

def main():

    invalidInput = True
    while invalidInput:
        dims = input("Enter length and width of codeword puzzle: ").split(" ")
        if len(dims) == 2:
            try:
                length = int(dims[0])
                width  = int(dims[1])
                invalidInput = False
            except:
                print("Invalid input.\n")
                continue

        else:
            print("Invalid input.")
            continue        

    vals = entryGUI(length, width)
    vals = oneDtoTwoDArray(vals, length, width)

    words            = extractWords(vals)
    letters, numbers = getLetsNums(words)
    possibleLetters  = list(map(chr, range(ord('a'), ord('z')+1)))

    for i in range(len(letters)):
        letters[i] = letters[i].lower()
        possibleLetters.remove(letters[i])

    dct = {}
    for num in numbers:
        dct[num] = possibleLetters

    print("Press any key to get another solved number")

    unsolved = True
    while unsolved:
        unsolved = solveWords(dct, words)

main()
