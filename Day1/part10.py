def calculate_average(scores):
    return sum(scores) / len(scores)

def classify_grade(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"

def count_passed(students):
    return sum(1 for s in students if s['score'] >= 40)

# Main Program
students = []

print("===== STUDENT PERFORMANCE DATA ENTRY =====")
for i in range(1, 6):
    print(f"\nStudent {i}")
    name = input("Name: ")
    age = int(input("Age: "))
    study_hours = float(input("Study Hours: "))
    score = float(input("Score: "))
    
    students.append({
        "name": name,
        "age": age,
        "study_hours": study_hours,
        "score": score,
        "grade": classify_grade(score)
    })

print("\n===== STUDENT PERFORMANCE REPORT =====")
for s in students:
    print(f"\nName: {s['name']}")
    print(f"Age: {s['age']}")
    print(f"Study Hours: {s['study_hours']}")
    print(f"Score: {s['score']}")
    print(f"Grade: {s['grade']}")

scores = [s['score'] for s in students]
print("\n===== SUMMARY =====")
print(f"Total Students: {len(students)}")
print(f"Average Score: {calculate_average(scores)}")
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Passed Students: {count_passed(students)}")
print(f"Failed Students: {len(students) - count_passed(students)}")
print(f"Top Student: {max(students, key=lambda x: x['score'])['name']}")