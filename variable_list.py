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
    if not fraction_enable:
        if 'e' not in list:
            list['e'] = 2.71828
        if 'π' not in list:
            list['pi'] = 3.14159
        if 'g' not in list:
            list['g'] = 9.80665
        if 'c' not in list:
            list['c'] = 299792458
        if 'h' not in list:
            list['h'] = 6.626e-34
    return list
