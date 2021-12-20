# -*- coding: utf-8 -*-

sehir = ["ankara","istanbul","izmir"]
my_iter = iter(sehir)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
try:
    print(next(my_iter))
except:
    print("liste bitti")

print("\n\n")

# alt kod aynı işi görür

for a in sehir:
    print(a)