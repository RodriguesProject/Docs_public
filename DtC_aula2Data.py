"""Aula 2 — NumPy: arrays, vetorização e estatística básica."""
import numpy as np

# Array unidimensional
array1 = np.array([10, 20, 30, 40, 50])
print(array1, "\n")
print("Terceiro elemento:", array1[2])
print("Fatia [1:4]:", array1[1:4])
print("Índices pares:", array1[::2])
print("Índices ímpares:", array1[1::2])

# Evite usar os nomes min e max, pois eles ocultam funções nativas do Python.
valor_minimo = np.min(array1)
valor_maximo = np.max(array1)
print("Mínimo:", valor_minimo)
print("Máximo:", valor_maximo)
print("Média:", np.mean(array1))
print("Mediana:", np.median(array1))
print("Desvio padrão:", np.std(array1))
print("Variância:", np.var(array1))

# Array bidimensional
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatriz:\n", array2)
print("Elemento da linha 2, coluna 3:", array2[1, 2])
print("Shape:", array2.shape)
print("Quantidade de elementos:", array2.size)
print("Tipo dos elementos:", array2.dtype)
print("Submatriz:\n", array2[0:2, 1:3])
print("Primeira coluna:", array2[:, 0])
print("Segunda linha:", array2[1, :])

# Exercício
array3 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
print("\nArray 3:", array3)
print("Média:", np.mean(array3))
print("Mediana:", np.median(array3))
print("Desvio padrão:", np.std(array3))
print("Variância:", np.var(array3))
