

def my_function():
    print("Bonjour de ma fonction !")

def ma_fonction_avec_args(utilisateur, message):
    print("Bonjour, %s, De ma fonction !, je vous souhaite %s"%(utilisateur, message ))

def somme_de_deux_nombres(a, b):
    return a + b

# imprimer (un simple message )
my_function()

#prints "Bonjour Mouslim Koms, De ma fonction !, je vous souhaite une excellente année !"
ma_fonction_avec_args("Mouslim Koms", "une belle année !")

# après cette ligne, x contiendra la valeur 3 !
x = somme_de_deux_nombres(1,2)