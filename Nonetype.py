largest = None
smallest = None
while True:
    n = input("Enter a number: ")
    print(n)
    if n == 'done':
        break
    try:
        num = float(n)
    except:
        print("Invalid input")
        continue

for i in [7,2,10,4]:
    if largest is None:
        largest = i
    elif i > largest:
        largest = i
        print('Maximum is', i)


for value in [7,2,10,4]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
        print('Minimum is', value)
