"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
textcount = 0
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    totalCalls = [item[0] for item in texts] + [item[1] for item in texts]
    settotalCalls = set(totalCalls)
    textcount += len(settotalCalls)
    print(textcount)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    totalCalls = [item[0] for item in calls] + [item[1] for item in calls]
    settotalCalls = set(totalCalls)
    textcount += len(settotalCalls)
print("there are " + str(textcount) + " different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

#Complexity
""" totalCalls is two for loops not nested so it should O(n)
making a set should be O(n)

The complexity should be O(n) """
