mport random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1

out_put = "Last digit of %d is %d and is" % (number, last_digit)

if last_digit == 0:
    print(out_put, "0")
elif last_digit > 5:
    print(out_put, "greater than 5")
else:
    print(out_put, "less than 6 and not 0")
