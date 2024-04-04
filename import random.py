import random

def get_user_choice():
    user_choice = input("Enter your choice of word amond (apple, banana, car, mountain, ocean):").lower()
    return user_choice


def get_computer_choice():
    words = ["apple", "banana", "car", "mountain", "ocean"] 
    random_list = [random.choice(words)]
    return random_list

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a match"
    else:
        return "Does not match any choice"

def main():
    print("Welcome to word match!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(get_computer_choice())
        print(f"You chose {user_choice}. The computer chose {computer_choice}.")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()