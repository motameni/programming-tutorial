Problem 24: Palindrome Checker

Write a Python program that checks whether a given string is a palindrome or not. A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward.

Your program should define a class called PalindromeChecker with the following methods:

init(self, input_str): Initializes the PalindromeChecker object with the input string.

is_palindrome(self): Checks if the input string is a palindrome. Returns True if it is a palindrome, and False otherwise.

You need to implement the class and use it to check whether the provided string is a palindrome or not.

Example:

```python
# Input
user_input = input("Enter a string: ")

# Create PalindromeChecker object
palindrome_checker = PalindromeChecker(user_input)

# Check if it's a palindrome
if palindrome_checker.is_palindrome():
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
```

Sample Output:
```
Enter a string: racecar
racecar is a palindrome.
```
