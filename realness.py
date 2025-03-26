import math
def calculate_realness(operator, x, y):
    # 如果x y 中有字符出现，返回错误
    if not isinstance(x, list) or not isinstance(y, list):
        print("variable error")
        return "#变量未定义/数值过大#"
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