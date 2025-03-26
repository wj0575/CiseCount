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
            print("#除数不能为零#")
            return "#除数不能为零#"
        return x / y
    elif operator == '^':
        return x ** y
    else:
        print("运算符错误")
        return "#运算符错误#"