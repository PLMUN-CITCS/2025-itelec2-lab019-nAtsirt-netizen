import unittest

def get_student_grade(score):
    """Calculates the grade based on the given score."""
    if not 0 <= score <= 100:
        return "Invalid Score"
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
    """Main function to demonstrate the grading."""
    score = 85  # Example score
    grade = get_student_grade(score)
    print(f"The student's grade is: {grade}")

class TestGrading(unittest.TestCase):
    """Unit tests for the grading functions."""

    def test_calculate_grade_a(self):
        self.assertEqual(get_student_grade(95), 'A')

    def test_calculate_grade_b(self):
        self.assertEqual(get_student_grade(85), 'B')

    def test_calculate_grade_c(self):
        self.assertEqual(get_student_grade(75), 'C')

    def test_calculate_grade_d(self):
        self.assertEqual(get_student_grade(65), 'D')

    def test_calculate_grade_f(self):
        self.assertEqual(get_student_grade(55), 'F')

    def test_calculate_grade_zero(self):
        self.assertEqual(get_student_grade(0), 'F')

    def test_calculate_grade_hundred(self):
        self.assertEqual(get_student_grade(100), 'A')

    def test_calculate_grade_invalid_negative(self):
        self.assertEqual(get_student_grade(-10), "Invalid Score")

    def test_calculate_grade_invalid_over_hundred(self):
        self.assertEqual(get_student_grade(110), "Invalid Score")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # run all tests
    main() # run the main function.
