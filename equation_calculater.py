import math
from fraction import fraction, simplify_fraction, calculate_fraction
from realness import *
from number_in import *

priority_dict = {
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
}
def priority(operator1, operator2):
    return priority_dict[operator1] - priority_dict[operator2]

def add_multiple_operators(text):
    """加入表达式中省略的乘号"""
    result = []
    for index, i in enumerate(text):
        if index == 0:
            continue
        if i not in ['+', '-', '*', '/', '^', '(', ')'] and len(result) > 0:
            if not text[index - 1] in ['+', '-', '*', '/', '^', '(', ')']:
                result.append('*')
        if i == '(':
            if not text[index - 1] in ['+', '-', '*', '/', '^', '(', ')']:
                result.append('*')
        if i not in ['+', '-', '*', '/', '^', '(', ')']:
            if text[index - 1] == ')':
                result.append('*')
        result.append(i)
    return result

def make_list(variables, fraction_enable):
    """将变量列表转换为字典"""
    list = {}
    variables = variables.split(' ')
    for i in range(len(variables)):
        try:
            tmp = variables[i].split('=')
            list[tmp[0]] = tmp[1]
        finally:
            continue
    return list

def equation_calculater(text, variables, fraction_enable=False):
    list_of_variables = make_list(variables, fraction_enable=fraction_enable)
    text = text.replace(' ', '')
    text = text.replace('**', '^')
    s = []
    stack_operator = []
    stack_num = []
    print(text, list_of_variables)
    if fraction_enable:# 有理数（分数）模式
        for i in text:
            if i.isdigit() or i == '.':
                if s and (s[-1].isdigit() or '.' in s[-1]):
                    s[-1] = s[-1] + i
                else:
                    s.append(i)
            elif i in list_of_variables:
                s.append(str(list_of_variables[i]))
            else:
                s.append(i)
        for i in range(len(s)):
            if '/' in s[i] and len(s[i]) > 1:
                s[i] = fraction_in(s[i])
            elif '.' in s[i] and len(s[i]) > 1:
                s[i] = fraction_in(s[i])
            elif s[i].isdigit():
                s[i] = fraction_in(s[i])
        s = add_multiple_operators(s)
        for i in s:
            print(i, end=' ')
        print("")
        for i in s:
            if isinstance(i, list):
                stack_num.append(i)
                continue
            if i == '(':
                stack_operator.append(i)
            elif i == ')':
                while stack_operator[-1] != '(':
                    num2 = stack_num.pop()
                    num1 = stack_num.pop()
                    operator = stack_operator.pop()
                    stack_num.append(calculate_fraction(operator, num1, num2))
                stack_operator.pop()
            elif i in ['+', '-', '*', '/', '^']:
                while stack_operator and stack_operator[-1] != '(' and priority(stack_operator[-1], i) > 0:
                    num2 = stack_num.pop()
                    num1 = stack_num.pop()
                    operator = stack_operator.pop()
                    stack_num.append(calculate_fraction(operator, num1, num2))
                stack_operator.append(i)
            else:
                stack_num.append(i)
        while stack_operator:
            num2 = stack_num.pop()
            num1 = stack_num.pop()
            operator = stack_operator.pop()
            stack_num.append(calculate_fraction(operator, num1, num2))
        result = simplify_fraction(stack_num[0])
        return fraction_show(result[0], result[1])
    else:# 实数（小数）模式
        for i in text:
            if i.isdigit() or i == '.':
                if s and (s[-1].isdigit() or '.' in s[-1]):
                    s[-1] = s[-1] + i
                else:
                    s.append(i)
            elif i in list_of_variables:
                s.append(str(list_of_variables[i]))
            else:
                s.append(i)
        for i in range(len(s)):
            if '/' in s[i] and len(s[i]) > 1:
                s[i] = realness_in(s[i])
            elif '.' in s[i] and len(s[i]) > 1:
                s[i] = realness_in(s[i])
            elif s[i].isdigit():
                s[i] = realness_in(s[i])
        s = add_multiple_operators(s)
        for i in s:
            if i == '(':
                stack_operator.append(i)
            elif i == ')':
                while stack_operator[-1] != '(':
                    num2 = stack_num.pop()
                    num1 = stack_num.pop()
                    operator = stack_operator.pop()
                    stack_num.append(calculate_realness(operator, num1, num2))
                stack_operator.pop()
            elif i in ['+', '-', '*', '/', '^']:
                while stack_operator and stack_operator[-1] != '(' and priority(stack_operator[-1], i) > 0:
                    num2 = stack_num.pop()
                    num1 = stack_num.pop()
                    operator = stack_operator.pop()
                    stack_num.append(calculate_realness(operator, num1, num2))
                stack_operator.append(i)
            else:
                stack_num.append(i)
        while stack_operator:
            num2 = stack_num.pop()
            num1 = stack_num.pop()
            operator = stack_operator.pop()
            stack_num.append(calculate_realness(operator, num1, num2))
        result = stack_num[0]
        return result

# 测试数据
"""
equation = '2ab'

list_variables = 'a=2 b=3'

print(equation_calculater(equation, list_variables, fraction_enable=True))
print(equation_calculater(equation, list_variables, fraction_enable=False))"""