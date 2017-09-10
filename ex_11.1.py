import re

hand = open('regex_sum_3684.txt')
x = hand.read()
newelement=0
y = re.findall('[0-9]+',x)
#print(y)
for element in y:
    z = int(element)
    newelement = z + newelement
print(newelement)
