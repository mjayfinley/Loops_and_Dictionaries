userInput = int(input("Please enter a number: "))

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    x = 5
    y = 2

    while x * x <= n:
        if n % x == 0:
            return False

        x += y
        y = 6 - y

    return True

print(f"Is {userInput} a prime number? {is_prime(userInput)}")
