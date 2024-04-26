
anos = 0
a = 80000
taxa = a * 0.03
b = 200000
taxa1 = b * 0.015

while a < b:
    a += a * taxa
    b += b * taxa1
    anos += 1

print(f"serão necessarios {anos} anos")