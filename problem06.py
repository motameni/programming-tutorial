grades = [18.75, 20, 15.5, 10, 8, 13.75]

for grade in grades:
    if grade < 14:
        print(grade, "- D")
    elif grade < 17:
        print(grade, "- C")
    elif grade < 19:
        print(grade, "- B")
    else:
        print(grade, "- A")
