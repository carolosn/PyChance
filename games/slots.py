import random

def play():
    print("\n🎰 Welcome to Slots!")

    print("No matches equal -5 points!")
    print("Two matches equal 15 points!")
    print("Jackpot! 3 matches equal 40 points!")
50

symbols = ['🍒', '🍋', '7️⃣', '🍀']

def spin():
    return [random.choice(symbols) for _ in range(3)]

def check_win(spins):
    return spins[0] == spins[1] == spins[2]

def play_game():
    points = 100 
    print("Welcome to the Python Slot Machine!")
    print(f"You start with {points} points.")
    
    while points > 0:
        print(f"\nYou have {points} points.")
        
        bet = input(f"How many points would you like to bet? (You have {points} points): ")

        try:
            bet = int(bet)
            if bet <= 0:
                print("You must bet a positive number of points.")
                continue
            if bet > points:
                print("You cannot bet more points than you have.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        input("Press Enter to spin the reels... 🍀🍀🍀")
        spins = spin()
        print(f"Result: {spins[0]} | {spins[1]} | {spins[2]}")
        
        if check_win(spins):
            points += bet  
            print(f"You win! 🎉 You earned {bet} points!")
        else:
            points -= bet  
            print(f"You lose! 😔 You lost {bet} points.")
        
        if points <= 0:
            print("\nYou are out of points! Game over.")
            break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Thanks for playing! You finished with {points} points. Goodbye! 👋")
            break

if __name__ == "__main__":
    play_game()
