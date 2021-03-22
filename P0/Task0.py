"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    index = texts[0][2].index(" ")
    timestamp = texts[0][2][index+1:]
    print("First record of texts, " + texts[0][0] + " texts " + texts[0][1] + " at time " + timestamp)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    lengthlist = len(calls)-1
    index = calls[lengthlist][2].index(" ")
    timestamp = calls[lengthlist][2][index+1:]
    seconds = calls[lengthlist][3]

    print("Last record of calls, " + calls[lengthlist][0] + " calls " + calls[lengthlist][1] + " at time "+ timestamp + " lasting " + seconds + " seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

#Time Complexity
""" the index function takes O(n) where n is the length of the string
getting an item at an index takes O(1)
the complexity should be O(n) """
