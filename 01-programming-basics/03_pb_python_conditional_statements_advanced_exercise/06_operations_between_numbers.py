n1 = int(input())
n2 = int(input())
operator_symbol = input()
result = 0
error = ""
flag = "no"
result_even_odd = "odd"

if operator_symbol in("+","-","*"):
    flag = "yes"
if operator_symbol == "+":
    result = n1 + n2
elif operator_symbol == "-":
    result = n1 - n2
elif operator_symbol == "*":
    result = n1 * n2
elif n2 == 0:
    error = "error"
    print(f"Cannot divide {n1} by zero")
elif (operator_symbol == "%") and (error == ""):
    result = n1 % n2
    print(f"{n1} % {n2} = {result}")
elif (operator_symbol == "/") and (error == ""):
    result = n1 / n2
    print(f"{n1} / {n2} = {result:.2f}")

if result % 2 == 0:
    result_even_odd = "even"

if flag == "yes":
    print(f"{n1} {operator_symbol} {n2} = {result} - {result_even_odd}")
