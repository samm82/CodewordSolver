# Solve.py
# 4/2/2019

from Process   import transposeArray

def solveWords(dct, words):
    for word in words:
        file = open("words/words" + str(len(word)).zfill(2) + ".txt", "r")
        lines = file.readlines()
        file.close()

        lines = [line.strip() for line in lines]

        buildingList, charList, indexList = [], [], []

        for char in word: # [1, 2, 'a', 1] - rear, dead, seas
            if char not in charList:
                indexList.append(len(indexList))
                charList.append(char)

                if type(char) == str:
                    buildingList.append([char])
                else:
                    buildingList.append(dct[char])
            else:
                buildingList.append([])
                charList.append('')
                indexList.append(charList.index(char))
                
        # print(buildingList) # [['d', 'e', 'l', 'r', 's', 't'], ['d', 'e', 'l', 'r', 's'], ['a']]
        # print(charList)     # [1, 2, 'a']
        # print(indexList)    # [0, 1, 2, 0]

        iterationNum = 1
        for lst in buildingList:
            if lst == []:
                continue
            else:
                iterationNum *= len(lst)

        lensBuildList = [len(lst) for lst in buildingList]

        # print(lensBuildList)
        
        bigIndexList = []

        for i in lensBuildList:
            if i == 0:
                continue

            mult = False
            for j in lensBuildList:
                if i == j:
                    continue
                elif j % i == 0 and i < j: 
                    mult = True

            if mult:
                iList = iListMultiples(iterationNum, i)
            else:
                iList = iListNoMultiples(iterationNum, i)

            # print(iterationNum, i, iList)
            bigIndexList.append(iList)

        # for i in bigIndexList:
        #     print(i)

        wordList = []

        for i in range(len(bigIndexList[0])):
            word = ""
            for j in indexList:
                word += buildingList[j][bigIndexList[j][i]]
            wordList.append(word)

        wordList = [word for word in wordList if word in lines]
        wordList.sort()

        # print(wordList)

        letters = [list(_word) for _word in wordList]
        letters = transposeArray(letters)
        letters = [list(set(lst)) for lst in letters]

        # print(letters)

        for i in indexList:
            if type(charList[i]) == int:
                dct.update({charList[i] : letters[i]})

        # for key,val in dct.items():
        #     print(key, "=>", val)


testwords = [[1, 2, 'a', 1]]
dct       = {
        1 : ['d', 'e', 'l', 'r', 's', 't'],
        2 : ['e', 'l', 'r']
    }

def iListNoMultiples(total, n):
    return int(total / n) * list(range(n))

def iListMultiples(total, n):
    lst = []
    rng = list(range(n))

    for i in range(n):
        lst += int(total / (n ** 2)) * rng
        rng.insert(len(rng), rng.pop(0))

    return lst

solveWords(dct, testwords)
