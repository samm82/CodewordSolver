# Solve.py
# 4/3/2019

from re import match

from Process import transposeArray

def solveWords(dct, words):
    for word in words:

        print("\nNew Word:", word)

        regex = ""
        for char in word:
            if type(char) == str:
                regex += char
            else:
                print(dct[char])
                if len(dct[char]) == 1:
                    regex += dct[char][0]
                else:
                    regex += "["
                    for i in dct[char]:
                        regex += i
                    regex += "]"

        print(regex)

        file = open("words/words" + str(len(word)).zfill(2) + ".txt", "r")
        lines = file.readlines()
        file.close()

        lines = [line.strip() for line in lines]

        validWords = []
        for line in lines:
            if (match(regex, line) == None):
                continue
            else:
                validWords.append(line)

        # print(validWords)

        letters = [list(_word) for _word in validWords]
        letters = transposeArray(letters)
        letters = [list(set(lst)) for lst in letters]

        # print(letters)

        for i in range(len(word)):
            char = word[i]
            if type(char) == int:
                letters[i].sort()
                if len(letters[i]) == 1:
                    dct.update({char : letters[i][0]})
                else:
                    dct.update({char : letters[i]})

        for key,val in dct.items():
            print(key, "=>", val)

            minimized = False
            while not minimized:
                minimized = True

                if len(val) == 1:
                    onlyLetter = val[0]
                    for key,val in dct.items():
                        if type(val) == list and onlyLetter in val:
                            val.remove(onlyLetter)

                for key,val in dct.items():
                    if type(val) == list and len(val) == 1:
                        minimized = False
                        break


        input("Press any key to run the next iteration")

        # printLines = []

        # open("output.txt", a)
        # for key,val in dct.items():
        #     # print(key, "=>", val)
        #     # printLines.append()
        #     file.write(str(key) + "=>" + str(val))
        # file.close()


# testwords = [[1, 2, 'a', 1]]
# dct       = {
#         1 : ['d', 'e', 'l', 'r', 's', 't'],
#         2 : ['e', 'l', 'r']
#     }

# solveWords(dct, testwords)
