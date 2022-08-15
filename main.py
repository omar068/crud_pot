from persona import Persona
from cliente import Cliente


name = input("Ingrese el nombre de la persona: ")
cc = input("Ingrese el número de cédula: ")
age = int(input("Ingrese la edad: "))
address = input("Ingrese la dirección: ")
email = input("Ingrese su correo electrónico: ")
Cliente(name, age, email, address, cc)
Cliente.ToString()
cedula = input("Ingrese el número de cedula a modificar: ")
Cliente.update_cliente(cedula)
print("----------------------")
Cliente.ToString()