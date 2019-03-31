# Process.py
# 3/31/2019

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
    for row in array:
        words1 = extractFromRow(row)

    transpose = transposeArray(array)

    for row in array:
        words2 = extractFromRow(row)

    return words1 + words2

def extractFromRow(lst):
    wordsList = []
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
