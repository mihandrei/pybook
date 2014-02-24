# ====
# Liste
# Rostul lor: container de date oarecare
# =====

# Un tip de date
#   mutabil : o valoare poate fi schimbata
#   linear  : e o insiruire
#   heterogen : spre deosebire de siruri ce is facute din caractere
#               o lista poate contine orice
# Au dimensiune arbitrara si variabila

# -------
# notatie
# -------
simpla = [2, 3, 4]
heterogena = ['ana', 3, [2, 1]]

# contructie
# ----------
# prin notatie literara descrisa mai sus
# via functia list din orice secventa
s = list("ana")
s == ['a', 'n', 'a']
# progresii artitmetice via range
s = range(3)
s == [0, 1, 2]
s = range(5, 2, -1)
s == [5, 4, 3]
# split
"ana are".split() == ["ana are"]
# etc

# operatii cu liste
# ------------------

# indexarea e operatia fundamentala. Cost O(1)
# --------------------------------------------

s = [3, 5, 6]
s[0] == 3 and s[1] == 5
# indexarea cu un negativ e interpretata ca numarare de la coada
s[-1] == 6
s[-2] == 5

# listele is mutabile
# valoarea de la un index poate fi schimbata
s[0] = 0
s[-1] = 0
s == [0, 5, 0]

# atentie asta inseamna ca:
s = [1, 2]
t = s
s[0] = 3  # il modifica si pe t, caci t si s sunt 2 nume pt aceeasi lista
t == [3, 2]

# valoarea la un index poate fi stearsa cu operatorul del
s = [4, 2, 1]
del s[1]
s == [4, 1]
# del e o(n)

# taieturi : s[a:b] ce e intre indecsi a inclusiv si b exclusiv
# -------------------------------------------------------------
s = [3, 6, 'z', 1]
s[1:3] == [6, 'z']
s[2:] == ['z', 1]  # de la 2 pana la capat
s[:2] == [3, 6]  # de la inceput pana la 2 exclisiv
s[:-1] == [3, 6, 'z']  # de la inceput pana la ultimul exclusiv
# motivul intervalului inchis stanga deschis dreapta se repeta peste tot. Aminteste-ti range

# Taieturile creaza copii:
s = [1, 2, 3]
t = s[:-1]  # t e o noua lista
t == [2, 3]
t[0] = 0  # fiindca t e o noua valoare schimbarea lui nu afecteaza pe s
s[0] == 1

# scrierea in taietura
s = [1, 2, 3]
# inlocuieste in lista s zona taiata cu o noua lista
s[:-1] = [8, 9, 10]
s == [8, 9, 10, 3]

# stergerea taieturii
del s[2:3]

# taieturi cu pas
s = [0, 1, 2, 3, 4]
s[::2] == [0, 2, 4]
s[::-1] == [4, 3, 2, 1, 0]

# + lipeste 2 liste
s = [1, 4] + [3] + [55, 44]
s == [1, 4, 3, 55, 44]

# * repeta o lista
s = [0] * 3
s == [0, 0, 0]

# grija la repetitia unei valori mutabile!
s = [[0]] * 2
s == [[0], [0]] # pare ok
# insa lista interioara e un obiect mutabil repetat
s[0][0] = 1
s == [[1], [1]]  # no tulai ca s-o schimbat si s[1][0]!

# operatii booleene
# -----------------

[1, 2] == [1, 2]
[1, 2] != [2, 1]
2 in [1, 2]  # inclus o(n)

# comparatiile compara element cu element de la stanga la dreapta
[1, 2, 3] < [1, 4] < [1, 6, 0]

# functii cu liste
# -----------------
len([1, 3, 4]) == 3  # lungime
z = zip([4, 5, 6], ['a', 't', 'u'])  # fermoar: lipeste primele valoare din lista 1 cu prima din lista 2
z == [(4, 'a'), (5, 't'), (6, 'u')]  # (4,a) e un tuplu. vezi tuple.py

# metode
# ------
s = [2, 4]
s.append(6)  # adauga la dreapta O(1)
s == [2, 4, 6]
6 == s.pop()  # scoate de la dreapta O(1)
s == [2, 4]
s.reverse()
s == [4, 2]
s.extend([33, 44]) # extinde cu alta lista
s == [4, 2, 33, 44]
s.insert(1, 'a')
s == [4, 'a', 33, 44]
s.sort()
# etc

# list comprehensions
# -------------------
# transforma o lista in alta evaluind o expresie

s = [2, 3, 1]
t = [x*2 for x in s]  # syntaxa [expresie for element in lista]
t == [4, 6, 2]

# creaza copii
t[0] = 0
s[0] == 2

# pot si filtra o lista cu if
t = [x for x in s if x % 2 == 1]  # sintaxa [expresie for element in lista if conditie]
t == [3, 1]

# combinate
dublu_imparelor = [x*2 for x in s if x % 2 == 1]  # un pic dubios de lung

# Se folosesc pentru expresii SCURTE pentru a inlocui
# 2 foarte dese tipuri de for-uri
# Expresia de mai sus e perfect echivalenta cu urmatorul bloc
dublu_imparelor = []
for x in s:
    if x % 2 == 1:
        dublu_imparelor.append(x * 2)

# List comprehensions se folosesc pentru ca standardizeaza cazul comun
# cand vezi un comprehension stii ca e o mapare sau filtrare simpla
# Insa NU tre folosite daca is lungi: prefera un for