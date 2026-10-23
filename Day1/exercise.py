mark = int(input("Enter your mark: "))

if mark < 0 or mark >100:
    print(f"Invalid mark:{mark}")
elif mark >= 80:
    print("Excellient")
elif mark >= 60:
    print("Good")
elif mark >= 40:
    print("Pass")
else:
    print("Fail")