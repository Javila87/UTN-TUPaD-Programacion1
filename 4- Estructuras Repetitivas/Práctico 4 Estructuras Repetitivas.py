# Práctico 4: Estructuras repetitivas

# Objetivo: Implementar ciclos para resolver problemas que requieran repetición de acciones.

# Actividades
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print("-- Números del 0 al 100 --")

for numero in range(101):        # de 0 a 100
    print(numero)                # un número por línea.

print("-- Fin --")


# 2) Desarrolla un programa que solicite al usuario un número entero 
# y determine la cantidad de dígitos que contiene.

print("-- Determinar número de dígitos --")

# Pedimos al usuario un número entero
while True:                                                # Controlar errores
    try:
        numero = int(input("Ingrese un número entero: "))  # Si es correcto → break
        break
    except ValueError:
        print("Error: Ingrese un número entero valido!")   # Invalido → vuelve a pedir dato
         
# Convertir a cadena para contar sus caracteres
digitos = len(str(abs(numero)))                   # abs() Para números negativos (valor absoluto)

print("-----------------")

# Resultado 
print(f"El número {numero} tiene {digitos} digito/s.")

print("-- Fin --")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("-- Suma entre dos valores --")

sumatoria = 0
lista_valores = []

print("Determine un rango númerico:")

print("-----------------------")

while True:
    try:
        # Pedimos datos al usuario
        minimo = int(input("Ingrese el valor mínimo = "))    
        maximo = int(input("Ingrese el valor máximo = ")) 
        
        # Validar rango
        if maximo > minimo and (maximo - minimo) >= 2:    # al menos un valor
            break 
        else:
            print("Error: Debe existir al menos un valor excluyendo extremos!")

    except ValueError:
        print("Error: Ingrese un dato valido!")

# Suma de valores excluyendo extremos
for valores in range(minimo+1,maximo):
    sumatoria += valores
    lista_valores.append(valores)        # lista de valores

print("-----------------------")

# Resultado
print(f"RANGO = ({minimo},{maximo})")
print("NUMEROS =",lista_valores)
print("SUMA TOTAL =",sumatoria)

print("-- Fin --")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("-- Suma secuencial --")

# Definimos variables
CORTE = 0 
suma_total = 0

# Pedimos dato al usuario        
numero = int(input("Ingrese valor a sumar (" + str(CORTE) + " para finalizar): "))

while numero != CORTE:

    suma_total += numero

    numero = int(input("Ingrese otro número (" + str(CORTE) + " para finalizar): "))

print("----------------")    

# Resultado    
print("SUMA TOTAL:", suma_total)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print("-- ADIVINA EL NUMERO SECRETO --")
print("El objetivo del juego es adivinar un número entre 0 y 9!")
print("¿Aceptas el deafio? A jugar!")

import random
intento= 0

print("--------------------")

# Numero aleatorio
numero_secreto = random.randint(0,9)     

while True:
    
    numero = int(input("Intenta adivinar: "))

    intento += 1
    if numero == numero_secreto:
        print("Adivinaste!")
        break
    elif numero > numero_secreto:
       print("Pista: Es menor!")
    elif numero < numero_secreto:
      print("Pista: Es mayor!")

print("--------------------")

print(f"El {intento}º intento fue el correcto!.")
print("-- GRACIAS POR JUGAR! ---")
   

# 6) Desarrolla un programa que imprima en pantalla todos los números pares 
# comprendidos entre 0 y 100, en orden decreciente.

print("-- Números pares del 100 al 0 --")

#Imprimir números pares
for i in range(100,-1,-2):   # de 100 a 0
    print(i,end=" ")

print("\n-- Fin --")    


# 7) Crea un programa que calcule la suma de todos los números comprendidos 
# entre 0 y un número entero positivo indicado por el usuario.
  
print("-- Suma de números positivos --")

suma_total = 0

while True:
    try:
        # Pedir dato al usuario
        numero = int(input("Ingrese un valor positivo: "))

        # Verificar si el numero es positivo
        if numero > 0:
            break
        else:
            print("Error: El número debe ser positivo!")

    except ValueError:
        print("Error: Ingrese un dato valido!")    

# Rango de números
for i in range(numero+1):
    suma_total += i
print("------------------")

# Resultado
print(f"RANGO = (0,{numero})")
print("SUMA TOTAL =",suma_total) 
print("-- Fin --")   


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("-- Clasificación de números --")

# Definimos constante y variables
RANGO = 5
par = 0
impar = 0
negativo = 0
positivo = 0

print(f"Ingrese {RANGO} números.")

# Rango de números enteros posibles
for cont in range(RANGO):
    while True:                                                # Control de errores
        try:
            numero = int(input(f"ingrese número {cont+1}: "))  # Si es correcto → break
            break
        except ValueError:
            print("Error: Ingrese un número entero valido!")   # Invalido → vuelve a pedir dato
    
    # Clasificar par/impar
    if numero % 2 == 0:
        par += 1     
    else:
        impar += 1
    
    # Clasificar positivo/negativo
    if numero > 0:       
        positivo += 1
    elif numero < 0:
        negativo += 1

# Resultados
print("POSITIVOS =",positivo)
print("NEGATIVOS =",negativo)
print("PARES =",par)
print("IMPARES =",impar)
print("-- Fin --")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

print(f"-- Cacular la Media de {RANGO} números --")

from statistics import mean

# Definir constante y lista vacia
RANGO = 5
lista_numeros = []

print(f"Ingrese {RANGO} números enteros.")

# Rango de números enteros
for cont in range(RANGO):
    while True:
        try:
            numero = int(input(f"ingrese número {cont+1}: "))
            lista_numeros.append(numero)                       # Guardar en la lista
            
            break
        except ValueError:
            print("Error: Ingrese un número entero valido!")

print("-------------------")

# Calcular media
media = mean(lista_numeros)
           
# Mostrar lista completa
print("LISTA =",lista_numeros)

# Resultado media
print("MEDIA =",media)
print("-- Fin --")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("-- Invertir orden de los dígitos --")

while True:
    try:
        numero = int(input("Ingrese un número de 2 digitos o mayor: "))

        if numero >= 10:
            numero_invertido = int(str(numero)[::-1])
            break
        elif numero <= -10:
            numero_invertido = int(str(abs(numero))[::-1]) * (-1)
            break
        else:
            print("Incorrecto") 

    except ValueError:
        print("Error: Ingrese un dato valido!")    

print("--------------")

# Resultado
print("NUMERO =",numero)
print("INVERTIDO =",numero_invertido)
print("-- Fin --")