n = int(input("enter the umber of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))