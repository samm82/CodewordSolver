# Main.py
# 3/30/2019

from functools import reduce
from re        import match

from GUI import entryGUI

def main():

    dims = input("Enter length and width of codeword puzzle: ").split(" ")
    dim1 = int(dims[0])
    dim2 = int(dims[1])

    values = entryGUI(dim1, dim2)
    for val in values:
        print(val)

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