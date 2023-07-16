import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Roll Game!")
    while True:
        user_input = input("Press 'r' to roll the dice or 'q' to quit: ")
        if user_input.lower() == 'q':
            print("Thank you for playing!")
            break
        elif user_input.lower() == 'r':
            result = roll_dice()
            print(f"You rolled a {result}")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()