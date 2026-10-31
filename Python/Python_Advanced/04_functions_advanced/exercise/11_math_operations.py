def math_operations(*args, **kwargs):
    for inx, data in enumerate(args):
        command = inx % 4
        data = float(data)
        if command == 0:
            kwargs["a"] += data
        elif command == 1:
            kwargs["s"] -= data
        elif command == 2 and data != 0:
            kwargs["d"] /= data
        elif command == 3:
            kwargs["m"] *= data
    sorted_result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    my_result = []
    for data, value in sorted_result:
        my_result.append(f"{data}: {value:.1f}")
    return "\n".join(my_result)



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print("====================================")
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print("======================================")
print(math_operations(6.0, a=0, s=0, d=5, m=0))