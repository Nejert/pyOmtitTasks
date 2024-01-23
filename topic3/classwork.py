import math
radius : str = input("Введите радиус: ") 
pi : float = math.pi
dlina_okr : float  = 2 * pi * float(radius)
print('Длина окружности с радиусом', radius, 'равна', dlina_okr)

print(int())
print(float())
print(bool())
print(str())

print("mark"<"mary")
print("mark">"mary")
print("mark"=="mary")

print(ord('a'))
print(chr(97))
print(chr(1072))

for i in range(12):
    print(chr(i+9800), end=" ")

n = int(input())
if n > 0:
    print("положительное")
else:
    if n < 0:
        print("отрицательное")
    else:
        print("ноль")