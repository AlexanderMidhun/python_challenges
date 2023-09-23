# Write Python code which Accept the student name and in turn
# returns their respective Mark. Make sure to use dictionaries to store
# student name and their respective mark. The dictionary should
# include at least 7 elements.
student_dict = {
    'Sam' : 88,
    'Jo' : 98,
    'Ram' : 97,
    'Jiss' : 95,
    'Hari' : 96,
    'Harry' : 99,
    'Alex' : 97,
}

def student_mark():
    student_name = input("Enter the student name : ")
    # print(student_dict[student_name])
    if student_name in student_dict:
        mark = student_dict[student_name]
        print("Name :" , student_name)
        print("Mark :" , mark)
    else:
        print("No mark for " + student_name)

student_mark()
student_mark()