#Actividades 
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print ("Hola Mundo!")

print("\n############################################\n") 
 
# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

nombre = input("Ingrese su nombre a continuacion: ")

print(f"\nHola {nombre} bienvenido a la UTN!")

print("\n############################################\n") 

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia 
# e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir 
# “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

print("Solicitamos que a continuacion ingrese sus datos personales:\n")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
pais = input("Pais: ")

print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {pais}!")

print("\n############################################\n") 

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

print("Para el siguiente ejercicio vamos a calcular el perimetro y el area de un circulo!\n")

radio = float(input("Le solicitamos que ingrese un valor para el 'radio': "))

pi = 3.14159
perimetro = 2*pi*radio
area = pi*radio*radio

print(f"\nEl radio ingresado es: {radio}")
print(f"El perimetro del circulo es: {perimetro}.")
print(f"EL area del circulo es: {area}.")

print("\n############################################\n") 

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

print("Calcular 'horas' en funcion de 'segundos' igresados.\n")

segundos = int(input("Ingrese cantidad en segundos: "))

horas = segundos/3600

print(f"\n{segundos} segundos equivalen a {horas} horas!")

print("\n############################################\n") 

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 

num = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))

print(f"\nTabla de multiplicar de {num}:")

print(f"\n{num} X 1 =",1*num)
print(f"{num} X 2 =",2*num)
print(f"{num} X 3 =",3*num)
print(f"{num} X 4 =",4*num)
print(f"{num} X 5 =",5*num)
print(f"{num} X 6 =",6*num)
print(f"{num} X 7 =",7*num)
print(f"{num} X 8 =",8*num)
print(f"{num} X 9 =",9*num)
print(f"{num} X 10 =",10*num)

print("\n############################################\n") 

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 
# y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Ingrese dos numeros enteros distintos de 'cero'\n")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

sumar = a+b
restar = a-b
dividir = a/b
multiplicar = a*b

print (f"\nEl resultado de sumar ambos numeros es: {sumar}")
print (f"El resultado de restar ambos numeros es: {restar}")
print (f"El resultado de dividir ambos numeros es: {dividir}")
print (f"El resultado de multiplicar ambos numeros es: {multiplicar}")

print("\n############################################\n") 
 
# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2

print("Calculemos su indice de masa corporal (IMC)\n")

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

IMC = peso / (altura ** 2)

print(f"\nSu indice de masa corporal es IMC = {IMC} kg/m")

print("\n############################################\n") 

#9) Crear un programa que pida al usuario una temperatura en grados Celsius 
# e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

print("Coversor de grados Celsius a grados Fahrenheit.\n")

C = float(input("Ingrese temperatura en Celsius: "))

F = 9/5*C+32

print(f"\n{C} grados Celsius equivalen a {F} grados Fahrenheit!")

print("\n############################################\n") 

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

print ("Ingrese 3 números para calcular su promedio.\n")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

prom = (a+b+c)/3

print(f"\nSu promedio es = {prom} ")

print("\n############################################\n")