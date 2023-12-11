x = 42
print(x == 42) # prints out True
print(x == 7) # prints out False
print(x < 43) # prints out True
print(x != 42)

name = "Mouslim"
age = 23
if name == "Mouslim" and age == 23:
    print("Votre nom est Mouslim et vous avez également 23 ans.")

if name == "Mouslim" or name == "Koms":
    print("Votre nom est Mouslim soit Koms" )
    
    
    name = "Koms"
if name in ["Mouslim", "Koms"]:
    print("Votre nom est Mouslim soit Koms")
    
    
declaration = False
declaration_a = True
if declaration is True:
    pass
elif declaration_a is True: 
    pass

else:
    pass


x = 2
if x == 2:
    print("x égal à deux!")
else:
    print("x n'est pas égal à deux.")
    
    
T = [1,2,3]
F = [1,2,3]
print(T == F)
print(T is F) 