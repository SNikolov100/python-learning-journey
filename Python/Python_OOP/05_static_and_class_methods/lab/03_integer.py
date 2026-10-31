roman_numerals = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000
                  }
class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, from_value):
        if not isinstance(from_value, float):
            return "value is not a float"
        return cls(int(from_value))

    @classmethod
    def from_roman(cls, value: str):
        int_value = 0
        for i in range(len(value)):
            if i + 1 < len(value) and roman_numerals[value[i]] < roman_numerals[value[i + 1]]:
                int_value -= roman_numerals[value[i]]
            else:
                int_value += roman_numerals[value[i]]
        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:
                return cls(int(value))
            except ValueError:
                pass
        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
