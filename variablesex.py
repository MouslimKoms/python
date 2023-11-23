

#Le but de cet exercice est de créer une chaîne, 
# un entier et un nombre à virgule flottante. 
# La chaîne doit être nommée machaine doit contenir le mot « stock ». 
# Le nombre à virgule flottante doit être nommé LotsAvirgules doit contenir le nombre 10,9348, 
# l'entier doit être nommé Lotscomplets doit contenir le nombre 20.
machaine = "stock"
LotsAvirgules = 10.9348
Lotscomplets = 20

if machaine == "stock" :
    print("inventaire : %s" % machaine)
    
if isinstance(LotsAvirgules, float) and LotsAvirgules == 10.9348 :
    print("Lots incomplets  : %f" % LotsAvirgules)
    
if isinstance(Lotscomplets, int) and Lotscomplets == 20 : 
    print("Lots complet : %d" % Lotscomplets)
    