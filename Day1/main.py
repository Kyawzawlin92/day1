student_name = "Kyaw Kyaw"
age = 22
python_score = 85.5
is_pass = True

print(student_name)
print(age)
print(python_score)
print(is_pass)

name = input("Enter your name")
age = int(input("Enter your age"))
score = float(input("Enter your score"))

print(f"Name:{name}")
print(f"Your age next year is: {age+1} ")
print(f"Your score is {score}")

marks = float(input("Enter your marks:"))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

import numpy as np
data =np.array([10,20,30,40,50])
print("Original array",data)
double = data * 2
print("Multiple with two",double)

