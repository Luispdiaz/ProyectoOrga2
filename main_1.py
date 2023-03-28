from Hash import Hash_Function
from Juego import Juego


def leer(base_de_datos,indices):
    data = open("Rent_A_Game.txt", "r")
    data_1 = open("Index.txt", "r")
    if data.read() == "" and data_1.read() == "":
        base_de_datos = { "primero": [], "segundo": [], "tercero": []}
        indices = {}
    else:
        data = open("Index.txt", "r")
        for x in data:
            i = 0
            indices[x.split(",")[i]] = x.split(",")[i+1],x.split(",")[i+2]

        data = open("Rent_A_Game.txt", "r")
        for x in data:
            for w, y in indices.items():
                i = 0
                juego = Juego(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3])
                if juego.titulo == w:
                    if indices[juego.titulo][0] == "0":
                        base_de_datos["primero"].append(juego)
                    elif indices[juego.titulo][0] == "1":
                        base_de_datos["segundo"].append(juego)           
                    elif indices[juego.titulo][0] == "2":
                        base_de_datos["tercero"].append(juego)
                    elif indices[juego.titulo][0] == "3":
                        base_de_datos["overflow_1"].append(juego)
                    elif indices[juego.titulo][0] == "4":
                        base_de_datos["overflow_2"].append(juego)
                    elif indices[juego.titulo][0] == "5":
                        base_de_datos["overflow_3"].append(juego)
                    elif indices[juego.titulo][0] == "6":
                        base_de_datos["overflow_4"].append(juego)
                    elif indices[juego.titulo][0] == "7":
                        base_de_datos["overflow_5"].append(juego)
                    elif indices[juego.titulo][0] == "8":
                        base_de_datos["overflow_6"].append(juego)

        print(indices)
        print(base_de_datos)            

def registro(base_de_datos,indices):
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

    status = "EN STOCK"

    juego = Juego(modelo,titulo,precio,status)

    hashing = Hash_Function(modelo)
    indice = hashing.Hash_func(modelo)
    print(indice)

    if int(indice) % 3 == 0:
        if len(base_de_datos["primero"]) < 3:
            base_de_datos["primero"].append(juego)
        else:
            if len(base_de_datos["overflow_1"]) < 3:
                base_de_datos["overflow_1"].append(juego)
            else:
                if len(base_de_datos["overflow_2"]) < 3:
                    base_de_datos["overflow_2"].append(juego)
                else:
                    if len(base_de_datos["overflow_3"]) < 3:
                        base_de_datos["overflow_3"].append(juego)
                    else:
                        if len(base_de_datos["overflow_4"]) < 3:
                            base_de_datos["overflow_4"].append(juego)
                        else:
                            if len(base_de_datos["overflow_5"]) < 3:
                                base_de_datos["overflow_5"].append(juego)
                            else:
                                if len(base_de_datos["overflow_6"]) < 3:
                                    base_de_datos["overflow_6"].append(juego)
                                else:
                                    print("Ya no se pueden ingresar mas juegos.")

    elif int(indice) % 3 == 1:
        if len(base_de_datos["segundo"]) < 3:
            base_de_datos["segundo"].append(juego)
        else:
            if len(base_de_datos["overflow_1"]) < 3:
                base_de_datos["overflow_1"].append(juego)
            else:
                if len(base_de_datos["overflow_2"]) < 3:
                    base_de_datos["overflow_2"].append(juego)
                else:
                    if len(base_de_datos["overflow_3"]) < 3:
                        base_de_datos["overflow_3"].append(juego)
                    else:
                        if len(base_de_datos["overflow_4"]) < 3:
                            base_de_datos["overflow_4"].append(juego)
                        else:
                            if len(base_de_datos["overflow_5"]) < 3:
                                base_de_datos["overflow_5"].append(juego)
                            else:
                                if len(base_de_datos["overflow_6"]) < 3:
                                    base_de_datos["overflow_6"].append(juego)
                                else:
                                    print("Ya no se pueden ingresar mas juegos.")
    else:
        if len(base_de_datos["tercero"]) < 3:
            base_de_datos["tercero"].append(juego)
        else:
            if len(base_de_datos["overflow_1"]) < 3:
                base_de_datos["overflow_1"].append(juego)
            else:
                if len(base_de_datos["overflow_2"]) < 3:
                    base_de_datos["overflow_2"].append(juego)
                else:
                    if len(base_de_datos["overflow_3"]) < 3:
                        base_de_datos["overflow_3"].append(juego)
                    else:
                        if len(base_de_datos["overflow_4"]) < 3:
                            base_de_datos["overflow_4"].append(juego)
                        else:
                            if len(base_de_datos["overflow_5"]) < 3:
                                base_de_datos["overflow_5"].append(juego)
                            else:
                                if len(base_de_datos["overflow_6"]) < 3:
                                    base_de_datos["overflow_6"].append(juego)
                                else:
                                    print("Ya no se pueden ingresar mas juegos.")


    for x, y in base_de_datos.items():
        i = 0
        for z in y:
            if titulo == z.titulo:
                indices[titulo] = x,i
            else:
                i += 1

    print(indices)
    


def busqueda(base_de_datos, indices):
    opcion = input("Buscar por: \n1.Modelo \n2.Titulo \n> ")
    while not opcion.isnumeric() or int(opcion) not in range(1,3):
        print("Elija una opcion valida")
        opcion = input("Buscar por: \n1.Modelo \n2.Titulo \n> ")

    if opcion == "1":
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

            for x, y in base_de_datos.items():
                for z in y:
                    if z.modelo == modelo:
                        z.mostrar()
                        encontrado = True
                        break

            if encontrado == True:
                break

    else:
        while True:
            titulo = input("Ingrese el título del juego: ").title()
            while len(titulo) > 10 or not titulo.isalpha() and not titulo.isnumeric():
                print("Error, el título no puede contener mas de 10 caracteres o no puede tener caracteres especiales")
                titulo = input("Ingrese el título del juego: ").title()
            
            for x, y in indices.items():
                if x == titulo:
                    encontrado = True
                    if str(y[0]) == str(0) or str(y[0]) == "primero" :
                        a = "primero"
                        b = y[1]
                    elif str(y[0]) == str(1) or str(y[0]) == "segundo":
                        a = "segundo"
                        b = y[1]
                    elif str(y[0]) == str(2) or str(y[0]) == "tercero":
                        a = "tercero"
                        b = y[1]
                    elif str(y[0]) == str(3) or str(y[0]) == "overflow_1":
                        a = "overflow_1"
                        b = y[1]
                    elif str(y[0]) == str(4) or str(y[0]) == "overflow_2":
                        a = "overflow_2"
                        b = y[1]
                    elif str(y[0]) == str(5) or str(y[0]) == "overflow_3":
                        a = "overflow_3"
                        b = y[1]
                    elif str(y[0]) == str(6) or str(y[0]) == "overflow_4":
                        a = "overflow_4"
                        b = y[1]
                    elif str(y[0]) == str(7) or str(y[0]) == "overflow_5":
                        a = "overflow_5"
                        b = y[1]
                    elif str(y[0]) == str(8) or str(y[0]) == "overflow_6":
                        a = "overflow_6"
                        b = y[1]
                else:
                    encontrado = False

            if encontrado == True:
                base_de_datos[a][int(b)].mostrar()
                break
            else:
                print("No se pudo conseguir el titulo")
                break
                
def alquiler(base_de_datos):
    print(base_de_datos)
    print("Lista de Juegos:\n")
    j = 0
    for x, y in base_de_datos.items():
        for i in range(0, len(y)):
            print(f"Nombre: {y[i].titulo}")
            print(f"Precio: {y[i].precio}")
            print(f"Status: {y[i].status}") 
            j += 1

    titulo = input("Ingrese el título del juego: ").title()
    while len(titulo) > 10 or not titulo.isalpha() and not titulo.isnumeric():
        print("Error, el título no puede contener mas de 10 caracteres o no puede tener caracteres especiales")
        titulo = input("Ingrese el título del juego: ").title()

    for x, y in base_de_datos.items():
        for z in y:
            if z.titulo == titulo:
                z.status = "ALQUILADO"



def devoluciones(base_de_datos):
    print("Lista de Juegos:")
    encontrado = False
    titulos = []
    for x, y in base_de_datos.items():
        for z in y:
            if "\n" in z.status:
                z.status = z.status.replace("\n", "")
                if z.status == "ALQUILADO":
                    encontrado = True
                    z.mostrar()
                    titulos.append(z.titulo)
            else:
                if z.status == "ALQUILADO":
                    encontrado = True
                    z.mostrar()
                    titulos.append(z.titulo)
    
    if encontrado != True:
        print("No hay ningun juego alquilado\n")
    
    else:
        juego_a = input("Introduzca el nombre del juego que desea devolver: ").title()
        while not juego_a.isalpha() or juego_a not in titulos:
            print("Error, introduzca un titulo valido")
            juego_a = input("Introduzca el nombre del juego que desea devolver: ").title()

        for x, y in base_de_datos.items():
            for z in y:
                if z.titulo == juego_a:
                    z.status = "EN STOCK"


def eliminar(base_de_datos):
    print("Lista de Juegos:\n")
    for x, y in base_de_datos.items():
        for i in range(0, len(y)):
            print(f"Nombre: {y[i].titulo}")
            print(f"Precio: {y[i].precio}")
            print(f"Status: {y[i].status}")

    titulo = input("Ingrese el título del juego: ").title()
    while len(titulo) > 10 or not titulo.isalpha() and not titulo.isnumeric():
        print("Error, el título no puede contener mas de 10 caracteres o no puede tener caracteres especiales")
        titulo = input("Ingrese el título del juego: ").title()

    for x, y in base_de_datos.items():
        i = 0
        for z in y:
            if z.titulo == titulo:
                y.pop(int(i))
                print("Juego eliminado")
                break
            else:
                i += 1

def cargar_datos(base_de_datos, indices):
    data = open("Index.txt", "w")
    data.close()
    data = open("Index.txt", "a")
    for x,y in indices.items():
        if y[0] == "primero":
            a = 0
        elif y[0] == "segundo":
            a = 1
        elif y[0] == "tercero":
            a = 2
        elif y[0] == "overflow_1":
            a = 3
        elif y[0] == "overflow_2":
            a = 4
        elif y[0] == "overflow_3":
            a = 5
        elif y[0] == "overflow_4":
            a = 6
        elif y[0] == "overflow_5":
            a = 7
        elif y[0] == "overflow_6":
            a = 8
        
        if "\n" in str(y[1]):
            b = y[1]
            b = b.replace("\n", "")
            data.write(f"{x},{y[0]},{b}\n")
        else:
            data.write(f"{x},{a},{y[1]}\n")

    data = open("Rent_A_Game.txt", "w")
    data.close()

    data = open("Rent_A_Game.txt", "a")
    for x, y in base_de_datos.items():
        for z in y:
            if "\n" in z.status:
                z.status = z.status.replace("\n","")
                z.database()
            else:
                z.database()





base_de_datos = { "primero": [], "segundo": [], "tercero": [], "overflow_1": [], "overflow_2": [], "overflow_3": [], "overflow_4": [], "overflow_5": [], "overflow_6": [] }
indices = {}

def main():
    leer(base_de_datos,indices)
    print("Bienvenido al sistema de registro de Rent - A - Game")
    while True:
        opcion = input("Ingresa la operación que deseas realizar: \n1.Insertar un nuevo juego \n2.Búsqueda de un juego \n3.Alquiler de un juego \n4.Devolución de un juego \n5.Eliminación de un juego \n6.Salir \n> ")
        while not opcion.isnumeric() or int(opcion) not in range(1,7):
            print("Por favor ingrese un número de opción válido")
            opcion = input("Ingresa la operación que deseas realizar: \n>1.Insertar un nuevo juego \n2.Búsqueda de un juego \n3.Alquiler de un juego \n4.Devolución de un juego \n5.Eliminación de un juego \n6.Salir \n> ")
        if opcion == "1":
            registro(base_de_datos,indices)
        elif opcion == "2":
            busqueda(base_de_datos,indices)
        elif opcion == "3":
            alquiler(base_de_datos)
        elif opcion == "4":
            devoluciones(base_de_datos)
        elif opcion == "5":
            eliminar(base_de_datos)
        else:
            cargar_datos(base_de_datos,indices)
            print("VUELVA PRONTO")
            break
main()