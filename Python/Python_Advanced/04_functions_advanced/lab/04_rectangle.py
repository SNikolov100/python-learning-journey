def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f"Enter valid values!"

    def area(l, w):
        return w*l

    def perimeter(l, w):
        return 2*w + 2*l

    return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"









print(rectangle(2, 10))
print("========================================")
print(rectangle('2', 10))


