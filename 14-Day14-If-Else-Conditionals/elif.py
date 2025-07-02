num = int(input("Enter a number: "))  # Added input to define 'num'

if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
elif num == 999:
    print("Number is special")
else:
    print("Positive")
