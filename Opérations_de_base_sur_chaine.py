chaine = "catalogues panneaux solaire!"
print(chaine)
chaine0 = 'catalogues panneaux solaire!'
print(chaine0)

chaine1 = "catalogues panneaux solaire!"
print("les guillements simple sont ' '")
print(chaine1)

print(len(chaine1))

chaine2 = "catalogues panneaux solaire!"
print(chaine2.index("i"))

chaine3 = "catalogues panneaux solaire!"
print(chaine3.count("n"))

chaine4 = "catalogues panneaux solaire!"
print(chaine4[3:7])


chaine5 = "catalogues panneaux solaire!"
print(chaine5[3:14:8])



chaine6 = "catalogues panneaux solaire!"
print(chaine6[3:9])
print(chaine6[3:9:1])

chaine7 = "catalogues panneaux solaire!"
print(chaine7[::-1])

chaine8 = "catalogues panneaux solaire!"
print(chaine8.upper())
print(chaine8.lower())

chaine9 = "catalogues panneaux solaire!"
print(chaine9.startswith("catalogues"))
print(chaine9.endswith("es pann"))


chaine11 = "catalogues de panneaux"
afewwords = chaine11.split(" ") 
print(afewwords)
