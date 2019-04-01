# Process.py
# 4/1/2019

def oneDtoTwoDArray(lst, l, w):
    for elem in lst:
        try:
            elem = int(elem)
        except:
            continue

    array = []
    
    for i in range(w):
        array.append(lst[i*l : i*l+w])

    return array

def extractWords(array):
    words = []
    for row in array:
        newList = extractFromRow(row)
        if newList != []:
            words += newList

    transpose = transposeArray(array)

    for row in transpose:
        newList = extractFromRow(row)
        if newList != []:
            words += newList

    return words

def extractFromRow(lst):
    wordsList = []
    word = []

    print(lst)
    for i in range(len(lst)):
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


testList = [[1,   2,  'A', 4,   ''],
            [13,  '', '',  'E', ''],
            ['R', 17, 'A', 2,   '']
            ]

newList = extractWords(testList)
print(newList)
