def generator():
    num1 = 0
    num2 = 1

    while True:
        yield num1
        num1, num2 = num2, num1 + num2


position = int(input("Enter position of the number: "))
count = 0
for number in generator():
    if count == position:
        print(number)
        break
    count += 1
