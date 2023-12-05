s = "Strings sont géniaux!"
# La longueur devrait être de 21
print("La longueur de s = %d" % len(s))

# La première occurrence de "u" doit être à l'index 18 
print("La première occurrence de u = %d" % s.index("u"))

# Le nombre de a doit être 1 
print("Le nombre de A dans la chaine %d" % s.count("a"))

# Découper la chaîne en bits
print("Les cinq premiers caractères sont'%s'" % s[:5]) # Les cinq premiers
print("Les cinq caractères suivants sont '%s'" % s[5:10]) # 5 a 10
print("Les treizième caractères est '%s'" % s[12]) # Les treizième 12
print("Les caractères d'index impair sont'%s'" %s[1::2])#(indexation basée sur 0)
print("Les cinq derniers caractères sont'%s'" % s[-5:]) # Les cinq derniers

# Convertir tout en majuscules
print("Chaîne en majuscule: %s" % s.upper())

# Convertir tout en minuscules
print("Chaîne en minuscules: %s" % s.lower())

# Vérifiez comment commence une chaîne
if s.startswith("Str"):
    print("La chaîne commence par'Str'. Good!")

# Vérifiez comment se termine une chaîne
if s.endswith("aux!"):
    print("La chaîne se termine par'aux!'. Good!")

# Divisez la chaîne en trois chaînes distinctes,
# chacun contenant seulement un mot
print("Divisez les mots de la chaîne: %s" % s.split(" "))