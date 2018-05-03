userInput = input("Please enter any word: ")
letters = list(userInput)
palindrome = True
#reverse_letters = letters[::-1]

#if reverse_letters == letters:
#    print("This word is a palindrome")
#else:
#    print("This word is not a palindrome")
for letter in letters:
    if letter == letters[-1]:
        letters.pop(-1)
    else:
        palindrome = False
        break

print(f"Is {userInput} a palindrome? {palindrome}")
