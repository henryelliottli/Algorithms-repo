"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
numberDict = {}
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for callers in calls:
        if callers[0] in numberDict: 
            numberDict[callers[0]] += int(callers[3])
        if callers[1] in numberDict:
            numberDict[callers[1]] += int(callers[3])
        else:
            numberDict[callers[0]] = int(callers[3])
            numberDict[callers[1]] = int(callers[3])
longestTime = max(numberDict.values())

maxKeys = ""
for k,v in numberDict.items():
    
    if v == longestTime:
        maxKeys = maxKeys + k + " , "
maxKeys = maxKeys[:-3]
print(maxKeys)

print(maxKeys + " spent the longest time, " + str(longestTime) + " seconds, on the phone during September 2016")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#Complexity

""" there are only un-nested for loops and creating a set in this algorithm so it should be O(n) """