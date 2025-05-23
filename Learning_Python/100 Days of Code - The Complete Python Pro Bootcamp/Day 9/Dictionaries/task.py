# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again.",
#                           "apple": "red"}
#
# # print(programming_dictionary["Bug"])
#
# # add new items to dictionary
# programming_dictionary["pear"] = "green."
#
# # print(programming_dictionary)
#
# for things in programming_dictionary:
#     print(things)
#     print(programming_dictionary[things])


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create an empty dictionary to collect the new values.
student_grades = {}

# Loop through each key in the student_scores dictionary
for student in student_scores:

    # Get the value (student score) by using the key each time.
    score = student_scores[student]

    # Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)