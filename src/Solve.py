# Solve.py
# 4/3/2019

from re import match

from Process import transposeArray

def solveWords(dct, words):
    for word in words:

        for key,val in dct.items():
            if type(val) == list and len(val) == 1:
                val = val[0]

        regex = ""
        for char in word:
            if type(char) == str:
                regex += char
            else:
                if len(dct[char]) == 1:
                    regex += dct[char][0]
                else:
                    regex += "["
                    for i in dct[char]:
                        regex += i
                    regex += "]"

        if "[" in regex:

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

            minimized = False
            while not minimized:
                minimized = True
                for key,val in dct.items():
                    if type(val) == list and len(val) == 1:
                        onlyLetter = val[0]
                        val = onlyLetter
                        for key,val in dct.items():
                            if type(val) == list and onlyLetter in val:
                                val.remove(onlyLetter)

                for key,val in dct.items():
                    if type(val) == list and len(val) == 1:
                        minimized = False

    for key,val in dct.items():
        if type(val) == str:
            input(str(key).rjust(2) + " is " + val)

    for key,val in dct.items():
        if type(val) == list:
            return False

    return True
