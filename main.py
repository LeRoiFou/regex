""""
Les expressions rationnelles (REGEX)

Lien n° 1 (formation vidéo) : https://www.youtube.com/watch?v=f3QwwnvSQ50&feature=youtu.be
Lien n° 2 : https://www.youtube.com/watch?v=PSvlRi42MK8

Lien pour tester des expressions rationnelles : https://regex101.com/
(similaire à python tutor pour des programmes simples)

L'expression rationnelle vient du terme anglais "regular expression" abrégé par REGEX : attention on ne traduit pas ce
terme en français d'expressions régulières mais d'expressions rationnelles

Fichier sur les principes des expressions rationnelles :
C:/Users/LRCOM/Documents/expressionsrationnelles/principes.ods

Dans ce test on peut voir qu'on a recours au r"" (f"" pour l'affichage des données) qui est formellement conseillé pour
les expressions rationnelles

Éditeur : Laurent REYNAUD
Date : 17-02-3021
"""

import re  # module pour les expressions rationnelles

"""--------------------------------------------------------------------------------------------------------------------
Récupération du 1er mot "Hello" de la donnée suivante : "Hello World Hello World"
--------------------------------------------------------------------------------------------------------------------"""
data = "Hello World Hello World"
matches = re.compile(r"^Hello")
result = matches.findall(data)
result_str = "".join(map(str, result))  # conversion du résultat obtenu en liste sous la forme d'une str
print(result_str)

"""--------------------------------------------------------------------------------------------------------------------
Récupération du dernier mot "World" de la donnée suivante : "Hello World Hello World"
--------------------------------------------------------------------------------------------------------------------"""
data = "Hello World Hello World"
matches = re.compile(r"World$")
result = matches.findall(data)
result_str = "".join(map(str, result))  # conversion du résultat obtenu en liste sous la forme d'une str
print(result_str)

"""--------------------------------------------------------------------------------------------------------------------
Récupération de toute la donnée : "25$"
--------------------------------------------------------------------------------------------------------------------"""
data = "25$"
matches = re.compile(r"^25\$$")
result = matches.findall(data)
result_str = "".join(map(str, result))  # conversion du résultat obtenu en liste sous la forme d'une str
print(result_str)

"""--------------------------------------------------------------------------------------------------------------------
Récupération de la tabulation en début de donnée et de la chaîne de caractères qui suit la tabulation :
donnée : ‘  bonjour’
--------------------------------------------------------------------------------------------------------------------"""
data = "  bonjour"
matches = re.compile(r"[\ta-z]")
result = matches.findall(data)
result_str = "".join(map(str, result))  # conversion du résultat obtenu en liste sous la forme d'une str
print(result_str)

"""--------------------------------------------------------------------------------------------------------------------
Récupération de toute la donnée : "tester une-expression-rationnelle-avec-Python"
--------------------------------------------------------------------------------------------------------------------"""
data = 'tester une-expression-rationnelle-avec-Python'
matches = re.compile(r"^[\s\w-]+$")
result = matches.findall(data)  # recoupement entre la str et l'expression rationnelle appliquée
result_str = "/".join(map(str, result))  # conversion du résultat obtenu en liste sous la forme d'une str
print(result_str)
print()

"""--------------------------------------------------------------------------------------------------------------------
Les différentes méthodes
--------------------------------------------------------------------------------------------------------------------"""
print('*' * 30 + " Les différentes méthodes " + '*' * 30)
text = "La phrase : 'Mélodie Monchel reçoit la gifle qu'elle semblait attendre patiemment'"
print(text)
print()

"""--------------------------------------------------------------------------------------------------------------------
Méthode avec findall() : renvoi sous la forme de liste tous les patterns présents dans la str dans l'ordre où elles sont 
trouvées
--------------------------------------------------------------------------------------------------------------------"""
print('*' * 30 + " Méthode avec findall() " + '*' * 30)
matches = re.compile(r're',  # caractères recherchés
                     re.IGNORECASE  # majuscules/minuscules ignorées
                     )
print(f"Liste des caractères recherchés : {matches.findall(text)}")
print()

"""--------------------------------------------------------------------------------------------------------------------
Méthode avec sub() : permet de remplacer les occurences souhaitées
--------------------------------------------------------------------------------------------------------------------"""
print('*' * 30 + " Méthode avec sub() " + '*' * 30)
pattern = 'gifle'
matches = re.sub(pattern,  # caractères recherchés
                 r'fessée',  # caractères à remplacer
                 text)
print(matches)
print()

"""--------------------------------------------------------------------------------------------------------------------
Méthode avec split() : renvoi sous la forme de liste les caractères non recherchés
--------------------------------------------------------------------------------------------------------------------"""
print('*' * 20 + " Méthode avec split() " + '*' * 20)
ratio = re.compile(r"i")
matches = ratio.split(text)
ma_str = "".join(map(str, matches))
print(ma_str)
print()

"""--------------------------------------------------------------------------------------------------------------------
Méthode avec finditer() avec la boucle for : renvoi sous la forme d'objet la position des caractères recherchés
--------------------------------------------------------------------------------------------------------------------"""
print('*' * 20 + " Méthode avec finditer() " + '*' * 20)
ratio = re.compile(r"m")
matches = ratio.finditer(text)
for match in matches:
    print(match)
print()

"""--------------------------------------------------------------------------------------------------------------------
Méthode avec finditer() combinée avec span(), start(), end() et la boucle for :
-> la méthode span() permet d'afficher sous la forme de tuple la position des caractères recherchés
-> la méthode start() permet d'afficher sous la forme d'un entier la première position des caractères recherchés
-> la méthode end() permet d'afficher sous la forme d'un entier la dernière position des caractères recherchés
--------------------------------------------------------------------------------------------------------------------"""
print('*' * 20 + " Méthode avec finditer() combinée avec span(), start() et end() " + '*' * 20)
ratio = re.compile(r"m")
matches = ratio.finditer(text)
for match in matches:
    print(match.span(), match.start(), match.end())
print()

"""--------------------------------------------------------------------------------------------------------------------
Méthode avec finditer() combinée avec group() : permet d'afficher sous la forme d'1 str les caractères recherchés
--------------------------------------------------------------------------------------------------------------------"""
print('*' * 20 + " Méthode avec finditer() combinée avec group() " + '*' * 20)
ratio = re.compile(r"m")
matches = ratio.finditer(text)
for match in matches:
    print(match.group())
    print(match.group()[0])  # affichage du caractère à l'indice 0
print()

"""--------------------------------------------------------------------------------------------------------------------
Méthode avec search : renvoi sous la forme d'entiers, la position des patterns présents dans la str en 1ère instance 
uniquement
--------------------------------------------------------------------------------------------------------------------"""
print('*' * 30 + " Méthode avec search() " + '*' * 30)
matches = re.compile(r'm',  # caractère recherché
                     re.IGNORECASE  # majuscules/minuscules ignorées
                     )
if matches.search(text):
    print(f"Position du 1er 'm/M' : {matches.search(text).start()}, {matches.search(text).end()}")
print()

"""--------------------------------------------------------------------------------------------------------------------
Méthode avec match : renvoi sous la forme d'objet la position des patterns présents dans la str ssi ils sont au début de 
la variable 
--------------------------------------------------------------------------------------------------------------------"""
print('*' * 30 + " Méthode avec match() " + '*' * 30)
matches = re.compile(r'm',  # caractère recherché
                     re.IGNORECASE  # majuscules/minuscules ignorées
                     )
print("Position du 'm/M' au début de la str ?")
if matches.match(text):
    print(f"Oui : {matches.match(text)}")
else:
    print("Non")
print()
