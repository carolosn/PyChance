import random

def play():
    print("\n🎡 Welcome to the Roulette Game!")

    print("You can bet on:")
    print("1. Red or Black")
    print("2. Odd or Even")

    bet_type = input("Choose your bet type (1 or 2): ")

    if bet_type == "1":
        color_choice = input("Pick a color (red or black): ").lower()
        result_color = random.choice(["red", "black"])
        print(f"The wheel landed on {result_color}.")

        if color_choice == result_color:
            print("🎉 You win!\n")
        else:
            print("😢 You lose.\n")

    elif bet_type == "2":
        number = random.randint(0, 36)
        print(f"The wheel landed on {number}.")
        if number == 0:
            print("House wins! You lose.\n")
        else:
            choice = input("Odd or Even? ").lower()
            if (number % 2 == 0 and choice == "even") or (number % 2 != 0 and choice == "odd"):
                print("🎉 You win!\n")
            else:
                print("😢 You lose.\n")
    else:
        print("Invalid choice. Please select 1 or 2.\n")
