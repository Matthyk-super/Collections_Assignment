def get_letter_grade(avg_score):
    if avg_score >= 90:
        return "A"
    elif avg_score >= 80:
        return "B"
    elif avg_score >= 70:
        return "C"
    elif avg_score >= 60:
        return "D"
    else:
        return "F"

student_name = input("Enter the student's name: ")

grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))
#The print is just there to separate the line between grade5 and print student_name
print()
total_score = grade1 + grade2 + grade3 + grade4 + grade5
average_score = total_score / 5

letter_grade = get_letter_grade(average_score)
print(f"{student_name}")
print(f"Average: {average_score:.1f}")
print(f"Letter Grade: {letter_grade}")