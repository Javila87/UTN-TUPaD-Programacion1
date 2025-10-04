# Práctico 5: Listas

# Objetivo:
# Desarrollar la comprensión y la capacidad de manipular listas en Python mediante la aplicación de conceptos fundamentales 
# como la indexación, la modificación de elementos, el uso de métodos integrados y el manejo de listas anidadas.

# Actividades:
# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.

# 1) Crear una lista con las notas de 10 estudiantes.
# •Mostrar la lista completa.
# •Calcular y mostrar el promedio.
# •Indicar la nota más alta y la más baja.

print("-- Lista con notas de 10 estudiantes --")
# Notas de 10 estudiantes
notas = [6, 8, 7, 9, 10, 6, 4, 8, 7, 9]

# Mostrar lista
print("Notas de los estudiantes:")
for i in notas:
    print(i,end=" ")
print()

# Calcular promedio
promedio = sum(notas) / len(notas) # sum() suma los elementos / len() cantidad de elementos.
print("Promedio:", promedio)

# Resultados
print("Nota más alta:", max(notas)) # max(notas) → devuelve la nota más alta
print("Nota más baja:", min(notas)) # min(notas) → devuelve la nota más baja
print("-- Fin --")


# 2) Pedir al usuario que cargue 5 productos en una lista.
# •Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# •Preguntar al usuario qué producto desea eliminar y actualizar la lista.

print("-- Lista de 5 productos --")
productos = []

# Pedir al usuario 5 productos
for i in range(5):
    cargar = input("Ingrese un producto: ")
    productos.append(cargar)

# Mostrar ordenados alfabéticamente
print("Lista ordenada:")
for p in sorted(productos): # sorted() devuelve una nueva lista ordenada
    print(p,end=" ")
print()

# Eliminar producto
eliminar = input("Ingrese producto a eliminar de la lista: ")
if eliminar in productos:
    productos.remove(eliminar) # remove() borrar de lista productos

# Resultados
print("Lista actualizada:")
for p in productos:
    print(p,end=" ")
print()
print("-- Fin --")   


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# •Crear una lista con los pares y otra con los impares.
# •Mostrar cuántos números tiene cada lista.

print("-- Lista de 15 números al azar entre 1 y 100 --")

import random
numeros = []
pares = []
impares = []

# Listar 15 números al azar
for i in range(15):
    numeros.append(random.randint(1, 100))

# Lista par/impar
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

# Resultados
print("Lista de números:",numeros)
print("Total pares:",len(pares))
print("Total impares:",len(impares))


# 4)Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# •Crear una nueva lista sin elementos repetidos.
# •Mostrar el resultado.

print("-- Crear una lista sin valores repetidos --")
origonal = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_duplicados = []

# Lista sin duplicados
for v in origonal:
    if v not in sin_duplicados:  # busca si el valor ya está; si no, lo agrega.
        sin_duplicados.append(v)
  
# Resultados
print("Lista original:",origonal)
print("Lista sin duplicados:",sin_duplicados)
print("-- Fin --")


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# •Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# •Mostrar la lista final actualizada.

print("-- Lista de estudiantes presentes en clase --")
presentes = ["Jonatan", "Mar", "Sofia", "Gabriel", "Sara", "Laura", "Diego", "Ana"]

# Mostrar lista de estudiantes
for i in presentes:
    print(i,end=" ")
print()

# Opción agregar/eliminar estudiante
opcion = input("Ingrese (1) para agregar ó (2) para eliminar un estudiante: ")

if opcion == "1":
    nuevo = input("Ingrese el nombre: ")
    presentes.append(nuevo)
elif opcion == "2":
    eliminar = input("Ingrese el nombre a eliminar: ")
    if eliminar in presentes:
        presentes.remove(eliminar)

# Resultados
print("Lista final actualizada:")
for i in presentes:
    print(i,end=" ")
print()    
print("-- Fin --")    


# 6)Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha 
# (el último pasa a ser el primero).

print("-- Rotar elementos de una lista (el último pasa a ser el primero) --")

# Lista de 7 números
numeros = [1, 2, 3, 4, 5, 6, 7]
ultimo = numeros[-1]
print("Lista:",numeros)

# Rotar a la derecha
for i in range(len(numeros)-1, 0, -1):  # iterar de 6 a 1
    numeros[i] = numeros[i-1]           # si i=6, el 6 recibe el 5   
numeros[0] = ultimo

# Resultados
print("Lista rotada:", numeros)
print("-- Fin --")


# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# •Calcular el promedio de las mínimas y el de las máximas.
# •Mostrar en qué día se registró la mayor amplitud térmica.

print("-- Matriz 7x2 temperaturas min/max semanales --")

# Matriz temperaturas mínimas / máximas 7x2
matriz = [
    [10, 20],
    [12, 22],
    [9, 25],
    [11, 24],
    [13, 23],
    [8, 19],
    [10, 21]
]

# Mostrar Matriz
for fila in range(len(matriz)):
    for columna in range(len(matriz[0])):
        print(matriz[fila][columna],end=" ")
    print()

# Variables
suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia = 0

# Sumar temperaturas y calcular mayor amplitud
for i in range(7):                              # 7 días de la semana                    
    suma_min += matriz[i][0]                    # Suma temperaturas mínimas
    suma_max += matriz[i][1]                    # Suma temperaturas máximas
    amplitud = matriz[i][1] - matriz[i][0]      # Comparar para obtener la mayor amplitud
    if amplitud > mayor_amplitud:                        
        mayor_amplitud = amplitud
        dia = i + 1

# Calcular promedios y mostrar resultados
print(f"Promedio temperaturas mínimas: {round((suma_min / 7),2)}°C") # Redondeo a 2 decimales
print(f"Promedio temperaturas máximas: {round((suma_max / 7),2)}°C") # Redondeo a 2 decimales
print(f"Mayor amplitud térmica: {mayor_amplitud}°C. Regsitrada el {dia}° día de la semana.")
print("-- Fin --")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# •Mostrar el promedio de cada estudiante.
# •Mostrar el promedio de cada materia.

print("-- Matriz 5x3 de estudiantes y notas por materia --")

# Notas de 5 estudiantes en 3 materias
notas = [
    [7, 8, 10],
    [9, 6, 7],
    [6, 9, 8],
    [6, 10, 8],
    [8, 9, 7]
]

# Mostrar Matriz
for fila in range(len(notas)):
    for columna in range(len(notas[0])):
        print(notas[fila][columna],end=" ")
    print()

print("Estudiantes")
# Promedio por estudiante
for i in range(len(notas)): # Número de estudiantes
    promedio = sum(notas[i]) / len(notas[i]) # Sumar notas por fila y dividir por materias
    print(f"Promedio estudiante {i+1}: {round(promedio,2)}") # Resultado con dos decimales

print("Materias")
# Promedio por materia
materias = len(notas[0]) # Número de materias
for j in range(materias):
    suma = 0
    for i in range(len(notas)): # Sumar las notas
        suma += notas[i][j]
    print(f"Promedio materia {j+1}: {round((suma / len(notas)),2)}") 

print("-- Fin --")    

 
#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# •Inicializarlo con guiones "-" representando casillas vacías.
# •Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# •Mostrar el tablero después de cada jugada. 


print("-- Matriz 3x3 TA TE TI --")

# Tablero Ta-Te-Ti 3x3
tablero = [["-","-","-"],
           ["-","-","-"],
           ["-","-","-"]]

# Ingreso de posiciones
for turno in range(10):  # 10 jugadas posibles 
    
    # Asignar turnos jugador "X"(par) / "O"(impar)
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"
    print("Turno de", jugador)

    # Indicar posicion en tablero "X" / "O"
    fila = int(input("Ingrese fila (0 - 1 - 2): "))   
    col = int(input("Ingrese columna (0 - 1 - 2): ")) 
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador

    # Mostrar tablero
    for fila in tablero:
        print(fila)
print("-- Fin --")


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# •Mostrar el total vendido por cada producto.
# •Mostrar el día con mayores ventas totales.
# •Indicar cuál fue el producto más vendido en la semana.

print("-- Matriz 4x7 Tienda Comercial --")

# Ventas de 4 productos en 7 días
ventas = [
    [5, 3, 4, 2, 6, 1, 7],
    [2, 4, 1, 3, 2, 5, 4],
    [3, 6, 2, 7, 5, 6, 8],
    [4, 2, 5, 3, 6, 7, 5]
]

# Mostrar Matriz
for fila in range(len(ventas)):
    for columna in range(len(ventas[0])):
        print(ventas[fila][columna],end=" ")
    print()

# Total por producto
for i in range(len(ventas)):
    print(f"Producto {i+1} total: {sum(ventas[i])}")

# Día con mayores ventas
dia_mayor = 0
ventas_mayor = 0
for j in range(7): # días
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    if total_dia > ventas_mayor:
        ventas_mayor = total_dia
        dia_mayor = j + 1
print("Día con mayores ventas:", dia_mayor)

# Producto más vendido
mas_vendido = 0
producto = 0
for i in range(4): # producto
    total = sum(ventas[i])
    if total > mas_vendido:
        mas_vendido = total
        producto = i + 1
print("Producto más vendido:", producto)
print("-- Fin --")

