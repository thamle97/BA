from math import sqrt

print("Nhập một số n:")
n = int(input())

assert n > 0
square = []
for i in range(1, n + 1):
    result = int(sqrt(i))
    if result ** 2 == i:
        square.append(i)

for i in square:
    print(i, end=" ")
