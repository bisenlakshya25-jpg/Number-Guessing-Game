import random
# function for valid input

def check_input(prompt, max_val = 3, min_val = 1, allow_quit = False):
    while True:
        value = input(prompt)

        if allow_quit and value.lower() == "q":
            return "q"

        try:
            num = int(value)
            if min_val <= num <= max_val:
                return num
            else:
                print("Invalid input! Please enter a value between", min_val, "and", max_val)
        except ValueError:
          print("Invalid input! Please enter a valid integer.")


# function to call game end
def game_end():
    print()
    print("Do you want to play againn\n1. Yes \n2. No")
    your_chose = check_input("Your Choice:", max_val = 2)
    if your_chose == 1:
      return (your_chose  == 1)
    else:
      print("Thanks for playing❤️")
     # if answer == 1:
       # print()
     # else:
         # print("Thanks for playing❤️")

# function to run the game
def game_run(target, maximum):
    attempts = 0
    while True:
        attempts += 1
        user_choice = check_input("Guess the target or Quit(Q):" , max_val = maximum, allow_quit = True)
        if user_choice == "q":
            return
        elif user_choice == target:
            if attempts <= 3:
                print ("Excellent ! \nYou guessed the number in", attempts, " attempts")
            elif 3 < attempts <= 7:
                print ("Great job! \nYou guessed the number in", attempts, " attempts")
            else:
                print ("keep practising! \nYou guessed the number in", attempts, " attempts")
            return

        elif user_choice < target:
            print("Your number was small. Take a bigger guess….")

        else:
            print("Your number was big. Take a smaller guess….")


# function to choose difficulty
def choose_difficulty ():
    print("==============================\n Number Guess Game \n==============================")
    print()
    print("Choose Difficulty Level:- \n1. Easy(1-50) \n2. Medium(1-100)  \n3. Hard(1-500) \n")

    while True:
        difficulty_level = check_input("Enter your choice:")
        if difficulty_level == 1:
            print ("You selected Easy mode. \nGuess the number between 1 and 50")
            target = random.randint(1, 50)
            game_run(target, 50)
            return
        elif difficulty_level == 2:
            print ("You selected Medium mode. \nGuess the number between 1 and 100")
            target = random.randint(1, 100)
            game_run(target, 100)
            return
        else:
            print ("You selected Hard mode. \nGuess the number between 1 and 500")
            target = random.randint(1, 500)
            game_run(target, 500)
            return


# funtion to show rule of the game
def show_rules():
    print("=============================== \n                 GAME RULES              \n===============================\n \n 1. The computer will randomly choose a number. \n2. Your task is to guess the correct number. \n3. Choose a difficulty level before starting:\n    • Easy   : 1 to 50 \n    • Medium : 1 to 100 \n    • Hard   : 1 to 500 \n4. After every guess, you will receive a hint:\n    • Too High \n.    • Too Low\n5. Keep guessing until you find the correct number. \n6. Your total number of attempts will be displayed when you win. \n7. You can choose to play again after the game ends. \n8. Enter valid numbers only.\n9. Have fun and challenge yourself! \n=============================== \n.    Best of Luck! 🎯\n===============================")
  
    next_choice = check_input("If you want to return to previous menu enter 1", max_val = 1)
    if next_choice == 1:
      return True
# function for calling main screen
def main_screen():
    print("==============================\n Number Guess Game \n============================== \n1. Start Game \n2. Rules \n3. Exit")
    choice = check_input("Enter Choice:")
    if choice == 1:
        choose_difficulty()
        return True
    elif choice == 2:
        show_rules()
        return True
    else:
        print("Thanks for playing. \nGoodbye👋🏻")
        return False

# calling to intiate our code
while True:
    main_screen()
    
    if not main_screen():
        break

    if not game_end():
        break