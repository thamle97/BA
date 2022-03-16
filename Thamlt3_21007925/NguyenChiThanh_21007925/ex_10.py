from itertools import combinations

print("Nhập 5 số nguyên a, b, c, d, e")
print("Nhập a:")
a = int(input())
print("Nhập b:")
b = int(input())
print("Nhập c:")
c = int(input())
print("Nhập d:")
d = int(input())
print("Nhập e:")
e = int(input())

assert a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0

solutions = []
for x, y, z in combinations(range(max(d, e) + 1), 3):
    if (x + y + z == e and a * x + b * y + c * z == d):
        solutions.append((x, y, z))

if len(solutions) == 0:
    print("Hệ phương trình trên vô nghiệm")
else:
    print("Các nghiệm của hệ phương trình trên là:")
    for x, y, z in solutions:
        print(x, y, z)
