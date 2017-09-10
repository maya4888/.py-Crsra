name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        #print(words)

for email in words:
    email=words[1]
    d[email]=d.get(email,0)+1
    #print(d)

winneremail = None
largestcount = None
for email,count in d.items():
    if largestcount is None or count > largestcount:
        winneremail = email
        largestcount = count
print(winneremail,largestcount)
