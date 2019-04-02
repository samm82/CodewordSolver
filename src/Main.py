# Main.py
# 4/2/2019

from functools import reduce
from re        import match

from GUI     import entryGUI
from Process import extractWords, oneDtoTwoDArray
from Solve   import getLetsNums

def main():

    # invalidInput = True
    # while invalidInput:
    #     dims = input("Enter length and width of codeword puzzle: ").split(" ")
    #     if len(dims) == 2:
    #         try:
    #             length = int(dims[0])
    #             width  = int(dims[1])
    #             invalidInput = False
    #         except:
    #             print("Invalid input.\n")
    #             continue

    #     else:
    #         print("Invalid input.")
    #         continue        

    # vals = entryGUI(length, width)
    # vals = oneDtoTwoDArray(vals, length, width)

    vals = [['', '15', '', '11', '', '3', '', '20', '', '11', '', '19', '', '7', ''], ['18', 'I', '8', '18', '22', '7', '6', '25', '', '17', '5', '6', '16', '22', '1'], ['', '8', '', 'I', '', '3', '', '22', '', '22', '', '2', '', 'I', ''], ['12', '3', '16', '8', '22', '15', '25', '23', '22', '16', '', '9', '25', '23', '18'], ['', '2', '', '8', '', '17', '', 'I', '', '12', '', 'I', '', '9', ''], ['17', '22', '5', 'I', '17', 'I', '', '4', '16', '3', '8', '3', '17', 'I', '15'], ['', '', '', '8', '', '6', '', '14', '', '', '', '', '', '16', ''], ['9', '16', 'I', '10', '22', '8', 'D', '', '24', '22', '14', '11', 'I', 'D', '3'], ['', '3', '', '', '', '', '', '3', '', '9', '', '2', '', '', ''], ['22', 'P', 'P', '3', '8', 'D', 'I', '1', '', 'D', '16', '6', '24', '11', '3'], ['', '16', '', '1', '', 'I', '', '15', '', 'I', '', '6', '', '17', ''], ['7', '6', '23', '17', '', '4', '3', '23', 'I', '15', 'I', '17', '6', '25', '11'], ['', '22', '', '16', '', '4', '', '22', '', '22', '', '5', '', 'D', ''], ['6', '15', '17', '22', '12', '3', '', 'I', '8', '17', '16', '3', 'P', 'I', 'D'], ['', '5', '', '11', '', '16', '', '2', '', '3', '', 'D', '', '6', '']]

    # print(vals)
        
    # for lst in vals:
    #     for val in lst:
    #         print(val, end=", ")
    #     print()

    words = extractWords(vals)
    # print(words)

    letters, numbers = getLetsNums(words)
    # print(letters)
    # print(numbers)

    possibleLetters = list(map(chr, range(ord('a'), ord('z')+1)))

    for i in range(len(letters)):
        letters[i] = letters[i].lower()
        possibleLetters.remove(letters[i])

    dicts = [{num : possibleLetters} for num in numbers]

    for dct in dicts:
        print(dct)

    # print(possibleLetters)

    # vals = formattedVals

    # TODO: extract list of words from vals

    # print("")

    # masterList = [[chr(i) for i in range(ord("a"), ord("z") + 1)] for j in range(27)]
    # masterList[0] = []

    # while True:
    #     word = input("Type 'exit' to exit or a codeword (separated by spaces): ")
    #     if word == "exit":
    #         break
    #     elif word == "":
    #         print("")
    #     else:
    #         letters = word.lower().split(" ")
    #         print(letters)

    #         file = open("words/words" + str(len(letters)).zfill(2) + ".txt", "r")
    #         lines = file.readlines()
    #         file.close()

    #         for i in range(len(letters)):
    #             try:
    #                 letters[i] = int(letters[i])
    #             except ValueError:
    #                 continue

    #         if not reduce((lambda x, y : x and y), [(0 < i <= 26) for i in letters if type(i) == int]):
    #             print("Numbers must be between 0 and 26\n")
    #             continue

    #         regex = ""
    #         for i in letters:
    #             if type(i) == int:
    #                 regex += "."
    #             else:
    #                 regex += i
    #                 for ind in range(1, 27):
    #                     if i not in masterList[ind]:
    #                         break
    #                     else:
    #                         masterList[ind].remove(i)


    #         # print(letters)
    #         # print(regex)

    #         # input()

    #         validLetters = [[] for i in range(len(letters))]
    #         for line in lines:
    #             line = line.strip()
    #             # print(line)
    #             # print(match(regex, line))
    #             # input()
    #             if (match(regex, line) == None):
    #                 continue
    #             else:
    #                 lineSplit = list(line)
    #                 if listNoDuplicateInts(letters):
    #                     if noDefinedLetters(lineSplit, letters) and noDoubleAssignments(lineSplit, letters):
    #                         for i in range(len(letters)):
    #                             if type(letters[i]) == int:
    #                                 # print(line)
    #                                 validLetters[i].append(line[i])
    #                                 # print(validLetters)
    #                                 # input()
    #                             else:
    #                                 continue
    #                     else:
    #                         continue
    #                 else:
    #                     print("Not implemented - duplicate numbers!")

    #         # print("Valid letters:\n")
    #         # print(validLetters)
    #         # print("")

    #         for i in range(len(letters)):
    #             letter = letters[i]
    #             if type(letter) == int:
    #                 masterList[letter] = [value for value in masterList[letter] if value in validLetters[i]]

    #         for i in masterList:
    #             print(i)

    # print("\n Quit")

def listNoDuplicateInts(lst):
    intList = list(filter(lambda x : type(x) == int, lst))
    return len(intList) == len(set(intList))

def noDefinedLetters(lst, letters):
    defLetters = []
    for letter in letters:
        if (type(letter) == str) and (letter not in defLetters):
            defLetters.append(letter)

    for i in range(len(letters)):
        if (type(letters[i]) == int) and (lst[i] in defLetters):
            return False

    return True

def noDoubleAssignments(lst, letters):
    for i in range(len(letters)):
        for j in range(i+1, len(letters)):
            if lst[i] == lst[j]:
                if letters[i] != letters[j]:
                    return False
    return True

main()