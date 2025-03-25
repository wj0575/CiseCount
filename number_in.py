from fraction import *

def fraction_in(x):
    if '/' in x:
        x = x.split('/')
        return [int(x[0]), int(x[1])]
    if '.' in x:
        x = str(x)
        x = x.split('.')
        return simplify_fraction([int(x[0])*10**len(x[1])+int(x[1]), 10**len(x[1])])
    return [int(x), 1]

def realness_in(x):
    if '/' in x:
        x = x.split('/')
        return int(x[0])/int(x[1])
    if '.' in x:
        return float(x)
    return int(x)

