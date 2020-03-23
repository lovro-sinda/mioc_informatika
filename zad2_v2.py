N = int(input())
K = int(input())
matrica = []

for i in range(K+1):          
    a = [] 
    for j in range(K+1):  
         a.append(0) 
    matrica.append(a) 

for i in range(N):
  x = int(input())
  y = int(input())
  matrica [x][y] = 1
  matrica [y][x] = 1

broj = int(input())
#Pazim da su mi čvorovi indeksirani od 1 do K (uključivo)
for i in range(1,K+1): 
    if (matrica [i][broj] == 1):
      print(i)
