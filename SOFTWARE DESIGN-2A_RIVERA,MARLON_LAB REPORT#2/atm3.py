from bank import Bank
from savingsaccount import SavingsAccount

bank = Bank()
bank.add(SavingsAccount("Wilma", "1001", 4000.00))
savings = SavingsAccount("Wilma", "1001", 4000.00)
tries = 3
while tries != 0:
    print()
    name = str(input("Name: "))
    pin = int(input("PIN: "))
    account1 = bank.get("Wilma", "1001")
    if pin == "1001":
        if name == "Wilma":
            print("----------Login Success---------")
            print()
            print("Choose an Option")

            print("[A] Get Balance")
            print("[B] Withdraw")
            print("[C] Logout")
            res = input("-> ").upper()

            if res == "A":
                print(savings.getBalance())
            if res == "B":
                print("Successfully withdrawn: ",savings.getBalance())
            if res == "C":
                print("Account Logout")

            break

    elif pin != 1001:
        print()
        print("Incorrect name or pin!")
        tries = tries -1
        if tries == 1:
            print("1 more try or else police will be called")
        
        elif tries == 0:
            input("account disabled...")
            print()





