import math
def calculate_realness(operator, x, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        if y == 0:
            print("divisor can't be 0")
            return 0
        return x / y
    elif operator == '^':
        return x ** y
    else:
        print("operator symbol error")