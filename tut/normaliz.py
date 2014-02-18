# Un programel ce normalizeaza un vector de 2 elemente
# Daca elementele sunt x = 1 si y = 3
# Vectorul normalizat va avea componentele impartite la lungimea vectorului

# Dam nume unor valori
x = 1
y = 2
# x si y se mai numesc variabile deoarece le putem schimba valoarea fara a da nume noi
y = y + 1   # y devine rezultatul adunarii lui y cu 1

print 'x e '
print x
print 'y e '
print y
# x**2 e x la puterea 2
print 'x**2 e :'
print x**2
# merg si puteri reale. De ex radical din x:
print 'x**0.5 e :'
print x**0.5
# introducem un nou nume pentru lungimea vectorului de  componente x, y
lungime = (x**2 + y**2)**0.5  # parantezele grupeaza operatiile
print 'lungime '
print lungime

x_normalizat = x / lungime
y_normalizat = y / lungime

print 'x si y normalizati'
print x_normalizat
print y_normalizat