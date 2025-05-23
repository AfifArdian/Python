# # Write your code below this line 👇
# # print("Hello " + input("what is your nama? ") + "!")
# print("e.g. " + "Hello " + input("what is your nama? ") + "!")

def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower()
    true_count = 0
    for letter1 in "True".lower():
        for letter2 in combined_name:
            if letter1 == letter2:
                true_count += 1

    love_count = 0
    for letter1 in "Love".lower():
        for letter2 in combined_name:
            if letter1 == letter2:
                love_count += 1


    print(f"Love Score = {true_count}{love_count}")

# Call your function with hard coded values
calculate_love_score( "Angela Yu","Jack Bauer")

