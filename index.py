def calculateGPA(grades, grade_values):
    credits_attempted = 3*len(grades)
    credits_completed = 0
    
    for grade in grades:
        credits_completed += 3*grade_values[grade]
        
    calculated_gpa = credits_completed/credits_attempted
    
    print(f"Your GPA is : {calculated_gpa}")
    return

def getInput(grade_values):
    course_number = 1
    grades = []
    
    while(True):
        new_grade = input(f"\nWhat letter grade did you recieve in course {course_number} : ")
        
        if new_grade not in grade_values :
            print("--- ERROR --- Please enter a valid grade --- ERROR ---")
        else:

            grades.append(new_grade)
            print(grades)
            
            calculateGPA(grades, grade_values)

            while(True):
            
                contiue_value = input("\nIf you would like to add another grade, enter 'C', otherwise type 'X' : ")

                
                if contiue_value == 'X':
                    return grades
                elif contiue_value == 'C':
                    course_number += 1
                    break
                else:
                    continue
        
def main():
    grade_values = {
        'A+' : 4.0,
        'A' : 4.0,
        'A-' : 3.7,
        'B+' : 3.3,
        'B' : 3.0,
        'B-' : 2.7,
        'C+' : 2.3,
        'C' : 2.0,
        'C-' : 1.7,
        'D+' : 1.3,
        'D' : 1.0,
        'D-' : 0.7,
        'F' : 0.0
    }
    
    getInput(grade_values)
    
if __name__ == '__main__':
    main()