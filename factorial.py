userInput = int(input("Please enter a number: "))
number = 1

while userInput >= 1:
    number = number * userInput
    userInput = userInput - 1

print(f"The factorial is {number}")
