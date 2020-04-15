print("Bienvenidx a la calculadora de años")
gato = int(input("Ingrese la edad de su gato en años humanos: "))

def calculadora():
    if gato >= 1:
        if gato >= 2:
            edadgato = str(((gato-2)*4)+25)
            return print("La edad en años de gato es: "+edadgato+" años. \nGracias por usar la calculadora.")
        else:
            edadgato = "25"
            return print("La edad en años de su gato es: "+edadgato+" años. \nGracias por usar la calculadora.")
    else:
        edadgato = "15"
        return print("La edad en años de su gato es: "+edadgato+" años. \nGracias por usar la calculadora.")

        
calculadora()