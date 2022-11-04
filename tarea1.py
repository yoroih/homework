"""
TAREA 1
Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autor(es). 
Considerar que un libro puede tener varios autores.

Se solicita escribir un programa en Python que permita registrar libros. 
Debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python.

Dicho programa debe tener un menu (a interactuar en la línea de comando) para:

Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
Opción 2: Listar libros.
Opción 3: Agregar libro.
Opción 4: Eliminar libro.
Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
Opción 6: Ordenar libros por título.
Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
Opción 8: Buscar libros por número de autores. 
    Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) 
    y se deben listar todos los libros que contengan 2 autores.
Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
Nota: listar libros involucra: título, género, ISBN, editorial y autor(es)
"""
import pandas as pd
import csv
from csv import DictWriter
from os import system
system("cls")

print("BIBLIOTECA")

class Libro:
    
    libros = ["id","titulo","genero","isbn","editorial","autores"] #columnas del csv 
    
    def __init__(self):
        pass
       
    def leer_archivo(self):
        datos = pd.read_csv("libros.csv")
        #print(datos.sort_values(by="id"))
        print(datos.iloc[0:3])
    
    def listar(self):
        datos = pd.read_csv("libros.csv")
        print(datos.iloc[:,[1,2,3,4,5]])
    
    def eliminar(self):
       
        datos = pd.read_csv("libros.csv")
        print(datos)       
        elim = int(input("\nIngrese id del libro que  desea eliminar: "))
        datos.drop(inplace=True, index = (elim-1))
        print(datos)
        
    
    def ultima_f(self):
        pass
        # datos = pd.read_csv("libros.csv")
        # print(datos)
        # elim = int(input("\nIngrese id del libro que  desea eliminar: "))
        # datos.drop(datos.index[[elim-1]],inplace=True)
        # a = dict(datos)
        # print(a)
        
        # with open("libros.csv","w") as file:
        #     writer = csv.writer(file, delimiter=",")
        #     writer.writerow(list(a))
        # print(datos)
        
        
        
        
        
        # with open("libros.csv", "w") as file:
        #     writer = csv.writer(file)
        #     writer.writerows(datos)
        # print(datos)
        
        
        
    def guardar(self):    
        insert = True
        while insert:
            self.__id = input("Ingrese ID: ")
            self.__titulo = input("Ingresar el titulo del libro: ")
            self.__genero = input("Ingrese genero del libro")
            self.__isbn = input("Ingrese ISBN: ")
            self.__editorial = input("Ingrese editorial: ")
            self.__autores = input("Ingrese autores: ")          
            lib_datos = {"id":self.__id, "titulo":self.__titulo, "genero":self.__genero, "isbn":self.__isbn, "editorial":self.__editorial, "autores":self.__autores}
            with open ('libros.csv','a',newline='') as nueva_linea:
                escribir = DictWriter(nueva_linea, fieldnames=self.libros)
                escribir.writerow(lib_datos)
                nueva_linea.close()
            print()
            if (input("Registrar otro libro? S/N: ")).lower() == "n":
                insert = False
                
    def buscar_isbn_titulo(self):
        #Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
        opcion = "0"
        while not(opcion == "3"):
            print("\nElija una opción\n")
            print("1. Buscar por ISBN")
            print("2. Buscar por Título")
            print("3. Salir\n")
            
            opcion = input("Ingresar opción: ")
                    
            if (opcion == "1"):
                datos = pd.read_csv("libros.csv")
                print(datos.iloc[:,[3]])
                        
            elif (opcion == "2"):
                datos = pd.read_csv("libros.csv")
                print(datos.iloc[:,[1]])
            
            elif (opcion == "3"):
                break
            else:
                print("Ingrese una opción valida")
        
    def buscar_autores(self):
        
        num_autores = int(input("ingrese el numero de autores: "))
        
        datos = pd.read_csv("libros.csv")   
        for i in datos["autores"]:
            a = i.split(",")
            #print(a)
            if len(a) == 1 and num_autores == 1:
                datos.drop(inplace=True, index = (1))
                print(datos)   
            
            # elif len(a) == 2:
            #     print("2 autores")

leer = Libro()
leer.buscar_autores()

        




        
        


    