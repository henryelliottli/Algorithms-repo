"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

areacode = "(080)"
areaCodeSet = set()
bangaloreCalls = 0
bangaloreCalled = 0
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
          if call[0].find(areacode) >= 0:
                bangaloreCalls += 1
                if call[1].find(" ") > -1:
                      spaceindex = call[1].index(" ")
                      areaCodeSet.add(call[1][:spaceindex])
                if call[1].find("(") > -1:
                      openParIndex = call[1].index("(")
                      closeParIndex = call[1].index(")")
                      areaCodeSet.add(call[1][openParIndex+1:closeParIndex])
                if call[1].find(areacode) >= 0:
                      bangaloreCalled += 1

sortedCodes = sorted(list(areaCodeSet))
print("The numbers called by people in Bangalore have codes:")
for code in sortedCodes:
      print(code)

print( str(round((bangaloreCalled/bangaloreCalls)*100,2)) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
#You need to calculate all the area codes 
#of the telephone numbers which banglore people called to. Note the area code must be unique.

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#Complexity
""" for loops are O(n)
sorting the areaCodes are O(nlogn) 

the complexity should be O(nlogn) """