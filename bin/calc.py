def calc():
    op = input("Operation(+|-|*|/): ")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    if op == "+":
        res = num1 + num2
    if op == "-":
        res = num1 - num2
    if op == "*":
        res = num1 * num2
    if op == "/":
        res = num1 / num2
    print("Result:")
    print(res)