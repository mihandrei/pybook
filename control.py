# In exemplele de pana acum Interpretorul executa fiecare linie
# Insa de multe ori e nevoie sa executam comenzi numai in anumite conditii
# sau sa executam ceva inmod repetat

# if executa o ramura sau alta in functie de valoarea unei expresii booleene
# daca lungimea sirului ana e 3 atunci .. altfel ...

if len('ana') == 3:
    print 'se executa daca e adevarat'
else:
    print 'se executa daca e fals'

# observa ca
# * expresia din if nu trebuie sa fie in paranteze
# * dupa expresie e un : dar si dupa else
# * ramurile expresiei sunt indentate cu 4 spatii (adica is mai la dreapta decat if -ul)

# Indentarea e esentiala in Python.
# Urmatorul cod e invalid gramatical in python
# if 2 < 3:
# print 3
# else:
# print 33
# Indentarea indica scopul intr-un mod similar cu {} din C++
# De ex

if 2 < 3:
    print 'gugu: se executa daca e True'
    print 'gaga: fac parte din acelasi bloc cu gugu'
else:
    print 'fsss: i fals'

# If poate fi ierarhic si indentarea indica ce comanda de care if se tine
if 2 < 3:
    print 'A'
    if 2**2 == 4:
        print 'B'
    else:
        print 'non-B'
else:
    print 'non-A'
    print 'tot non-A'  # daca ar fi cu 4 spatii la stanga aliniat cu else atuni nu s-ar executa pe else
print 'o alta comanda ce nu tine de if-elsu de mai sus'

# Revenim la expresii booleene
# Sunt expresii ce se evalueaza la True sau False
# ex:
print 2 == 3
# pot fi combinate cu operatoiri logici
# negatie
print not 2 == 3
# si
print len('ana') == 3 and 44 < 55
# sau
print len('ana') == 44 or len('ana') == 3


if (len('ana') == 3 or len('baba') == 44) and 2 < 3:
    print 'ceva complicat e adevarat'

# While se isi executa blocul in mod repetat cat timp conditia lui e adevarata
# Sau s-a executatu un break

numar = 0

while numar < 5:
    print numar
    numar += 1  # += e tot una cu numar = numar + 1

print 'numar ' + str(numar)  # fa un sir din numar si lipeste-l de sirul 'numar '

# De obicei in while ceva variabila se schimba astfel incat coditia sa devina falsa
# Atlfel while se executa pentru totdeauna
# codu comentat de mai jos nu s-ar opri veci.
# while True:
#     print 'etern'

# din While mai poti scapa cu break
while True:
    numar -= 1
    if numar % 2 == 0:  # % restul impartirii la
        print 'amu e par'
        break  # intrerupe ciclul parinte
