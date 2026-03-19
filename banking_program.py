# show balance
# deposit
# withdraw

def show_balance():
    print(f"Your Balance is ${balance: .2f}")


def deposit():
    amount = float(input("Enter the amount you want to deposit: "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount


def withdraw():
    amount = float(input("Enter the amount you want to withdraw: "))
    if amount > balance:
        print("You dont have enough money")
        return 0
    elif amount < 0:
        print("This is an invalid amount!")
        return 0
    else:
        return amount


balance = 0

while True:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = input("enter (1-4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
        print(f"You have deposited a total of: ${balance: .2f}")
    elif choice == "3":
        amount2 = withdraw()
        balance -= amount2
        print(f"You have withdrawn ${amount2}")
        print(f"Your balance is {balance}")
    elif choice == "4":
        break
    else:
        print("Please enter a Valid Choice")
print("Thank you and have a nice day")
