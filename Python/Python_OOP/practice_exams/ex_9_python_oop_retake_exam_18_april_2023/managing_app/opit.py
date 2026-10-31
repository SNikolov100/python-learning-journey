a= [1, 2, 3, 4]
if any(True for i in a if i == 5):
    print("ok")
else:
    print("no")