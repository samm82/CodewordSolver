# Solve.py
# 4/1/2019

def solveWords(dct, words):
    for word in words:
        file = open("words/words" + str(len(word)).zfill(2) + ".txt", "r")
        lines = file.readlines()
        file.close()

        buildingList = []

        for char in word: # [1, 2, 'a', 1] - rear, dead, seas
            if type(char) == str:
                buildingList.append([char])
            else:
                buildingList.append(dicts)


