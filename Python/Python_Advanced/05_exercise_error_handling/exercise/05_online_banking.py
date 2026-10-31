class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


def send_money(i_send_money, my_balance, entered_pin, my_pin, my_age):
    if i_send_money > my_balance:
        raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
    if entered_pin != my_pin:
        raise PINCodeError("Invalid PIN code")
    if my_age < 18:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
    my_balance -= i_send_money
    print(f"Successfully sent {i_send_money:.2f} money to a friend")
    print(f"There is {my_balance:.2f} money left in the bank account")
    return my_balance


def receive_money(salary, my_balance):
    if salary < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")
    my_balance += salary * 0.5
    print(f"{salary * 0.5:.2f} money went straight into the bank account")
    return my_balance


pin, balance, age = map(int, input().split(", "))

while True:
    commands = input().split("#")
    if commands[0] == "End":
        break
    money = int(commands[1])
    if commands[0] == "Send Money":
        entered_pin_code = int(commands[2])
        balance = send_money(money, balance, entered_pin_code, pin, age)
    elif commands[0] == "Receive Money":
        balance = receive_money(money, balance)
