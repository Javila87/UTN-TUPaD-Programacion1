# PRACTICO 3: ESTRUCTURAS CONDICIONALES

# OBJETIVO: Comprender y aplicar las estructuras condicionales en la programación, 
# desarrollando algoritmos que involucren tomas de decisiones.

# ACTIVIDADES
 
# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

MAYOR = 18 
edad = int(input("Ingrese su edad: "))

if edad >= MAYOR:
    print("Es mayor de edad.")
elif edad <= 0:
    print("Error: ingrese edad valida.")
else:
    print("Es menor de edad.")
print ("Gracias.\n")


# 2) Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("Ingrese una nota: "))

A = nota >= 6 and nota <= 10
D = nota > 0 and nota < 6

if A:
    print("Aprobado.")
elif D:
    print("Desaprobado.")    
else:
    print("Error: Ingrese nota valida.")
print("Gracias.\n")


# 3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.") 
print("Gracias.\n")  


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: ")) 

if edad > 0 and edad < 12:
    print("Niño/a.")
elif edad >= 12 and edad < 18:
    print("Adolecente.")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven.")
elif edad >= 30 and edad < 120:
    print("Adulto/a mayor.")
else:
    print("Error: ingrese edad valida.")        
print ("Gracias.\n")            


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje 
# "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un 
# iterable tal como una lista o un string. 

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
print("Gracias.\n")
 
 
# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular
# la moda (mode), la mediana (median) y la media (mean) de dichos números. Parámetros estadísticos que 
# se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: la media es mayor que la mediana y la mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: la media es menor que la mediana y la mediana es menor que la moda. 
# ● Sin sesgo: la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado: Escribir un programa que tome la lista numeros_aleatorios, 
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o 
# no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mean, median, mode
import random

# Lista aleatoria

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular: media, mediana, moda.

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Calcular sesgo.

if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo."
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo." 
elif media == mediana == moda:
    sesgo = "Sin sesgo."    
else:
    sesgo = "No aplica condicion."

# Mostrar resultados

print("Lista aleatoria:",numeros_aleatorios)
print("Media:",media)
print("Mediama:",mediana)
print("Moda:",moda)
print("Resultado:",sesgo)


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Definir frase o palabra
palabra = input("\nIngresa una frase o palabra: ")

# Definir vocales (incluyo acentuadas)
vocales = "aeiouáéíóú"

# Quitar espacios finales para evaluar último caracter. 
cadena = palabra.rstrip()

# Comprobar cadena no vacía, ultimo caracter a minuscula y si es vocal.

if cadena == "":
    print("Dato vacio e invalido.")
elif cadena[-1].lower() in vocales:
    print(cadena + "!")
else:
    print(cadena)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("\nIngrese su nombre: ")

print("Ingrese una opción:")
print("1- Nombre en MAYÚSCULAS.")
print("2- Nombre en minúsculas.")
print("3- Solo la primer letra en mayúscula.")

opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:",nombre.upper())
elif opcion == "2":
    print("Resultado:",nombre.lower())
elif opcion == "3":
    print("Resultado:",nombre.title())
else:
    print("Opción no válida.")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud 
# en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("\nIngrese la magnitud de un terremoto: "))

muy_leve = 0 < magnitud < 3
leve = 3 <= magnitud < 4
moderado = 4 <= magnitud < 5
fuerte = 5 <= magnitud < 6
muy_fuerte = 6 <= magnitud < 7
extremo = 7 <= magnitud <= 10

if muy_leve: 
    print("Muy leve (imperceptible).")
elif leve:
    print("Leve (ligeramente perceptible).") 
elif moderado:
    print("Moderado (sentido por personas, pero generalmente no causa daños).") 
elif fuerte:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif muy_fuerte:
    print("Muy Fuerte (puede causar daños significativos).")
elif extremo:
    print("Extremo (puede causar graves daños a gran escala).")
else:
    print("Magnitud fuera de rango! (mínima detectable superior a 0, máxima 10)")
                            

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:
# Desde 21 de diciembre hasta 20 de marzo (incluidos) Hemisferio norte: Invierno. Hemisferio sur: Verano
# Desde 21 de marzo hasta 20 de junio (incluidos) Hemisferio norte: Primavera. Hemisferio sur: Otoño
# Desde 21 de junio hasta 20 de septiembre (incluidos) Hemisferio norte: Verano. Hemisferio sur: Invierno
# Desde 21 de septiembre hasta 20 de diciembre (incluidos) Hemisferio norte: Otoño. Hemisferio sur: Primavera
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), 
# qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir 
# por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

import sys 

print("\n¿En que hemisferio se encuentra?")
print("Ingrese una opción:")
print("N: Hemisferio Norte.")
print("S: Hemisferio Sur.")


hemisferio = input("Ingrese S/N: ").upper()

if hemisferio not in ("N","S"):
    print("Dato invalido! Volver a intentar.")
    sys.exit()  

print("\n¿En que mes del año se encuentra?")
print("Ingrese una opción:")
print("Del 1 al 12 para el mes.")

try:
    mes = int(input("Ingrese 1/12: "))
except ValueError:
     print("Dato invalido! Volver a intentar.")
     sys.exit()   

if not (1<= mes <= 12):
    print("Fuera de rango! Volver a intentar.")
    sys.exit()  

print("\n¿En que dia del mes se encuentra?")
print("Ingrese una opción:")
print("Del 1 al 31 para el dia.")

try:
    dia = int(input("Ingrese 1/31: "))
except ValueError:
    print("Dato invalido! Volver a intentar.")
    sys.exit()

if  not (1 <= dia <= 31):
    print("Fuera de rango! Volver a intentar.")  
    sys.exit()

if (mes == 12 and dia >= 21) or (mes == 3 and dia <=20) or ( 1 <= mes <=2):
    estacion_norte = "Invieno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or ( 4 <= mes <= 5):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or ( 7 <= mes <= 8):
    estacion_norte = "Verano"
    estacion_sur = "Inviermo"
elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or ( 10 <= mes <= 11):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    pass    

print(f"\nDia: {dia} - Mes: {mes} - Hemisferio: {hemisferio}")  

if hemisferio == "N":
    print(f"\nEs {estacion_norte} en el Hemisferio Norte!\n")
else:
    print(f"\nEs {estacion_sur} en el Hemisferio Sur!\n")

#Fin de la actividad.