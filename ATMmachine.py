import time
print("Enter your CARD to continue to BHARAT bank")
time.sleep(6)
password=1111
pin=int(input("Enter your ATM PIN "))
balance=100000

if pin==password:
    while True:
        print("""
    1 == CURRENT BALANCE
    2 == WITHDRAW CASH
    3 == DEPOSIT CASH
    4 == EXIT
    """)
try:
    option=int(input("Enter your choice"))
except:
    print("Please enter any Valid choice")

if option == 1:
   print(f"Your CURRENT BALANCE is {balance}")
if option == 2:
    withdraw_amount=int(input("Enter the amount you want to WITHDRAW"))
    balance=balance-withdraw_amount
    print(f"{withdraw_amount}is DEBITED from your account")
    print(f"Your current balance is {balance}")
if option == 3:
    deposit_amount=int(input("Enter the amount you want to DEPOSIT"))
    balance=balance+deposit_amount
    print(f"{deposit_amount}is CREDITED to your account")
    print(f"Your Updated balance is {balance}")
if option == 4:
     break
else:
    print("You have inserted WRONG PIN, Please try again or visit nearest branch.")
