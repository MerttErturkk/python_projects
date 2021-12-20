sayilar = [1,2,3,4,5]

#kareler = []
#for sayi in sayilar:
#   kareler.append(sayi*sayi)
#print(kareler)


squares = list(map(lambda sayi: sayi**2,sayilar))
print(squares)

