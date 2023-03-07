#!/usr/bin/python3

for xters in range(97, 123):
    if xters == 101 or xters == 113:
        continue
    print("{:c}".format(xters), end='')
