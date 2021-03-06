# Process.py
# 4/2/2019

def oneDtoTwoDArray(lst, l, w):
    array = []
    
    for i in range(w):
        array.append(lst[i*l : i*l+w])

    return array

def extractWords(array):
    words = []
    for row in array:
        newList = __extractFromRow(row)
        if newList != []:
            words += newList

    transpose = transposeArray(array)

    for row in transpose:
        newList = __extractFromRow(row)
        if newList != []:
            words += newList

    return words

def getLetsNums(bigList):
    lets, nums = [], []
    for smallList in bigList:
        for char in smallList:
            try:
                new = int(char)
                if new not in nums:
                    nums.append(new)
            except:
                char.lower()
                if char not in lets:
                    lets.append(char)

    lets.sort()
    nums.sort()
    return lets, nums

# Local functions

def __extractFromRow(lst):
    wordsList = []
    word = []

    for i in range(len(lst)):
        try:
            lst[i] = int(lst[i])
        except:
            lst[i] = lst[i].lower()

        char = lst[i]
        if char == '' and len(word) < 2:
            word = []
        elif char == '':
            if word != []:
                wordsList.append(word)
                word = []
        elif i == len(lst) - 1:
            word.append(char)
            if len(word) > 1:
                wordsList.append(word)
                word = []
        else:
            word.append(char)

    return wordsList

def transposeArray(array):
    transpose = [[0 for i in range(len(array))] for j in range(len(array[0]))]

    for i in range(len(array)):
       for j in range(len(array[0])):
           transpose[j][i] = array[i][j]

    return transpose
