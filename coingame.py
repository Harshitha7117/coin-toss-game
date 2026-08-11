import random

print("==============================")
print("       COIN TOSS GAME")
print("==============================")

player_score = 0
computer_score = 0
rounds = 5

for i in range(1, rounds + 1):
    print("\nRound", i)

    choice = input("Choose Heads or Tails: ").lower()

    while choice not in ["heads", "tails"]:
        print("Invalid choice! Please choose Heads or Tails.")
        choice = input("Choose Heads or Tails: ").lower()

    coin = random.choice(["heads", "tails"])

    print("Coin result:", coin)

    if choice == coin:
        print("You won!")
        player_score += 1
    else:
        print("Computer won!")
        computer_score += 1

print("\n==============================")
print("        FINAL RESULT")
print("==============================")
print("Your score:", player_score)
print("Computer score:", computer_score)

if player_score > computer_score:
    print("🎉 You are the winner!")
elif computer_score > player_score:
    print("Computer is the winner!")
else:
    print("It's a tie!")
