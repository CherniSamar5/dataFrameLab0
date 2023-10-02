import pandas as pd
import matplotlib.pyplot as plt


myData = {
    'Pays': ['États-Unis', 'Chine', 'Inde', 'Japon'],
    'Population': [331002651, 1439323776, 1380004385, 126476461],
    'Superficie (km²)': [9629091, 9640011, 3287263, 377972],
    'Taux de croissance annuel (%)': [0.6, 0.4, 1.1, -0.2]
}

# Question 2: Transformer cette dataframe en un dictionnaire nommé « dict_pays ».
df_p = pd.DataFrame(myData)

#print(df_p)
'''transformer le dataFrame en dictionnaire d'ou la colonne "Pays" pour que chaque pays devienne une clé dans le dictionnaire
et les autres attributs constituent un autre dictionnaire qui est la valeur de la clé '''
dictPays = df_p.set_index('Pays').to_dict(orient='index')

print(dictPays)

# Question 3 : Trier le dictionnaire par ordre croissant de la population
dictPaysSorted = dict(sorted(dictPays.items(), key=lambda x: x[1]['Population']))

print(dictPaysSorted)

#Question 4 :

# Extraire les noms des pays (qui sont dans la colonne 'Pays' de notre DataFrame)
namePays = df_p['Pays']

# Extraire les populations (qui sont dans la colonne 'Population' de notre DataFrame)
population = df_p['Population']

# Créer le graphique à barres avec des couleurs
plt.bar(namePays, population, color='red')

#Ajouter des titres aux axes
plt.xlabel('Pays')
plt.ylabel('Population')
plt.title('Population/pays')

# Afficher le graphique
plt.show()


#Question5 :
# Extraire la superficie
superficie = df_p['Superficie (km²)']

# Extraire le taux de croissance
tauxCroissance = df_p['Taux de croissance annuel (%)']

# Créer le graphique en nuage de points (scatter plot)
plt.scatter(superficie, tauxCroissance, color='green', marker='o')

# Ajouter des titres
plt.xlabel('Superficie (km²)')
plt.ylabel('Taux de croissance annuel (%)')
plt.title('Relation entre Superficie et Taux de croissance annuel')

# Afficher le graphique
plt.show()

