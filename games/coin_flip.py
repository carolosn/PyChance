import random

def play():
    print("\n🪙 Welcome to the Coin Flip Game!")
    choice = input("Heads or Tails? ").lower()
    result = random.choice(["heads", "tails"])
    print(f"The coin landed on {result}.")

    if choice == result:
        print("🎉 You win!\n")
    else:
        print("😢 You lose.\n")
