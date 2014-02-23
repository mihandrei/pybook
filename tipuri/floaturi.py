# ===================
# float - numere reale
# Rostul lor: Pentru a reprezenta valoarea unor masuratori. Pentru algoritmi numerici.
# ====================

# Reprezinta numere cu virgula
p = 3.14

# NU au precizie arbitrara ca int
# Sunt mai complicate. Au comportamente specifice si diferite de numerele reale.
# De obicei se comporta ok dar pentru numere foarte mari mici sau precise ...

# ex: exista numere cu virgula ce nu pot fi reprezentate (precizie prea mare)
0.5555555555555555501 == 0.5555555555555555599  # in mod ciudat e True
# numere prea mari pt float
10.0 ** 1000  # va arunca o eroare

# Constructie
# -----------
# via notatie literara
p = 3.14
# literara stiintifica
p = 3.14e5
3.14e5 == 314000
# via notatie ametita de cap
p = .1
.1 == 0.1
# prin operatii cu floaturi
p = 3.12 + 0.0216
# conversii via functia float
p = float('3.1416') # din sir
p = float(3)  # din intreg

# operatii
# --------

# + - * ca la int dar pot sa dea erori numerice
r = 3.14 + 1.3 * 3.0

# grija la impartire !
# --------------------

1.5 == 3.0 / 2 == 3 / 2.0
#insa
1 == 3 / 2

# daca intr-o operatie e intre un intreg si un float, intregu se converteste
# astfel 3.0/2 devine 3.0/2.0
# dar nu tine pentru expresii intregi:
0.5 == 2/3 + 1.0/2  # devine 0 + 0.5 , apoi plus-ul face conversia 0.0 + 0.5
# capcana deasa
b = 1  # presupunem ca b si c vin de departe ca altfel se rezolva cu un .0 dupa numere
c = 2
rap = b / c  # daca vrei ca impartirea sa dea cu virgula nu-i bine daca b si c is int
rap = float(b) / c  # convertesc explicit unu din astia in float

# putere
# ca si pentru int
p = 2.0 ** 2.0
p = 2.0 ** -2.0
# dar si
radical2 = 2.0 ** 0.5
# sau arbitrar
pi_la_pi_cu_bucurie = 3.1415 ** 3.1416

# contractii ca la int
p += 3.0  # etc

# comparatiile la fel ca la int
4.0 < 4.1 # etc

# min max abs ca la int

# egalitatea tot la fel
3.0 == 3.0
# grija mare la == cu floaturi !
# datorita erorilor numerice de multe ori nu vrei sa compari exact
2.999999999999999999 != 3.0  # dar foarte probabil ai vrea sa le consideri egale
# Depinde de caz dar de obicei se face cam asa
# if abs(p - 3.0) < precizie:
#     le consider egale

# functii cu floaturi
# -------------------

# Module pe scurt: sunt fisiere python.
# Poti de ex sa zici
# import intregi
# si apoi sa folosesti nume definite in fisierul intregi.py

import math  # importa modul math in care sunt functii de mate
math.pi > 3.0
math.sin(math.pi) < 0.0000000001   # apropo de == la floaturi asta nu e 0
# is multe functii in math toate cu floatu-uri
math.floor(3.14) == 3.0  # parte intreaga (spre deosebire de int(3.14) intoarce float)
# etc
