from itertools import combinations

print("Nhập số nguyên n:")
n = int(input())

assert n > 0

triplets = []
for a, b, c in combinations(range(n + 1), 3):
    if (a ** 2 + b ** 2 == c ** 2 or a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2):
        triplets.append((a, b, c))

if len(triplets) == 0:
    print("Không có bộ 3 số nào lập thành bộ Pytago")
else:
    print("Các bộ 3 số a, b, c lập thành bộ Pytago là:")
    for a, b, c in triplets:
        print(a, b, c)
        