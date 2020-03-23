N = int(input()) #broj bridova
K = int(input()) #max broj čvora

susjedi = [[]for i in range(K+1)]

for i in range(N):
	a, b = map(int, input() .split() ) 
	susjedi[a].append(b)
	susjedi[b].append(a) 

broj = int(input())
for s in susjedi[broj]:
	print(s)
# zadatak se također mogao rješiti preko matrice susjedstva koju ste napisali u prvom zadataku(ako niste tako rješili pokušajte razmisliti kako)
