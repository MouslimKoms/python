# Modifiez cette fonction pour renvoyer une liste de chaînes comme défini ci-dessus
def list_benefits():
     return "Code plus organisé", "Code plus lisible", "Réutilisation du code plus facile", "Permettre aux programmeurs de partager et de connecter du code ensemble"

# Modifiez cette fonction pour la concaténer à chaque benefit - " est un benefit des fonctions ! "
def build_sentence (benefit):
     return "%s est un avantage des fonctions !" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    
    
    
    for benefit in list_of_benefits:
    
            print(build_sentence(benefit))

name_the_benefits_of_functions()

