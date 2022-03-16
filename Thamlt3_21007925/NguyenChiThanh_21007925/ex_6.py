def sin(x, n):
    result = 0
    p = x
    for i in range(1, n + 1):
        result += p
        p *= (-1) * x ** 2 / (2*i * (2*i + 1))
    
    return result

print("Nhập 2 số, số thực x và số nguyên n:")
print("Nhập số thực x:")
x = float(input())
print("Nhập số nguyên n:")
n = int(input())

assert n > 0
print("Giá trị của sin({}) là: {}".format(x, sin(x, n)))
