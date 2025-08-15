#Ejercicio 1
print("Hola Mundo!")



#Ejercicio 2
nombre = input("Porfavor ingresa tu nombre! ")
print (f"Hola {nombre}!")



#Ejercicio 3
nombre = input("Bienvenido! Por favor ingresa tu nombre: ")
apellido = input("Ahora tu apellido: ")
edad = input("A continuacion ingresa tu edad: ")
lugar = input("Por ultimo, ingresa de donde eres: ")
edad = int(edad)
print (f"Gracias por ingresar tus datos! Ahora sabemos que eres {nombre} {apellido} tienes {edad} años y eres de {lugar}!")



#Ejercicio 4
radio = input("Ingresa por favor el radio del circulo: ")
radio = int(radio)
pi = 3.14
area = pi * radio ** 2
perimetro = 2 * pi * radio
print (f"Cuando el radio del circulo vale {radio} el area es de {area} y el perimetro es de {perimetro:.2f}")



#Ejercicio 5
segundos = input("Por favor ingrese una cantidad de segundos para representarlo en horas ")
segundos = int(segundos)
minutos = segundos / 60
horas = minutos / 60
redondeo = round(horas)
if segundos < 3600:
    print (f"no alcanzan los segundos para representarlo en horas")
else:
    print (f"La cantidad de segundos equivale a {horas:.2f}hs")



#Ejercicio 6
num = input("Por favor ingrese un numero para saber su tabla de multiplicar ")
num = int(num)
print(num * 1)
print(num * 2)
print(num * 3)
print(num * 4)
print(num * 5)
print(num * 6)
print(num * 7)
print(num * 8)
print(num * 9)
print(num * 10)



#Ejercicio 7
while True:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))    
    if num1 == 0 and num2 == 0:
        print("Por favor ingrese un número mayor a cero")
    else:
        break
    
print(num1 + num2)
print(num1 / num2)
print(num1 * num2)
print(num1 - num2)


#Ejercicio 8
altura = int(input("Porfavor ingrese su altura en centimetros: "))
altura = float(altura / 100)

peso = int(input("Por favor ingrese su peso: "))
imc = int(peso / (altura ** 2))
print(f"Su indice de masa corporal es de: {imc}")



#Ejercicio 9 
temp = input("Por favor ingrese la temperatura en grados Celsius: ")
temp = float(temp)
Faren = (9/5) * temp + 32
print(f"{temp} grados Celsius equivalen a {Faren} grados Fahrenheit")



#Ejercicio 10
num1 = float(input("Porfavor ingresa el primer numero: "))
num2 = float(input("Porfavor ingresa el segundo numero: "))
num3 = float(input("Porfavor ingresa el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los numeros ingresados es de: {promedio:.2f}")