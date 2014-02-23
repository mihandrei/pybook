# =======
# Siruri
# Rostul lor e sa tina text
# =======

# Text in alfabetul ASCII
# Pentru text in romana cu diacritice situatia se complica semnificativ
# ASCII e cam ce gasesti pe tastatura americana
# abc..z ABC..Z 0..9 +-*.,'";:?[]{}/\|!@#$%^&*()=~`

# Sirurile sunt imutabile ca si numerele: odata create nu pot fi modificate
# Orice operatie cu siruri va creea noi valori
# Sirurile au dimensiune arbitrara

# -------
# notatie
# -------

a = 'ana are mere si o dublu ghilimea " '
b = "ana are mere si o ghilimea ' "
# daca sirul contine un " atunci folosesti notatia 1 daca un ' notatia 2

# sir multilinie - delimitat de 3 ghilimele
c = """ un sir ce se
intinde pe mai multe linii
lalata
"""

# escape sequences
# ----------------
# ce te faci daca le contine pe ambele ghilimele?
# pui un \ in fata ghilimelei
c = "io-s un sir nesimtit am si \" dar si ' "
# poti pune \ si unde nu-i musai
"lala \" ' lulu" == 'lala " \' lulu' == 'lala \" \' lulu'
# bine da daca vreau un \ in sir? Atunci il dublezi
sir_cu_backslash = "am un \\ no!"
print sir_cu_backslash
# notatie raw: are un r in fata si ignora escapurile adica
r"a\t" == "a\\t"


# contructie
# ----------
# prin notatie literara descrisa mai sus
# din operatii cu siruri
# via functia str
s = str(23)
"23" == s

# operatii cu siruri
# ------------------

# + lipeste 2 siruri
s = "ana"
p = s + " are"  # "ana" nu e modificat fiind imutabil o noua valoare se creeaza

# * repeta un sir. Un operand tre sa fie int
p = "tic " * 3

# indexarea e identica cu listele
s = "anax"
s[1] == "n"
s[-1] == "x"
# taieturi
s = "petre"
s[1:3] == "et"

# operatii booleene
# -----------------

'ana' == "ana"
'ana' != "mere"
"an" in "bani"  # an inclus in bani . True
"lala" not in "a"  # neinclus

# comparatiile considera ordinea in alfabet.
# se comporta normal
"a" < "z"
# daca siru e mai lung compara primu caracter apoi al doilea etc
"ab" < "az"
# comparatia cu numere e neintuitiva. Nu o folosi
"3" > 3  # in mod enervant nu arunca eroare ci da True

# pozitia in alfabet-ul ASCII a unei litere e data de functia ord
97 == ord("a")
98 == ord("b")
# functia chr ia un index in alfabet si intoarce litera aferante
"a" == chr(97)

# functii cu siruri
# -----------------
len("ana") == 3  # lungime

# metodele sirurilor
# ------------------

# un sir e un obiect. Urmatoarele metode is des folosite

s = "ana are mere"
s.endswith("mere") == True  # daca se sfarseste cu sirul
s.startswith("ana") # incepe cu
s.count("a")  # de cate ori e inclus "a" in s
s.find("are") == 4  # la ce index se gaseste prima data subsirul ana. -1 daca ana not in s
"AnA".lower() == "ana"
s.split() == ["ana", "are", "mere"]  # taie sirul la spatii
"1#2#3#".split("#") == ["1","2",""]
"__".join(["a", "6", "mere"]) == "a__6__mere"  # lipeste siruri dintr-o lista
s.strip("    ana   ") == "ana"  # taie spatii de la capete
# si altele multe

# performanta
# -----------

# indexarea e O(1)
# copierea/creerea unui sir e O(len(s))
# fiind imutabile operatiile creaza siruri noi
# astfel + * s.lower() etc sunt O(n)
