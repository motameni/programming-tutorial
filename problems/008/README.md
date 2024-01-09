Problem 8: Class Report Formatter 
 
Background: 
 
Imagine you are a teacher and you have data for students and their marks in different subjects. You want to print a neat report for each student. 
 
Problem Statement: 
 
Given a list of lists containing data for students in the following format: 

```python
 
data = [ 
    ["Name", "Subject", "Marks"], 
    ["John", "Math", 85], 
    ["Jane", "Math", 90], 
    ["John", "History", 78], 
    ["Jane", "History", 88], 
    ["John", "Science", 90], 
    ["Jane", "Science", 87] 
]

```

The first inner list always contains the titles: "Name", "Subject", and "Marks". 
 
Write a Python program that: 
 
Iterates through the list.
 
For each unique student, prints a formatted report with their name, the subjects they've taken, the marks they've received, and an overall grade.
 
The grade is based on the average of their marks and should be classified as follows:
 
Average >= 90: "A" 
Average >= 80 and < 90: "B" 
Average >= 70 and < 80: "C" 
Average < 70: "D"
 
Expected Output (for the given data): 

```python
Report for John: 
Math: 85 
History: 78 
Science: 90 
Overall Grade: B 
 
Report for Jane: 
Math: 90 
History: 88 
Science: 87 
Overall Grade: B
```
