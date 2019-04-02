# Solve.py
# 4/1/2019

def solveWords(dicts, words):
    for word in words:
        file = open("words/words" + str(len(word)).zfill(2) + ".txt", "r")
        lines = file.readlines()
        file.close()

# testList = [['1', '5', 'A', '7'], ['S', '5', '7', '3', '2'], ['1', 'E', '9', 'S', '6'], ['A', '18', '23', '7']]
# lets, nums = getLetsNums(testList)
# print(lets)
# print(nums)
