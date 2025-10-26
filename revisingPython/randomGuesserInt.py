import random

target = random.randint(1, 100)
i = 0
print("Welcome to the Number Guessing Game!\nYou have to guess a number between 1 to 100 in 10 attempts.\nYou can also quit anytime by entering 'Q'.")
while i<10:
    i+=1
    userChoice = input("Enter your guess (1-100) or Quit(Q): ")
    if userChoice.lower() == 'q':
        print(f"You chose to quit. The correct number was {target}.")
        break
    try:
        userChoice = int(userChoice)
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 100.")
        continue
    print(f"Attempt {i} of 10:")
    if userChoice==target:
        print(f"Congratulations! You've guessed the correct number at attempt {i}th attempt.")
        break
    elif userChoice<target:
        print("The number is too low! Take a bigger guess.")
    else:
        print("The number is too high! Take a smaller guess.")