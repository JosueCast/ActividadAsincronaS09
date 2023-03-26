


follow = "true"


while follow == "true":
    print("==============================================")
    print("BIENVENIDO AL PROGRAMA DEL GRUPO LOS MEJORES")
    print("==============================================\n")
    # Solicitando los datos al usuario
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo (F para femenino, M para masculino): ").upper()

    # Mostrando los datos ingresados
    print("Los datos ingresados son:")
    print("Nombre completo:", nombre, apellido)
    print("Edad:", edad)
    if sexo == "M" or sexo == "MASCULINO":
        print("Sexo:", "Masculino")
    else:
        print("Sexo:", "Femenino")

    # Determinando la etapa de vida según la edad ingresada
    if edad <= 2:
        print("El usuario se encuentra en la etapa de bebé")
    elif edad <= 5:
        print("El usuario se encuentra en la etapa de infancia")
    elif edad <= 11:
        print("El usuario se encuentra en la etapa de niñes")
    elif edad <= 18:
        print("El usuario se encuentra en la etapa de adolescencia")
    elif edad <= 26:
        print("El usuario se encuentra en la etapa de juventud")
    elif edad <= 40:
        print("El usuario se encuentra en la etapa de adultez joven")
    elif edad <= 55:
        print("El usuario se encuentra en la etapa de adultez")
    elif edad <= 65:
        print("El usuario se encuentra en la etapa de persona mayor")
    else:
        print("El usuario se encuentra en la etapa de tercera edad")

    # Determinando si la edad es par o impar
    if edad % 2 == 0:
        print("La edad ingresada es par")
    else:
        print("La edad ingresada es impar")
  
  
    print("Quiere seguir ingresando usuarios Si - No")
    resp = input("Ingrese su respuesta:   ").upper()
    if resp == "SI":
        follow = "true"
    else:
        follow = "false"
    
    

# Mostrando mensaje de finalización del programa
print("Programa terminado :(")
