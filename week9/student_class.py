def student_in_class(student_name,student_list):
    if student_name in student_list:
        print('{} is in this class'.format(student_name))
    else:
        print('{} is not in this class'.format(student_name))

student_list = ['Ana','Maria','Joana','Joao']
student_name = input('Please enter the student name')
student_in_class(student_name,student_list)
#update_marks(student_name,mark_sheet)
