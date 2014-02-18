# Pt cei ce stiu C: Python nu are pointeri sau array-uri (zone continue de memorie)
# Pt cei ce stiu structuri de date: lista e un array redimensionabil prin realocare,
# dictionarul e o tabela de dispersie

# Python are 2 glorioase tipuri de date ce nu le vezi in C
# lista

tada = [2, 3, 4]
print tada
# operatii cu liste
# indexarea
print tada[0]
print tada[1]
print len(tada)
print tada + [66, 77]  # face o noua lista lipind 2
print tada  # nu e schimbat

# listele nu tre sa fie omogene
lis = [2, 'ana', [44, 55]]

# listele sunt obiecte
# si au metode. Astea is ca niste functii normale (len, str) numai ca sunt invocate cu punct
# si se refera automat la obiectul curent
# ex:

tada.append(23)  # adauga 23 in lista tada
print tada
z = tada.pop()  # salta elementul de la capatul listei
print tada

# functia range face o lista de numere crescatoare
tada = range(3)  # de la 0 la 3
print tada == [0, 1, 2]  # e adevarat
print range(2, 8, 2)  # incepe cu 2 opreste la 8 sari din 2 in 2

# instructiunea for repeta blocul sau pentru fiecare element dintr-o lista
for a in [2, 6, 9, 6]:  # pentru orice a in lista executa
    print a*3 # il putem folosi pe a aici

# for-ul clasic din C poate fi reprodus cu range
# de ex echiv cu for(int i =0 ;i<3;i++){cout << i;}
for a in range(3):  # range e [0,1,2]
    print a

