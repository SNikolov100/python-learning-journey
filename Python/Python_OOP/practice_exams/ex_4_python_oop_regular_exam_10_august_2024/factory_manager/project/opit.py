def my_list(*args):
    a = args
    print(type(args))
    return args


print(my_list("1", "5", "we"))

