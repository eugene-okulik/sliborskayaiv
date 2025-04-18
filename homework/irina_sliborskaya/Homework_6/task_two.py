for num in range(1, 101):
    if num % 3 == 0:
        if num % 5 != 0:
            print('Fuzz')
        else:
            print('FuzzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
