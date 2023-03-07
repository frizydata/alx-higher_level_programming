mport random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1


if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5"
            .format(number, lastDigit))
elif last_digit < 6:
    print("Last digit of {} is {} and is less than 6 and not 0"
            .format(number, lastDigit))
else:
    print("Last digit of {} is 0 and is 0".format(number))
