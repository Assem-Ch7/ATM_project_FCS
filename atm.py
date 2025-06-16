balance = 1000
choice = 0 
password = "1234"
user_password = ""
counter_withdraw = 0
counter_transactions = 0

print("""
Welcome to the ATM!
    Please enter your password to continue:
    """)


while(user_password != password):
    user_password = input()
    if user_password == password:
        print("Password accepted.")
    else:
        print("Incorrect password. Please try again.")
    

print("""
Welcome to the ATM!
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
    """)

while(choice != 4):
    print("Please select an option (1-4): ")
    choice = float(input())
    if choice == 1:
        counter_transactions += 1
        print("Your current balance: ", balance)
    elif choice == 2:
        deposit = float(input("how much to deposit: "))
        if deposit > 0 :
            counter_transactions += 1
            balance += deposit
        else:
            print("Invalid deposit amount.")
    elif choice == 3:
        withdraw = float(input("how much to withdraw: "))
        if withdraw > 0 and withdraw <= balance:
            balance -= withdraw
            counter_transactions += 1
        else:
            counter_withdraw +=1
            print("Invalid withdraw amount.")
            if counter_withdraw >= 3:
                print(counter_withdraw," failed withdrawals were attempted.")         
    elif choice == 4:
        print(counter_transactions, "transactions were made.")
        print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid choice. Please select a valid option (1-4).")