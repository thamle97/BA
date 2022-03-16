print("Nhập số nguyên dương n:")
n = int(input())

assert n > 0
if n % 2 == 0:
    result = 1
    for i in range(2, n + 1, 2):
        result *= i
    print("n!! = {}".format(result))
else:
    result = 1
    for i in range(1, n + 1, 2):
        result *= i
    print("n!! = {}".format(result))
    