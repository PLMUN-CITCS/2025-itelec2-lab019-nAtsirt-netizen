
def get_student_score():
    
    while True:
        try:
            score = float(input("Enter the student's score: "))
            if 0 <= score <= 100:
                return score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score):

    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

def main():

    score = get_student_score()
    grade = calculate_grade(score)
    print(f"The student's grade is: {grade}")

if _name_ == "_main_":
    main()
