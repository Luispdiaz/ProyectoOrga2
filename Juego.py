class Juego():
    def __init__(self,modelo,titulo,precio,status):
        self.modelo = modelo
        self.titulo = titulo
        self.precio = precio
        self.status = status

    def database(self):
        data = open("Rent_A_Game.txt", "a")
        data.write(f"{self.modelo},{self.titulo},{self.precio},{self.status}\n")
        print("Se agrego el juego a la base de datos")

    def mostrar(self):
        print(f"Modelo: {self.modelo} \nTitulo: {self.titulo} \nPrecio: {self.precio} \nStatus: {self.status}")
    