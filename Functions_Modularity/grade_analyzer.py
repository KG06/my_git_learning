
# Task 1 — Process the Scores
def process_scores(students):
    student_name = students["name"]
    total_marks = average = 0
    total_subjects = len(students["marks"])
    for marks in students["marks"]:
        total_marks += marks
    
    average = round((total_marks/total_subjects),2)
    
    return {student_name : average}

# Task 2 — Classify the Grades
def classify_grades(averages):
    data = {}
    for name in averages:
        grade = "F"
        if averages[name] >= 90:
            grade = "A"
        elif averages[name] >= 75:
            grade = "B"
        elif averages[name] >= 60:
            grade = "C"
       
        data[name] = (averages[name], grade)     
    
    return data

def generate_report(classified, passing_avg = 70):
    for result in classified:
        status = "FAIL"
        if classified[result][0] >= passing_avg:
            status = "PASS"
        print(f"{result}    | Avg: {classified[result][0]} | Grade: {classified[result][1]} | Status: {status}")
    return status


total_students = passed = failed = 0 

student_data = [
    {"name":"Student 1", "marks": [75, 80, 90]}, 
    {"name":"Student 2", "marks": [85, 82, 89]}, 
    {"name":"Student 3", "marks": [98, 95, 90]}
]

print("===== Student Grade Report =====")

for student in student_data:
    total_students += 1
    averages = process_scores(student)
    classified = classify_grades(averages)
    status = generate_report(classified)

    if status == "PASS":
        passed += 1
    else:
        failed += 1

print("================================")
print(f"Total Students : {total_students}")
print(f"Passed         : {passed}")
print(f"Failed         : {failed}")