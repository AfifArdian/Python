import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = input("what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n")

if choose == "0":
    print(rock)
elif choose == "1":
    print(paper)
elif choose == "2":
    print(scissors)
else:
    print("Wrong inputs")

print("Computer  chose: ")

num = ["0", "1", "2"]

choose2 = random.choice(num)

if choose2 == "0":
    print(rock)
elif choose2 == "1":
    print(paper)
elif choose2 == "2":
    print(scissors)
else:
    print("Wrong inputs")

if choose == "0" and choose2 == "0":
    print("draw")
elif choose == "1" and choose2 == "1":
    print("draw")
elif choose == "2" and choose2 == "2":
    print("draw")
elif choose == "0" and choose2 == "1":
    print("you lose")
elif choose == "0" and choose2 == "2":
    print("you win")
elif choose == "1" and choose2 == "0":
    print("you win")
elif choose == "1" and choose2 == "2":
    print("you lose")
elif choose == "2" and choose2 == "0":
    print("you lose")
elif choose == "2" and choose2 == "1":
    print("you win")