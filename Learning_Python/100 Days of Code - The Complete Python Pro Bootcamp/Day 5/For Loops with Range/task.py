# gauss = 0
#
# for number in range(1, 101):
#     gauss += number
#
# print(gauss)

for number in range(1, 100):  # Loop dari 1 sampai 100
    if number %3 == 0 and number %5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:  # Jika habis dibagi 3
        print("Fizz")
    elif number %5 == 0:
        print("Buzz")
    else:
        print(number)