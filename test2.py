class hola:
    a = 5
    
    def __init__(self, b):
        self.__b = b

    def suma(self):
        z = self.__b + self.__a 
        print(z)

obj = hola
obj.suma()

    