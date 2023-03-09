#!/usr/bin/python3
if __name__ == "__main__":
    import sys

count_list = len(sys.argv) - 1
if count_list == 0:
    print("0 arguments.")
elif count_list == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count_list))
for i in range(count_list):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
