# Imprime 0,1,2,3,4 puis imprime "la valeur de comptage a atteint 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("valeur de comptage atteinte %d" %(count))

# Imprime 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("ceci n'est pas imprimé car la boucle for est terminée en raison d'une rupture mais pas en raison d'un échec en condition")