# =======
# Intregi
# Rostul lor: sa numere chestii
# =======

# notatie
# -------

a = 8
# spre deosebire de alte limbaje intregii in python au precizie arbitrara
b = 1234567898765432112233456
# b e prea mare pentru un int in C sau java
# intregii sunt cu semn
c = -234

# contructie
# ----------
# prin notatie literara
a = 12
# din operatii cu intregi
a = a - 2
# conversie via functia int
a = int(3.14)  # dintr-un float (detalii mai jos)
a == 3
# dintr-un sir
b = int('23')
# baza optionala
1323154 == int('CAFEA', 18) == int('101000011000010010010', 2)

# operatii cu intregi
# -------------------

# + - * se comporta ca in mate
r = 2 + 4 - 6 * 3
# fiindca au precizie arbitrara rezultatele sunt intodeauna corecte
# nu se dau peste cap
r_urias = 5000000000 * 40000000

# - poate fi unar
r_minus = -r
# impartirea a doi intregi e tot un intreg
1 == 3/2

# impartirea la zero arunca o eroare
r0 = 3/0

# restul impartirii la un numar
rest = 3 % 2
rest == 1

# ridicare la putere
trei_patrat = 3 ** 2
tri_patrat_inv = 3 ** -2
# contractii
r += 2  # r = r + 2
r -= 2
r *= 2
r /= 5
r %= 2

# operatii booleene

3 == 4
3 != 4
3 < 4
3 <= 4
3 >= 4

# in python astea pot fi inlantuite
1 < 3 <= 3 < 4
3 == c == 4

# operatii binare.
# Aici doar ca sa stii sa NU le folosesti
3 & 2 | 4
if 3 < 2 & 4 < 5 | 5 == 3:
    print 'nu face ce crezi. foloseste and si or'

# functii ce merg cu intregi
# modul
abs(-3) == 3
# min max
min(2, 3, 4) == 2
