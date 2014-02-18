# Acesta line e un comentariu. A inceput cu #. Menirea lui e sa fie citit
# de oameni si ignorat de masina. Aici se refugiaza limba oamenilor
# In afara comentariilor e limba masinii:
print 'Masina vorbeste'
# Sunt multe limbi a masinii.
# Limba de aici e python.
print 'Sunt python'
# Ea i se adreseaza Interpretorului. El pricepe python.
# Ca un actor robot Interpretorul citeste povestea asta scrisa in python
# si interpreteaza scenariul
# Hai sa-i zicem sa salute entuziast lumea
print 'Salutare lume!'
# Daca dai dublu click pe acest fisier windows ar trebui sa-i
# spuna Interpretorului sa-i dea drumu  la treaba

# Interpretorul citeste si executa comenzile din acest fisier
# in ordinea in care au fost scrise
print "intai se executa primul print"
print "apoi acest al doilea"

# Romana are parti de vorbire: substantive adjective ...
# Python are tipuri de date :

# siruri
print 'Sunt un sir'
# numere
print 2831
# si altele

# print e un verb in python. O comanda. Verbele poruncesc interpretorului sa
# faca o actiune.

# Ca exemplu verbe folosite des in propozitii cu numere
print 22 + 33 - 4 * 5
print 2/3
print 3 < 5
# Verbe folosite cu siruri
print 'Acest sir se va lipi ' + 'de acesta'
print 'a'*3

# Unele propozitii nu au sens. Decomenteaza mai jos si Interpretorul se va
# plange de o eroare de sintaxa (ortografie).
# print 3 ++ 5
# Alte propozitii au o forma corecta da tot nu au sens
# print 'ana are mere' / 24

# Functiile sunt si ele niste verbe.
# Arata cam asa
# nume_functie(argument1, argument2)
# Ex len - lungimea a ceva
print len('ana are mere')

# Ex transforma un sir intr-un numar.
# Al doilea argument e baza in care e scris numarul
print int('101', 2)
# sau baza 16
print int('B', 16)

# Cateva verbe sunt oarecum universale; au sens cu orice tip de date
print 2 == 2
print 'ana' == 'ana'
print str(432)  # transforma ceva intr-un sir

# Dupa cum ai observat verbele au numele lor
# Si noi putem numi valorile unui tip de date
un_sir_numit = 'Cineva m-a boteat!'
# Putem acum folosi numele oriunde am fi folosit valoarea
print un_sir_numit + ' Is Cool'

#Ce inseamna asta? :
print un_sir_numit + str(2 + 4)

# experimenteaza:
print un_sir_numit * 2

# Un tip de date important in python e bool-eanul
# Poate avea doar 2 valori True (adevarat) sau False
print True
# Unele expresii au un rezultat boolean
# Ex :
# e adevarat ca 2 e intre 1 si 3
print 1 < 2 < 3
# e fals ca lungimea sirului 'ana' e 5
print len('ana') == 5

