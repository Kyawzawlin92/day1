def calculate_total(scores):
    return sum(scores)
def calculate_average(scores):
    return sum(scores)/len(scores)
def classify_grade(score):
        if score >= 90:
            return "Grade-A"
        elif score >= 60:
            return "Grade-B"
        elif score >= 40:
            return "Grade-C"
        else:
            return "Grade-D"

def count_pass(scores):
            if scores >= 40:
                return "pass"
            else:
                return "fail"

scores = [50,30,45,20,80,95]

total = calculate_total(scores)
print("Total:",total)

average = calculate_average(scores)
print("Average:",average)

print(classify_grade(99))
print(classify_grade(12))

print(count_pass(23))