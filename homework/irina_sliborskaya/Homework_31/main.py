import time

seconds = 5
while seconds > 0:
    print(f"You have {seconds} seconds...", end='\r')
    time.sleep(1)
    seconds -= 1

print("\nStop!")
