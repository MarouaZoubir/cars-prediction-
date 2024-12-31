import pandas as pd
import numpy as np
data_dict = {
    'marque': ['BMW', 'Toyota', 'Renault'],
    'modèle': ['X5', 'Corolla', 'Clio'],
    'Carburant': ['Diesel', 'Essence', 'Hybride'],
    'price': [50000, 20000, 15000],
    'Année': [2020, 2018, 2019],
    'Kilométrage': [30000, 50000, 45000],
    'Puissance fiscale': [10, 7, 5]
}

df = pd.DataFrame(data_dict)

# Simuler les colonnes encodées après transformation
X_columns = ['Année', 'Kilométrage', 'Puissance fiscale', 
             'Carburant_Diesel', 'Carburant_Essence', 'Carburant_Hybride',
             'marque_BMW', 'marque_Toyota', 'marque_Renault',
             'modèle_X5', 'modèle_Corolla', 'modèle_Clio']

# Simuler les données utilisateur
user_input = {
    'Année': 2020,
    'Kilométrage': 35000,
    'Puissance fiscale': 9,
    'marque': 'BMW',
    'modèle': 'X5',
    'Carburant': 'Diesel'
}

# Convertir la liste de colonnes en DataFrame pour obtenir les colonnes simulées
X = pd.DataFrame(columns=X_columns)

# Définir la fonction à tester
def input_to_one_hot(data):
    enc_input = np.zeros(len(X_columns))
    
    # Remplir les valeurs numériques
    enc_input[0] = data['Année']
    enc_input[1] = data['Kilométrage']
    enc_input[2] = data['Puissance fiscale']
    
    ##################### Marque #########################
    redefinded_user_input = 'marque_' + data['marque']
    mark_column_index = X_columns.index(redefinded_user_input)
    enc_input[mark_column_index] = 1
    
    ##################### Modèle #########################
    redefinded_user_input = 'modèle_' + data['modèle']
    model_column_index = X_columns.index(redefinded_user_input)
    enc_input[model_column_index] = 1
    
    ##################### Carburant ######################
    redefinded_user_input = 'Carburant_' + data['Carburant']
    fuelType_column_index = X_columns.index(redefinded_user_input)
    enc_input[fuelType_column_index] = 1
    
    return enc_input

# Tester la fonction
encoded_input = input_to_one_hot(user_input)

# Afficher le résultat encodé
print("Encodage des données utilisateur :")
print(encoded_input)