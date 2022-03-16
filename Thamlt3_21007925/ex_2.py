from  math import sqrt

print("Nhập ba số a, b, c")
print("Nhập a:")
a = float(input())
print("Nhập b:")
b = float(input())
print("Nhập c")
c = float(input())

if (a + b > c and a + c > b and b + c > a):
    print("Ba cạnh trên lập thành một tam giác")
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Chu vi của tam giác là: {}, diện tích của tam giác là: {}".format(2 * p, s))
else:
    print("Ba số trên không tạo thành một tam giác")
    