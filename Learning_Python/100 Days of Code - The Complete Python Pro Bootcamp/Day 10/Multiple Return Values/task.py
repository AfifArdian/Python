def format_name(f_name, l_name):
    if f_name == "" or l_name ==  "":
        print("you did not provide valid inputs ")
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result : {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name? "),input("What is your last name? ")))

# latihan coding 10:Leap year
# def is_leap_year(year):
#     # Write your code here.
#     # Don't change the function name.
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True
#
# print(is_leap_year(2020))