name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    #print(words)
    for w in words:
        print(w)
        if w in d:
            d[w]=d[w] + 1
        else:
            d[w]=1
        print(d[w])
