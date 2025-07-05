def get_grade_point(letter_grade):
    # Map letter grades to GPA points
    grade_points = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }
    
    letter_grade = letter_grade.upper()
    
    if letter_grade in grade_points:
        return grade_points[letter_grade]
    else:
        return None

def calculate_gpa(grade_points_list):
    total_points = 0.0
    count = len(grade_points_list)
    
    if count == 0:
        return 0.0
    
    for point in grade_points_list:
        total_points += point
    
    return total_points / count

def main():
    print("=== Student Grade Calculator ===")
    
    number_of_courses = int(input("Enter number of courses: "))
    
    course_names = []
    course_grades = []
    
    for i in range(number_of_courses):
        print(f"\nCourse {i + 1}:")
        
        course_name = input("Enter course name: ")
        course_names.append(course_name)
        
        grade = input("Enter letter grade (A-F): ")
        
        grade_point = get_grade_point(grade)
        
        if grade_point is None:
            print("Invalid grade entered. Please enter a valid letter grade (A, B, C, D, F).")
            return
        
        course_grades.append(grade_point)
    
    gpa = calculate_gpa(course_grades)
    
    print("\n--- Grade Report ---")
    
    for i in range(number_of_courses):
        print(f"{course_names[i]}: Grade Point = {course_grades[i]}")
    
    print(f"\nCalculated GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()
