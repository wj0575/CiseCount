import math

priority_dict = {
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2
}

def fraction(up, down):
    """构造有理数类型"""
    if down == 0:
        print("error")
        return [0, 1]
    if down < 0:
        up = -up
        down = -down
    return [up, down]

def simplify_fraction(x):
    """化简有理数"""
    gcd = math.gcd(x[0], x[1])
    return [x[0] // gcd, x[1] // gcd]

def calculate_fraction(operator, x, y):
    # 如果x y 中有字符出现，返回错误
    if not isinstance(x, list) or not isinstance(y, list):
        print("variable error")
        return "#变量未定义#"
    if operator == '+':
        return simplify_fraction([x[0] * y[1] + y[0] * x[1], x[1] * y[1]])
    elif operator == '-':
        return simplify_fraction([x[0] * y[1] - y[0] * x[1], x[1] * y[1]])
    elif operator == '*':
        return simplify_fraction([x[0] * y[0], x[1] * y[1]])
    elif operator == '/':
        if y[0] == 0:
            print("divisor can't be 0")
            return "#除数不能为零#"
        return simplify_fraction([x[0] * y[1], x[1] * y[0]])
    elif operator == '^':
        if y[1] != 1:
            print("under fraction mode, the index must be integer")
            return "#有理数内不能开分数次方#"
        return simplify_fraction([x[0] ** y[0], x[1] ** y[0]])
    else:
        print("operator symbol error")
        return "#运算符错误#"

def print_fraction(x):
    """打印有理数"""
    if x[1] == 1:
        print(x[0])
    if x[0] == 0:
        print(0)
    else:
        print(x[0], '/', x[1])

def fraction_show(x, y):
    """返回有理数的字符串形式"""
    if y == 1:
        return str(x)
    if x == 0:
        return str(0)
    elif len(str(x/y)) < 8:
        return str(x) + '/' + str(y) + ' ( ' + str(round(x/y, 5)) + ' )'
    else:
        return str(x) + '/' + str(y)
