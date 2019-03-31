# Process.py
# 3/31/2019

def oneDtoTwoDArray(lst, l, w):
    newLst = []
    
    for i in range(w):
        newLst.append(lst[i*l : i*l+w])

    return newLst
