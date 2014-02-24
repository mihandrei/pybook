# =====
# Tuple
# Rostul lor e sa fie folosite pentru decompozitie si ca si chei in dictionare
# =====

# O versiune imutabila de lista
#   immutabil
#   linear
#   heterogen
# Au dimensiune arbitrara si fixa

# -------
# notatie
# -------
simpla = (2, 3, 'a')
implicita = 2, 3, 'a'

# tuplu de lungime 1 e un caz special in notatie
t = (2)  # se interpreteaza aritmetic si e 2
t == 2
# notatia implicita clar ca nu mere
t = 2
# sintaxa speciala pt 1-tuplu
t = (2,)

# Apropo regula in python: poti pune delimitatori in plus si nu-i bai
[1, 2] == [1, 2,]

# constructie
# ----------

# prin notatie literara descrisa mai sus
# via functia tuple din orice secventa
s = tuple("ana")
s == ('a', 'n', 'a')
s = tuple([3, 4])
s == (3, 4)

# Deconstructia e operatia fundamentala
# -------------------------------------
t = (3, 4)
(a, b) = t   # sintaxa speciala in limbaj pentru deconstructie : tuplu simbolic = tuplu
a, b = t  # acelasi lucru
a == 3

# Deconstructia e mecanismul prin care in Py poti intoarce 'mai multe valori' dintr-o functie
# a, b = functie()
# DEconstructia merge cu mai multe valori
a, b, c = 1, 4, 2
# Deconstructia merge si cu alte secvente
a, b = [3, 5]
a, b = "AT"

# indexare
# --------
s = (3, 5, 6)
s[0] == 3 and s[1] == 5
# ca la liste numai nu poti schima
# s[0] = 33 va arunca o eroare

# taieturi :
# ca la liste exceptie modificarile
# rar folosite

# + lipeste 2 tuple, rar folosit
s = (1, 4) + (3,)
s == (1, 4, 3)

# grija la notatia implicita. nu o folosi cu alti operatori ca tinde sa confuzeze
1, 4 + 3, 1 == (1, 7, 1)  # ???
(1, 4) + (3, 1) == (1, 4, 3, 1)  # normal

# * repeta un tuplu ca la liste. nu am folosit veci
s = (0, 1) * 3

# operatii booleene
# -----------------
(1, 2) == (1, 2)
2 in (1, 2)

# comparatiile ca la liste
# functii cu tuple:
len((1, 3, 4)) == 3

# metode : nimic interesant
