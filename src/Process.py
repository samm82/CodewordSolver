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

    for row in transpose:
        words2 = extractFromRow(row)

    return words1 + words2

def extractFromRow(lst):
    wordsList = []
    word = []

    for char in lst:
        print("Word:", word, "Words List:", wordsList)
        print("Char:", char)
        input()
        if char == '' and len(word) < 2:
            word = []
            # print("Word:", word, "Words List:", wordsList)
            # input()
        elif char == '':
            #newWord = word[0:len(word)]
            # wordsList += [word[:]]
            wordsList.append([i for i in word])
            word = []
            print("ADDED")
            # print("Word:", word, "Words List:", wordsList)
            # input()
        else:
            word.append(char)
            # print("Word:", word, "Words List:", wordsList)
            # input()

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
