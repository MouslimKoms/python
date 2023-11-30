number = 1 + 2 * 3 / 4.0
print(number)

reste = 11 % 3
print(reste)

squared = 7 ** 2 #7*7=49
cubed = 2 ** 3   #2*2*2=8
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

répétebonjourdixfois = "bonjour" * 10
print(répétebonjourdixfois)

Nombre_Paire = [2,4,6,8]
Nombre_Impaire = [1,3,5,7]
Nombre_Paire_Impaire = Nombre_Paire + Nombre_Impaire
print(Nombre_Paire_Impaire)

print([1,2,3] * 3)


x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contient %d objets" % len(x_list))
print("y_list contient %d objets" % len(y_list))
print("big_list contient %d objets" % len(big_list))


if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Presque la ...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Super!")