#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Version 1
# clean_name = []
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     name = names_file.readlines()
#
# for i in name:
#     y = i.strip()
#     clean_name.append(y)
#
# with open("./Input/Letters/starting_letter.txt") as mail:
#     contents = mail.read()
#
# for create_mail in range(len(clean_name)):
#     with open(f"./Output/ReadyToSend/letter_for_{clean_name[create_mail]}.txt", mode='w+') as new_mail:
#         x = contents.replace("[name]", clean_name[create_mail])
#         new_mail.write(x)

# Version 2
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt")  as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w+') as completed_letter:
            completed_letter.write(new_letter)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp