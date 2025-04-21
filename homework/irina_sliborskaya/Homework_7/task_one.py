i = 24
while True:
    user_input = int(input("Guess the number: "))
    if user_input == i:
        print("Congrats! You win!")
        break
    else:
        print("Try again!")
