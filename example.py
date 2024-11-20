# example.py
import numpy as np

# Créer un tableau NumPy avec des valeurs de 0 à 9
array = np.arange(10)

# Afficher le tableau
print("Tableau NumPy:")
print(array)

# Calculer la somme des éléments du tableau
sum_array = np.sum(array)
print("\nSomme des éléments du tableau:")
print(sum_array)

# Créer une matrice 2x3
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Afficher la matrice
print("\nMatrice 2x3:")
print(matrix)

# Calculer la transposée de la matrice
transpose_matrix = np.transpose(matrix)
print("\nTransposée de la matrice:")
print(transpose_matrix)
