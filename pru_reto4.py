"""
Ejemplo para crear la matriz de existencias con dimensionamiento estático y luego disminuir la existencia para alguna de ELLIPSIS_MARKER
"""
from fun_mat import imprimirmatriz
try:
  n = int(input('Indique la cantidad de sucursales    :'))
  k = int(input('Indique la cantidad de medicamentos  :'))
  # se realiza la matriz de acondicionamiento estático
  existencias = []
  for i in range(n):
      existencias.append([0]*k)
  #Se imprime la matriz
  imprimirmatriz(existencias)
  # Se llena la matriz
  for i in range(n):
      datos = input.strip().split()
      for j in range(k):
          existencias[i][j]=int(datos[j])
# imprime la matriz para ve si la llenó
  print('uno')
