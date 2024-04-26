'''
anos = 0
a = 80000
taxa = 0.03
b = 200000
taxa1 = 0.015

for i in range(a, b):
    a += a * taxa
    b += b * taxa1
    anos += 1
    if a >= b:
        break

print(f"serão necessarios {anos}")
'''
anos = 0
a = 80000
taxa = 0.03
b = 200000
taxa1 = 0.015

while (a < b):
    a += a * taxa
    b += b * taxa1
    anos += 1
    if a >= b:
        break
print(anos)