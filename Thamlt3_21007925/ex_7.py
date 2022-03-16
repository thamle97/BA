

def cos(x, e):
    result = 0
    p = 1
    i = 1
    while True:
        result += p
        new_p = p * (-1) * x ** 2 / ((2*i - 1) * 2*i)
        if abs(abs(new_p) - abs(p)) < e:
            break
        p = new_p
    
    return result


print("Nhập 2 số, số thực x và số thực e:")
print("Nhập số thực x:")
x = float(input())
print("Nhập số thực e:")
e = float(input())

print("Giá trị của cos({}) là: {}".format(x, cos(x, e)))