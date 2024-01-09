Problem 20:

You are given a list of names and ages. Your task is to print the names of people who are 18 years or older in the following format:

```
<Name> is <Age> years old.
```
If a person is younger than 18, print:
```
<Name> is a minor.
```

Write a Python program that takes the input as a list of tuples, where each tuple contains a name and an age. The program should use a for loop and if-else statements to format and print the output as described above.

Here's a sample input and output:

Input:
```
people = [("Alice", 25), ("Bob", 17), ("Charlie", 20), ("David", 16), ("Eva", 22)]
```
Output:
```
Alice is 25 years old.
Bob is a minor.
Charlie is 20 years old.
David is a minor.
Eva is 22 years old.
```