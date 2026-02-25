

def calculate_total(sub1, sub2, sub3):
    return sub1 + sub2 + sub3

def calculate_percentage(total):
    return (total/300) * 100

def get_grade(percentage):
    if(percentage >= 75):
        return "A"
    elif(percentage >= 60):
        return "B"
    elif(percentage >= 40):
        return "C"
    elif(percentage < 40):
        return "F"

name = str(input("Enter Name: "))
subject1 = int(input("Enter Subject 1 Mark: "))
subject2 = int(input("Enter Subject 2 Mark: "))
subject3 = int(input("Enter Subject 3 Mark: "))

print(name)
total = calculate_total(subject1, subject2, subject3)
print(f"Total: {total}/300")
percentange = calculate_percentage(total)
print(f"Percentage: {percentange}%",)
grade = get_grade(percentange)
print("Grade: ", grade)