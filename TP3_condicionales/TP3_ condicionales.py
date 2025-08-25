#Práctico 3: Estructuras condicionales.
#ACTIVIDAD 1
    #defino la edad minima y pido al usuario su edad.
edad_minima = 18
edad = int(input("Por favor ingrese su edad: "))
    #comparo los valores e imprimo resultado
if edad >= edad_minima:
    print("Es mayor de edad")




#ACTIVIDAD 2
    #defino la nota para aprobar y pido al usuario su nota.
nota_aprueba = 6
nota = int(input("Por favor ingrese su nota: "))
    #comparo la nota con la necesaria para aprobar.
if nota >= nota_aprueba:
    print("Aprobado")
else:
    print("Desaprobado")


    
    
#ACTIVIDAD 3
    #pido al usuario un numero par
num1 = int(input("Por favor ingrese un numero par: "))
    #comparo con el modulo si el numero que ingreso es realmente par o no.
if num1 % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par.")
    


    
#ACTIVIDAD 4
    #pido la edad al usuario
edad = int(input("Porfavor ingrese su edad: "))
    #comparo su edad con los rangos de edad para saber a que categoria pertenece
if edad < 12:
    print("Usted es un Niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es Adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es Adulto/joven")
else:
    print("Usted es Adulto")


    
    
#ACTIVIDAD 5
    #defino los parametros, y pido al usuario que ingrese una contraseña.
    #uso "len" para extraer la longitud
contraseña = input("Porfavor introduce una contrseña entre 8 y 14 caracteres: ")
largo_contraseña = len(contraseña)
largo_minimo = 8
largo_maximo = 14
    #comparo si el largo es el requerido
if largo_contraseña >= largo_minimo and largo_contraseña <= largo_maximo:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")




#ACTIVIDAD 6
    #importo el random, y creo la variable que almacene los 50 numeros aleatorios.
    #los imprimo por pantalla para saber los valores.
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)

    #importo el paquete statistics
from statistics import mode, median, mean

    #calculo e imprimo cada uno de los valores obtenidos
moda = mode(numeros_aleatorios)
print(f"El valor mas repetido es {moda}")
mediana = median(numeros_aleatorios)
print(f"El valor central es {mediana}")
media = mean(numeros_aleatorios)
print(f"El promedio es {media}")

    #comparo los sesgos
if media > mediana and mediana > moda:
    print("Hay sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
     print("No se puede determinar un sesgo.")




#ACTIVIDAD 7
    #pido una frase o palabra al usuario
frase = input("Porfavor ingrese una frase o una frase o palabra: ")
    #con la funcion len extraemos el ultimo caracter del indice frase
ultimo_caracter = frase[len(frase)-1]

    #comparamos todas las vocales con el caracter 
if ultimo_caracter == "a" or ultimo_caracter == "e" or ultimo_caracter == "i" or ultimo_caracter == "o" or ultimo_caracter == "u"\
    or ultimo_caracter == "A" or ultimo_caracter == "E" or ultimo_caracter == "I" or ultimo_caracter == "O" or ultimo_caracter == "U":
    print(f"{frase}!")
else:
    print(frase)
    
    
    
    
#ACTIVIDAD 8
    #pido al usuario su nombre y  luego le doy las opciones para que elija la forma de escritura. La opcion la guardo como entero en una variable.
nombre = str(input("Porfavor ingrese su nombre: "))
print("Elija la opcion deseada para escribir su nombre: ")
opcion = int(input("1 Si quiere su nombre en mayuscula. EJEMPLO: PEDRO,\n2 Si quiere su nombre en minuscula. EJEMPLO: pedro,\n3 Si quiere su nombre con la primera letra Mayuscula. EJEMPLO: Pedro "))

    #comparo las opciones y convierto el texto utilizando las funciones.
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
    
    
    
    
#ACTIVIDAD 9
    #pido al usuario la magnitud y guardo un float en la variable
magnitud = float(input("Por favor ingrese la magnitud del terremoto: "))
    #imprimo un texto para mayor comprension
print("Segun la escala de Richter la magnitud del terremoto ingresada es: ")
    #comparo todas las posibilidades
if magnitud < 3:
    print("Muy leve (Imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (Ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (Sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")




#ACTIVIDAD 10
    #Pido al usuario su hermisferio y al final coloco la funcion upper para modificar a Mayuscula el input
hemisferio = (input("Porfavor ingrese en que hemisferio se encuentra\n(N = Norte o S = Sur): ")).upper()
    #Guardo como enteros el mes y dia ingresado
mes = int(input("Ingrese el mes en que se encuentra(1-12): "))
dia = int(input("Ingrese el dia del mes en que se encuentra: "))

    #comparo en todas las posibilidades tanto como en hemisferio norte o sur, solo modifico el hemisferio.
if hemisferio == "N" and ((mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20)):
    print("Usted se encuentra en Invierno")
elif hemisferio == "S" and ((mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20)):
    print("Usted se encuentra en Verano")
elif hemisferio == "N" and ((mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20)):
    print("Usted se encuentra en Primavera")
elif hemisferio == "S" and ((mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20)):
    print("Usted se encuentra en Otoño")
elif hemisferio == "N" and ((mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20)):
    print("Usted se encuentra en Verano")
elif hemisferio == "S" and ((mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20)):
    print("Usted se encuentra en Invierno")
elif hemisferio == "N" and ((mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20)):
    print("Usted se encuentra en Otoño")
elif hemisferio == "S" and ((mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20)):
    print("Usted se encuentra en Primavera")
    
    