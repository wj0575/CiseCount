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
    result = []
    for index, i in enumerate(text):
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

def make_list(variables):
    list = {}
    variables = variables.split(' ')
    for i in range(len(variables)):
        try:
            tmp = variables[i].split('=')
            list[tmp[0]] = int(tmp[1])
        finally:
            continue
    return list

def equation_calculater(text, variables, fraction_enable=False):
    list_of_variables = make_list(variables)
    text = text.replace(' ', '')
    text = text.replace('**', '^')
    s = []
    stack_operator = []
    stack_num = []
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
        return fraction(result[0], result[1])
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
equation = '2ab^c'

list_variables = 'a=2 b=3 c=2'

print(equation_calculater(equation, list_variables, fraction_enable=True))
print(equation_calculater(equation, list_variables, fraction_enable=False))"""