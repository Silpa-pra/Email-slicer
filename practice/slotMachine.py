#python slot machine

import random


def spin_row():
    symbols = ['🍒', '💎', '7️⃣', '🔔', '🍋']
    
    return [random.choice(symbols) for _ in range(3)]

"""   results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results """


def print_row(row):
    print("************************")
    print(" | ".join(row))
    print("************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 1
        elif row[0] == '💎':
            return bet * 3
        elif row[0] == '7️⃣':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🍋':
            return bet * 15
    return 0    
    
        
def main():
    balance = 100

    print("******************************")
    print("Welcome to PYthon Slot Machine")
    print("Symbols: 🍒 💎 7️⃣  🔔 🍋 ")
    print("******************************")

    while balance > 0:
        print(f"Current balance: €{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number!!")
            continue

        bet = int(bet)
        if bet > balance:
            print(f"Insufficient Balance, your current Balance is €{balance}")
            continue

        if bet<=0:
            print("Bet amount must be greater than 0")
            continue        


        balance -= bet

        row = spin_row()
        print("SPINNING......")
        print_row(row)


        payout = get_payout(row, bet)

        if payout > 0:
            print(f"YEAH!! You won €{payout}")
        else:
            print("-_- SORRY you lost!! -_-")
        
        balance += payout

        play_again = input("Do you want to SPIN again? (Y/N): ").upper()

        if play_again != 'Y':
            break
      

    print("*********************************************")
    print(f"GAME OVER!!! Your final balance is €{balance}")
    print("*********************************************")

    
if __name__ == '__main__':
    main()