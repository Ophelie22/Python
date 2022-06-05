"""
Dans cet exercice, vous devez utiliser les fonctions de conversions
pour convertir les objets dans le bon type afin d'afficher les phrases
suivantes et éviter les erreurs.
Phrases à afficher :
J'ai une classe de 30 élèves
10 + 5 est égal à 15
15
L'addition de 10 + 5 est égal à 15
"""

a = "J'ai une classe de " + 30 + " élèves"
b = 10 + " + " + "5" + " est égal à " + 15
c = 10 + "5"
d = "L'addition de 10 + 5 est égal à " + 10 + 5

"""réponse = """

a = "J'ai une classe de " + str(30) + " élèves"
'''ici in va convertir en chaine de caretere str avec les autre chaines de caractereres '''
b = str(10) + " + " + "5" + " est égal à " + str(15)
'''Pareil que ci dessus'''
c = 10 +int("5")
'''La je convertie en nombre'''
d = "L'addition de 10 + 5 est égal à " + str(10 + 5)
'''La je converti en chaine de caractere'''

