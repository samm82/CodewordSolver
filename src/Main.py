# Main.py
# 3/25/2019

from functools import reduce
from re        import search

def main():

    print("")

    masterList = [[chr(i) for i in range(ord("A"), ord("Z") + 1)] for j in range(27)]
    masterList[0] = []

    while True:
        word = input("Type 'exit' to exit or a codeword (separated by spaces): ")
        if word == "exit":
            break
        elif word == "":
            print("")
        else:
            letters = word.lower().split(" ")
            print(letters)

            file = open("words/words" + str(len(letters)).zfill(2) + ".txt", "r")
            lines = file.readlines()
            file.close()

            for i in range(len(letters)):
                try:
                    letters[i] = int(letters[i])
                except ValueError:
                    continue

            if not reduce((lambda x, y : x and y), [(0 < i <= 26) for i in letters if type(i) == int]):
                print("Numbers must be between 0 and 26\n")
                continue

            regex = ""
            for i in letters:
                if type(i) == int:
                    regex += "."
                else:
                    regex += i

            print(letters)
            print(regex)

            for line in lines:
                line = line.strip()
                if not search(regex, line):
                    continue
                else:
                    print(line)


    print("\n Quit")

main()