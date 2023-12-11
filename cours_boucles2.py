# Imprime 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Imprime uniquement les nombres impairs - 1,3,5,7,9
for x in range(10):
    # Vérifiez si x est pair
    if x % 2 == 0:
        continue
    print(x)