# Main.py
# 4/3/2019

from GUI     import entryGUI
from Process import extractWords, getLetsNums, oneDtoTwoDArray
from Solve   import solveWords

def main():

    invalidInput = True

    while invalidInput:
        method = input("Would you like to enter the codeword [1] by a grid or [2] by words? ")
        if method.lower() in ['1', 'by a grid', 'grid']:

            invalidGridInput = True
            while invalidGridInput:
                dims = input("Enter length and width of codeword puzzle: ").split(" ")
                if len(dims) == 2:
                    try:
                        length = int(dims[0])
                        width  = int(dims[1])
                        invalidGridInput = False
                    except:
                        print("Invalid input.\n")

                else:
                    print("Invalid input.")

            words = extractWords(oneDtoTwoDArray(entryGUI(length, width), length, width))

            invalidInput = False

        elif method.lower() in ['2', 'by words', 'words']:
            words = []

            print("TIP: Enter words row-by-row, then column-by-column")
            print("Type 'done' to stop entering words.")

            while True:
                chars = input("Enter word of numbers and letters separated by spaces: ")

                if chars.lower() == "done":
                    break
                else:
                    chars = chars.split(" ")
                    print(chars)
                    if len(chars) < 2:
                        print("Invalid length. Word must have at least two letters.")
                        break

                for i in range(len(chars)):
                    char = chars[i]
                    try:
                        chars[i] = int(char)
                    except:
                        continue

                words.append(chars)

            invalidInput = False
        else:
            print("Invalid input.")

    print(words)

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
