print("Nhập 2 số x, y")
print("Nhập x:")
x = float(input())
print("Nhập y:")
y = float(input())

if (x == 0 and y == 0):
    print("Điểm này là gốc tọa độ")
elif (x == 0):
    print("Điểm này thuộc trục tung")
elif (y == 0):
    print("Điểm này thuộc trục hoành")
elif (x > 0 and y > 0):
    print("Điểm này thuộc góc phần tư thứ nhất")
elif (x > 0 and y < 0):
    print("Điểm này thuộc cung phần tư thứ tư")
elif (x < 0 and y > 0):
    print("Điểm này thuộc cung phần tư thứ hai")
elif (x < 0 and y < 0):
    print("Điểm này thuộc cung phần tư thứ ba")
