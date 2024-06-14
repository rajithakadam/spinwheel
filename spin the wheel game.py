import random

print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
print("         Welcome to spin the wheel")
print("                  With bets")
print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
print("There is 5 options on the wheel:")
print("Green doubles your money")
print("Blue loses your money")
print("Yellow 1.5x your money")
print("Red returns your money")
print("Orange loses your money")

def get_new_balance(balance, message):
    while True:
        try:
            deposit = int(input(message))
        except ValueError:
            print("Please enter a numerical amount.")
            continue

        if deposit > 0:
            balance += deposit
            print("Thank you your balance is currently: £", balance)
            return balance
        else:
            print("Please deposit at least £1.")

balance = get_new_balance(0, "Please deposit money to play: £")

while True:
    while True:
        try:
            bet = int(input("Please enter how much you'd like to bet on this spin: £"))
        except ValueError:
            print("Please enter a numerical amount.")
            continue

        if bet > balance:
            print("Please bet an amount that is no larger than your balance of: £", balance)
        else:
            print("Thank you, you have just bet: £", bet)
            balance -= bet
            break

    colours = {"green": bet*2, "blue": 0, "yellow": bet*1.5, "red": bet, "orange": 0}
    colour, outcome = random.choice(list(colours.items()))

    start = input("Hit enter to spin the wheel")
    print("It landed on:", colour)
    if outcome == 0:
        print("That means you lost your bet of £", bet)
    if outcome == bet:
        print("You got your money back.")
    if outcome > bet:
        print("You made: £", outcome - bet, "So got £", outcome, "back.")

    balance += outcome
    print("Your balance is now: £", balance)

    again = input("Would you like to play another round? ").lower()
    if again in ("yes", "y"):
        if balance < 1:
            balance = get_new_balance(balance, "You have run out of money. Please deposit more money to keep playing. £")

    else:
        print("Thank you for playing")
        print("Your final balance was: £", balance)
        if balance > 0:
            withdraw = input("Would you like to withdraw your money? ").lower()
            if withdraw in ("yes", "y", "please"):
                print("We have deposited your balance of £", balance, "into your bank account.")
                balance = 0
                print("Your balance is now: £", balance)
            else:
                print("That's ok, we will keep your money for next time you play.")
        break

