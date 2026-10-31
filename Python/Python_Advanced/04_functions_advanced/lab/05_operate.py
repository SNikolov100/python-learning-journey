from functools import reduce

def sum_num(*args):
    return sum(args)

# def sub_num(*args):
#     return reduce(lambda x, y: x - y, args)
#
# def multi_num(*args):
#     return reduce(lambda x, y: x*y, args)

def div_num(*args):
    if 0 not in args:
        return reduce(lambda x, y: x/y, args)
    return "Zero divide"

operator_action = {
    "+": sum_num,
    "-": lambda *args: reduce(lambda x, y: x-y, args),
    "*": lambda *args: reduce(lambda x, y: x*y, args),
    "/": div_num
}

def operate(operator, *args):
    return operator_action[operator](*args)




print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))