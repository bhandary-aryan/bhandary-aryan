import random

def get_computer_choice():
    choices = ['Snake', 'Water', 'Gun']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == 'Snake':
        if computer_choice == 'Water':
            return "You win! Snake drinks Water."
        else:
            return "Computer wins! Gun shoots Snake."
    elif player_choice == 'Water':
        if computer_choice == 'Gun':
            return "You win! Water extinguishes Gun."
        else:
            return "Computer wins! Snake drinks Water."
    elif player_choice == 'Gun':
        if computer_choice == 'Snake':
            return "You win! Gun shoots Snake."
        else:
            return "Computer wins! Water extinguishes Gun."

def main():
    print("Welcome to the Snake Water Game!")
    print("Choose one: Snake, Water, Gun")
    
    while True:
        player_choice = input("Your choice: ").capitalize()
        if player_choice not in ['Snake', 'Water', 'Gun']:
            print("Invalid choice. Please choose from Snake, Water, or Gun.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
