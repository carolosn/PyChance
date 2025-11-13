import random

symbols = ["🍒", "💎",️ "💰"]
points = 0

def play_slots(points):
    print("\n--- SLOT MACHINE ---")
    s1 = random.choice(symbols)
    s2 = random.choice(symbols)
    s3 = random.choice(symbols)
    print(f"[ {s1} ]  [ {s2} ]  [ {s3} ]")

    if s1 == s2 == s3:
        points += 40
        print("JACKPOT! +40 points")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        points += 15
        print("Two matches! +15 points")
    else:
        points -= 5
        print("No match. -5 points")

    print(f"Total Points: {points}")
    return points


while True:
    choice = input("\nPress ENTER to spin or type 'quit' to exit: ")
    if choice.lower() == "quit":
        print("\nThanks for playing!")
        break
    points = play_slots(points)
