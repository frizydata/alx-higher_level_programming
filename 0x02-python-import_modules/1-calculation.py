#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div
a = 10
b = 5

adding = add(a, b)
subtracting = sub(a, b)
multiplying = mul(a, b)
dividing = div(a, b)

print("{} + {} = {}".format(a, b, adding))
print("{} - {} = {}".format(a, b, subtracting))
print("{} * {} = {}".format(a, b, multiplying))
print("{} / {} = {}".format(a, b, dividing))
