c = input().split()
s = int(c[0]) ** 2
a = 3.14 * int(c[1]) ** 2
if s > a:
    print("SQUARE")
else:
    print("CIRCLE")