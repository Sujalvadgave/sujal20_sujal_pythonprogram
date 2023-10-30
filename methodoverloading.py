class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()

result1 = calc.add(5, 10)
result2 = calc.add(5, 10, 15)

print("Result with two arguments:", result1)
print("Result with three arguments:", result2)
