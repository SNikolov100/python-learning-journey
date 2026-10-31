def age_assignment(*args,**kwargs):
    my_dict = {}
    my_result = []
    for name in args:
        for first_letter, age in kwargs.items():
            if name[0] == first_letter:
                if name in my_dict:
                    my_dict[name] = int
                my_dict[name] = age
    sorted_list = sorted(my_dict.items(), key=lambda x: x[0])
    for data in sorted_list:
        my_result.append(f"{data[0]} is {data[1]} years old.")
    return "\n".join(my_result)


print(age_assignment("Peter", "George", G=26, P=19))
print("================================")
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))