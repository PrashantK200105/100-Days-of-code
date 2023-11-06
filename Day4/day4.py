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

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]
user_input = int(input("0 for rock, 1 for paper, 2 for scissior\n"))

if user_input >= 3 and user_input <= 0:
  print("You typed an invalide number, you lose.")
else:
  print(game_images[user_input])

computer_value = random.randint(0,2)
print("computer choose:")
print(game_images[computer_value])


if user_input == 0 and computer_value == 2:
  print("You win!")
elif computer_value == 0 and user_input == 2:
  print("You lose!")

elif computer_value > user_input:
  print("You lose!")
elif user_input > computer_value:
  print("You win!")
elif computer_value == user_input:
  print("It's a draw")


