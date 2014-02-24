# ======================================
# Dictionare
# Rostul lor: container de date oarecare
# ======================================

# asociaza unei valori imutabile o valoare arbitrara

# Un tip de date
#   mutabil : o valoare poate fi schimbata
#   neordonat  : spre deosebire de liste sau siruri NU exista o ordine a cheilor
#   heterogen : cheile pot fi orice imutabil, valorile orice
# Au dimensiune arbitrara si variabila

# -------
# notatie
# -------
d = {2: 3, "ana": 4}
e = {'ana': [2, 1]}  # la 'ana' ii corespunde lista

# Cheile tre sa fie imutabile
f = {[2, 3]: 4}  # o sa dea eroare

# contructie
# ----------
# prin notatie literara descrisa mai sus
# via functia dict din orice secventa de dublete
s = dict([(2, 3), ("ana", 3)])
s == {2: 3, "ana": 3}
# sau chestii convertibile la dublete. Cam confuzant
s = dict([(2, 3), [4, 5], "AZ"])
# sau daca cheile is nume permise in python via argumente numite la dict
# o sa vorbim la functii despre kwargs
s = dict(ana=3, petre=55)
s == {'ana': 3, 'petre': 55}

# obs : se intalneste des dict cu zip:
chei = [2, 4, 6]
valori = [22, 44, 66]
zip(chei, valori) == [[2, 22], [4, 44], [6, 66]]
d = dict(zip(chei, valori))
d == {2: 22, 4: 44, 6: 66}

# operatii cu dictionare
# ----------------------

# operatia fundamentala e citirea dupa cheie O(1)
# -----------------------------------------------
s == {2: 3, "ana": 4}
s[2] == 3
s["ana"] == 4
# daca cheia nu e arunca eroare
s["petre"]

# dict is mutabile
# valoarea de la o cheie poate fi schimbata
s["ana"] = 0
s == {2: 3, "ana": 0}

# atentie asta inseamna ca:
s = {1: 2}
t = s
s[0] = 3  # il modifica si pe t, caci t si s sunt 2 nume pt aceeasi valoare
t == {1: 3}

# o cheie poate fi stearsa cu del
s = {2: 3, "ana": 4}
del s[2]
s == {"ana": 4}

# o cheie noua se creaza tot cu =
s["petre"] = 66
s == {"ana": 4, "petre": 66}

# Iteratie
# --------
s = {2: 3, "ana": 4}
[2, "ana"] == s.keys()  # intoarce o lista cu cheile. Ordinea e arbitrara.
[3, 4] == s.values()  # valorile
[(2, 3), ("ana", 4)] == s.items()  # lista de tuple

# daca transformam un dict in lista obtinem s.keys
list(s) == [2, "ana"]
# daca iteram un dict iteram keys:
for k in s:
    print k
# va printa 2, "ana"
# pentru a itera cheie valoare combinam s.items cu decostructie de tuple
for k, v in s.items():
    print k, v + 1
# va printa 2 4   "ana" 5
# OBS: ordinea din s.keys nu e cea in care am inserat valorile si in general nu are sens
# se poate schimba arbitrar la modificarea dictului
s = {}  # dict gol
s[99] = 1
s[1] = 4
[1, 99] == s.keys()  # exemplul asta pare sa indice ca keys e sortat, dar nu-i
# obs tehnica: dict e o tabela de dispersie, ordinea cheilor e data de hash. hash-urile sunt prin natura lor complexe


# operatii booleene
# -----------------
{1: 3, 4: 5} == {4: 5, 1: 3}  # ordinea nu conteaza in dicturi
2 in {2: 4}  # inclus in CHEI !
4 not in {2: 4}

# comapratiile nu prea au sens in practica

# functii cu dicts
# -----------------
#len da lungimea

# metode
# ------
s = {1: 4}
s.get(1) == 4  # intoarce valoarea daca e alfel
s.get(9) == None  # None
s.get(9, 'd') == 'd'  # sau o valoare default

s.update({6: 4})  # comaseaza cele 2 dict-uri
s == {6: 4, 1: 4}
