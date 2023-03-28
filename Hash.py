import hashlib
class Hash_Function():
    def __init__(self,valor):
        self.valor = valor

    """ Funcion hash """
    def Hash_func(self, valor):
        key = 0
        for i in range(0,len(valor)):
            key += ord(valor[i])
        return key % 3
        
