largest = None
smallest = None
while True:
    value = input("Enter a number: ")
    if value == "done" : break
    try:
        fnum = float(value)
    except:
        print('Invalid input')
for value in [7, 2, 10, 4]:
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
print("Maximum is", largest)
for value in [7, 2, 10, 4]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
print("Minimum is", smallest)
