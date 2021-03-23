"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    realPeople = set(text[0] for text in texts)
    realPeople.add(text[1] for text in texts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    callers = set(call[0] for call in calls)
    realPeople.add(call[1] for call in calls)

differences = sorted(callers.difference(realPeople))
print("These numbers could be telemarketers: ")
for difference in differences:
    print(difference)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

#Analysis
""" What I did was:

Turn the lists from the CSV files into sets [O(n)]
Find the difference in the sets [O(n)]
Turn the new set into a list [O(n)]
Sort the list [O(nlogn)]
Print the list [O(n)] 

The complexity should be O(nlogn)
"""
