fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    print(words)
for element in words:
    if element in lst:
        continue
    else:
        lst.append(element)
print(lst)



fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l = line.rstrip()
    words = line.split()
    #print(words)
    for l in words:
        if words in lst:
            continue
        else:
            lst.append(l)
            lst.sort()
print(lst)
