from Hash import Hash_Function
from Juego import Juego

""" Modulo de Registro de los juegos """
def registro(base_de_datos, indices):
    contador = 0
    data = open("Rent_A_Game.txt", "r")
    if data.read() == "":
        while True:
            modelo = input("Introduzca el código del modelo: ")
            contador_num = 0
            contador_letra = 0
            for x in modelo:
                if x.isnumeric():
                    contador_num += 1
                elif x.isalpha():
                    contador_letra += 1
            while contador_letra != 6 or contador_num != 2 or (contador_letra + contador_num) != 8:
                print("Error, por favor ingrese un código válido")
                modelo = input("Introduzca el código del modelo: ")
                contador_num = 0
                contador_letra = 0
                for x in modelo:
                    if x.isnumeric():
                        contador_num += 1
                    elif x.isalpha():
                        contador_letra += 1
            break
        titulo = input("Ingrese el título del juego: ").title()
        while len(titulo) > 10 or not titulo.isalpha() and not titulo.isnumeric():
            print("Error, el título no puede contener mas de 10 caracteres o no puede tener caracteres especiales")
            titulo = input("Ingrese el título del juego: ").title() 
        precio = input("Introduzca el precio del juego: ")
        while not precio.isnumeric() or int(precio) not in range(1,1000):
            print("Error, introduzca un precio válido")
            precio = input("Introduzca el precio del juego: ")

        hashing = Hash_Function(modelo)
        codigo = hashing.Hashing(modelo)

        overflow = 0
        status = "EN STOCK"

        data = open("Index.txt", "r")
        for x in data:
            i = 0
            if "\n" in x.split(",")[i+1]:
                x.split(",")[i+1] = x.split(",")[i+1].replace("\n", "")
            indices[x.split(",")[i]] = x.split(",")[i+1]
        indices[titulo] = contador
        data = open("Index.txt", "w")
        data.close()
        data = open("Index.txt", "a")
        for x, y in indices.items():
            titulo = x
            data.write(f"{titulo},{contador}\n")
            contador += 1
        

        juego = Juego(codigo, titulo, precio, status, overflow)
        juego.database()

        if contador < 3:
            base_de_datos["primero"].append(juego)
            contador += 1
        elif contador < 6:
            base_de_datos["segundo"].append(juego)
            contador += 1
        else:
            base_de_datos["tercero"].append(juego)
            contador += 1
    else:
        contador = 0
        print("aqui")
        base_de_datos = { "primero": [], "segundo": [], "tercero": []}
        modelos = []
        titulos = []
        data = open("Rent_A_Game.txt", "r")
        for x in data:
            i = 0
            if "\n" in x.split(",")[i+4]:
                x.split(",")[i+4] = x.split(",")[i+4].replace(",", "")
            modelos.append(x.split(",")[i])
            titulos.append(x.split(",")[i+1])
            juego = Juego(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4])
            if contador <= 3:
                base_de_datos["primero"].append(juego)
                contador += 1
            elif contador <= 6:
                base_de_datos["segundo"].append(juego)
                contador += 1
            else:
                base_de_datos["tercero"].append(juego)
                contador += 1
        while True:
            modelo = input("Introduzca el código del modelo: ")
            contador_num = 0
            contador_letra = 0
            for x in modelo:
                if x.isnumeric():
                    contador_num += 1
                elif x.isalpha():
                    contador_letra += 1
            while contador_letra != 6 or contador_num != 2 or (contador_letra + contador_num) != 8:
                print("Error, por favor ingrese un código válido")
                modelo = input("Introduzca el código del modelo: ")
                contador_num = 0
                contador_letra = 0
                for x in modelo:
                    if x.isnumeric():
                        contador_num += 1
                    elif x.isalpha():
                        contador_letra += 1
            hashing = Hash_Function(modelo)
            codigo = hashing.Hashing(modelo)
            encontrado = False
            for x in modelos:
                if codigo == x:
                    encontrado = True
                    break
            if encontrado != True:
                break
            else:
                print("Error, el codigo ya existe")

        while True:
            titulo = input("Ingrese el título del juego: ").title()
            while len(titulo) > 10 or not titulo.isalpha() and not titulo.isnumeric():
                print("Error, el título no puede contener mas de 10 caracteres o no puede tener caracteres especiales")
                titulo = input("Ingrese el título del juego: ").title() 
            

            encontrado = False
            print(titulos)
            for x in titulos:
                if x == titulo:
                    encontrado = True
                    break
            if encontrado != True:
                break
            else:
                print("Error, el titulo ya existe")

        precio = input("Introduzca el precio del juego: ")
        while not precio.isnumeric() or int(precio) not in range(1,1000):
            print("Error, introduzca un precio válido")
            precio = input("Introduzca el precio del juego: ")
                    
        hashing = Hash_Function(modelo)
        codigo = hashing.Hashing(modelo)

        overflow = 0
        status = "EN STOCK"

        data = open("Index.txt", "r")
        indices = {}
        for x in data:
            i = 0
            if "\n" in x.split(",")[i+1]:
                x.split(",")[i+1] = x.split(",")[i+1].replace("\n", "")
            indices[x.split(",")[i]] = x.split(",")[i+1]
            indices[x.split(",")[i]] = x.split(",")[i+1]
        indices[titulo] = contador
        data = open("Index.txt", "w")
        data.close()
        data = open("Index.txt", "a")
        contador_i = 0
        for x, y in indices.items():
            titulo = x
            data.write(f"{titulo},{contador_i}\n")
            contador_i += 1

        juego = Juego(codigo, titulo, precio, status, overflow)
        juego.database()
        if contador < 3:
            base_de_datos["primero"].append(juego)
            contador += 1
        elif contador < 6:
            base_de_datos["segundo"].append(juego)
            contador += 1
        else:
            base_de_datos["tercero"].append(juego)
            contador += 1

""" Modulo de busqueda de juegos """
def buscar(base_de_datos):
    opcion = input("Buscar por: \n1.Modelo \n2.Titulo \n> ")
    while not opcion.isnumeric() or int(opcion) not in range(1,3):
        print("Elija una opcion valida")
        opcion = input("Buscar por: \n1.Modelo \n2.Titulo \n> ")

    if opcion == "1":
        contador = 1
        data = open("Rent_A_Game.txt", "r")
        for x in data:
            i = 0
            if "\n" in x.split(",")[i+4]:
                x.split(",")[i+4] = x.split(",")[i+4].replace(",", "")
            juego = Juego(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4])
            if contador <= 3:
                base_de_datos["primero"].append(juego)
                contador += 1
            elif contador <= 6:
                base_de_datos["segundo"].append(juego)
                contador += 1
            else:
                base_de_datos["tercero"].append(juego)
                contador += 1
        while True:
            contador_num = 0
            contador_letra = 0
            modelo = input("Introduzca el código del modelo: ")
            for x in modelo:
                if x.isnumeric():
                    contador_num += 1
                elif x.isalpha():
                    contador_letra += 1
            while contador_letra != 6 or contador_num != 2 or (contador_letra + contador_num) != 8:
                print("Error, por favor introduzca un modelo valido")
                contador_num = 0
                contador_letra = 0
                modelo = input("Introduzca el código del modelo: ")
                for x in modelo:
                    if x.isnumeric():
                        contador_num += 1
                    elif x.isalpha():
                        contador_letra += 1
                

            hashing = Hash_Function(modelo)
            codigo = hashing.Hashing(modelo)

            encontrado = False
            for x, y in base_de_datos.items():
                for i in range(0, len(y)):
                    if codigo == y[i].modelo:
                        y[i].mostrar()
                        encontrado = True
            
            if encontrado != True:
                print("Error, no existe el modelo en la base de datos")
                opcion = input("Desea salir: \n1.Si \n2.No \n> ")
                while not opcion.isnumeric() or int(opcion) not in range(1,3):
                    opcion = input("Desea salir: \n1.Si \n2.No \n> ")
                if opcion == "1":
                    break
            else:
                break 
    else:
        base_de_datos = { "primero": [], "segundo": [], "tercero": []}
        contador = 1
        data = open("Rent_A_Game.txt", "r")
        for x in data:
            i = 0
            if "\n" in x.split(",")[i+4]:
                x.split(",")[i+4] = x.split(",")[i+4].replace(",", "")
            juego = Juego(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4])
            if contador <= 3:
                base_de_datos["primero"].append(juego)
                contador += 1
            elif contador <= 6:
                base_de_datos["segundo"].append(juego)
                contador += 1
            else:
                base_de_datos["tercero"].append(juego)
                contador += 1

        print(base_de_datos)

        while True:
            titulo = input("Ingrese el título del juego: ").title()
            while len(titulo) > 10 or not titulo.isalpha() and not titulo.isnumeric():
                print("Error, el título no puede contener mas de 10 caracteres o no puede tener caracteres especiales")
                titulo = input("Ingrese el título del juego: ").title()
            
            data = open("Rent_A_Game.txt", "r")
            encontrado = False
            for x in data:
                print(x.split(",")[i+1])
                i = 0
                if x.split(",")[i+1] == titulo:
                    encontrado = True

            if encontrado != True:
                print("Error, no se encontro el titulo del juego")
            else:
                break
        
        data = open("Index.txt", "r")
        for x in data:
            i = 0
            if  x.split(",")[i] == titulo:
                if "\n" in x.split(",")[i+1]:
                    indice = x.split(",")[i+1].replace("\n", "")
        
        for x, y in base_de_datos.items():
            print(indice)
            juego_e = y[int(indice)]
            juego_e.mostrar()
            break
""" Modulo de alquiler de juegos """
def alquiler(base_de_datos):
    base_de_datos = { "primero": [], "segundo": [], "tercero": []}
    contador = 1
    data = open("Rent_A_Game.txt", "r")
    for x in data:
        i = 0
        if "\n" in x.split(",")[i+4]:
            x.split(",")[i+4] = x.split(",")[i+4].replace(",", "")
        juego = Juego(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4])
        if contador <= 3:
            base_de_datos["primero"].append(juego)
            contador += 1
        elif contador <= 6:
            base_de_datos["segundo"].append(juego)
            contador += 1
        else:
            base_de_datos["tercero"].append(juego)
            contador += 1
    print("Lista de Juegos:\n")
    for x, y in base_de_datos.items():
        for i in range(0, len(y)):
            print(f"---------{i+1}--------")
            print(f"Nombre: {y[i].titulo}")
            print(f"Precio: {y[i].precio}")
            print(f"Status: {y[i].status}\n")

    juego_a = input("Introduzca el numero del juego que desea alquilar: ")
    while not juego_a.isnumeric() or int(juego_a) > i+1:
        print("Error, introduzca un indice valido")
        juego_a = input("Introduzca el numero del juego que desea alquilar: ")

    for x, y in base_de_datos.items():
        for i in range(0, len(y)):
            y[int(juego_a)-1].status = "ALQUILADO"
    
    data = open("Rent_A_Game.txt", "w")
    data.close()

    for x, y in base_de_datos.items():
        for i in range(0,len(y)):
            if "\n" in y[i].overflow:
                y[i].overflow = y[i].overflow.replace("\n", "")
                juego = Juego(y[i].modelo,y[i].titulo, y[i].precio,y[i].status,y[i].overflow)
                juego.database()
            else:
                juego = Juego(y[i].modelo,y[i].titulo, y[i].precio,y[i].status,y[i].overflow)
                juego.database()

""" Modulo de devoluciones de juegos """
def devolucion(base_de_datos):
    base_de_datos = { "primero": [], "segundo": [], "tercero": []}
    contador = 1
    data = open("Rent_A_Game.txt", "r")
    for x in data:
        i = 0
        if "\n" in x.split(",")[i+4]:
            x.split(",")[i+4] = x.split(",")[i+4].replace(",", "")
        juego = Juego(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4])
        if contador <= 3:
            base_de_datos["primero"].append(juego)
            contador += 1
        elif contador <= 6:
            base_de_datos["segundo"].append(juego)
            contador += 1
        else:
            base_de_datos["tercero"].append(juego)
            contador += 1
    
    print("Lista de Juegos:")
    encontrado = False
    titulos = []
    for x, y in base_de_datos.items():
        for i in range(0, len(y)):
            if y[i].status == "ALQUILADO":
                encontrado = True
                print(f"Nombre: {y[i].titulo}")
                print(f"Precio: {y[i].precio}")
                print(f"Status: {y[i].status}\n")
                titulos.append(y[i].titulo)
    
    if encontrado != True:
        print("No hay ningun juego alquilado\n")
    
    else:
        juego_a = input("Introduzca el nombre del juego que desea devolver: ").title()
        while not juego_a.isalpha() or juego_a not in titulos:
            print("Error, introduzca un titulo valido")
            juego_a = input("Introduzca el nombre del juego que desea devolver: ").title()

        for x, y in base_de_datos.items():
            for i in range(0, len(y)):
                if y[i].titulo == juego_a:
                    y[i].status = "EN STOCK"
        
        data = open("Rent_A_Game.txt", "w")
        data.close()

        for x, y in base_de_datos.items():
            for i in range(0,len(y)):
                if "\n" in y[i].overflow:
                    y[i].overflow = y[i].overflow.replace("\n", "")
                    juego = Juego(y[i].modelo,y[i].titulo, y[i].precio,y[i].status,y[i].overflow)
                    juego.database()
                else:
                    juego = Juego(y[i].modelo,y[i].titulo, y[i].precio,y[i].status,y[i].overflow)
                    juego.database()   

""" Modulo de eliminar juegos """
def eliminar(base_de_datos):
    base_de_datos = { "primero": [], "segundo": [], "tercero": []}
    contador = 1
    data = open("Rent_A_Game.txt", "r")
    for x in data:
        i = 0
        if "\n" in x.split(",")[i+4]:
            x.split(",")[i+4] = x.split(",")[i+4].replace(",", "")
        juego = Juego(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4])
        if contador <= 3:
            base_de_datos["primero"].append(juego)
            contador += 1
        elif contador <= 6:
            base_de_datos["segundo"].append(juego)
            contador += 1
        else:
            base_de_datos["tercero"].append(juego)
            contador += 1
    print("Lista de Juegos:\n")
    for x, y in base_de_datos.items():
        for i in range(0, len(y)):
            print(f"---------{i+1}--------")
            print(f"Nombre: {y[i].titulo}")
            print(f"Precio: {y[i].precio}")
            print(f"Status: {y[i].status}\n")

    juego_e = input("Introduzca el numero del juego que desea eliminar: ")
    while not juego_e.isnumeric() or int(juego_e) > i+1:
        print("Error, introduzca un indice valido")
        juego_e = input("Introduzca el numero del juego que desea alquilar: ")

    for x, y in base_de_datos.items():
        for z in y:
            y.pop(int(juego_e)-1)
            print("Juego eliminado")
            break
    data = open("Index.txt", "w")
    data.close()
    data = open("Index.txt", "a")
    contador = 0
    for x, y in base_de_datos.items():
        for z in y:
            titulo = z.titulo
            data.write(f"{titulo}, {contador}\n")
            contador += 1
            
    data = open("Rent_A_Game.txt", "w")
    data.close()
    for x, y in base_de_datos.items():
        for i in range(0,len(y)):
            if "\n" in y[i].overflow:
                y[i].overflow = y[i].overflow.replace("\n", "")
                juego = Juego(y[i].modelo,y[i].titulo, y[i].precio,y[i].status,y[i].overflow)
                juego.database()
            else:
                juego = Juego(y[i].modelo,y[i].titulo, y[i].precio,y[i].status,y[i].overflow)
                juego.database()



base_de_datos = { "primero": [], "segundo": [], "tercero": []}
indices = {}

""" Modulo Main """
def main():
    print("Bienvenido al sistema de registro de Rent - A - Game")
    print()
    while True:
        opcion = input("Ingresa la operación que deseas realizar: \n1.Insertar un nuevo juego \n2.Búsqueda de un juego \n3.Alquiler de un juego \n4.Devolución de un juego \n5.Eliminación de un juego \n6.Salir \n>")
        while not opcion.isnumeric() or int(opcion) not in range(1,7):
            print("Por favor ingrese un número de opción válido")
            opcion = input("Ingresa la operación que deseas realizar: \n>1.Insertar un nuevo juego \n2.Búsqueda de un juego \n3.Alquiler de un juego \n4.Devolución de un juego \n5.Eliminación de un juego \n6.Salir \n> ")
        if opcion == "1":
            registro(base_de_datos,indices)
        elif opcion == "2":
            buscar(base_de_datos)
        elif opcion == "3":
            alquiler(base_de_datos)
        elif opcion == "4":
            devolucion(base_de_datos)
        elif opcion == "5":
            eliminar(base_de_datos)
        else:
            break
main()