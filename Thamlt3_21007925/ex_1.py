from math import sqrt

print("Nhập a:")
a = float(input())
print("Nhập b:")
b = float(input())
print("Nhập c")
c = float(input())

delta = b**2 - 4 * a * c

if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x = {}".format(-b / (2 * a)))
else:
    print("Phương trình có hai nghiệm phân biệt là x1 = {}, x2 = {}".format((-b + sqrt(delta))/(2 * a), (-b - sqrt(delta))/(2 * a)))