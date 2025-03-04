"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import sys
import controller
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
dataFolder = "GoodReads"


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def printMenu():
    print("Opciones:")
    print("1- Cargar Libros")
    print("2- Cargar Tags")
    # TODO: Modificaciones lab 1, agregar opcion 3.
    print("3- Cargar Libros con tags")
    print("0- Salir")


def loadBooks(control):
    """
    Carga los libros
    """
    books = controller.loadBooks(control,
                                 "GoodReads/books-small.csv")
    return books


def loadTags(control):
    """
    Carga los Tags
    """
    tags = controller.loadTags(control,
                               "GoodReads/tags.csv")
    return tags


def loadBooksTags(control):
    """
    Cargar los Tags de libros
    """
    booksTags = controller.loadBooksTags(control,
                                         "GoodReads/book_tags-small1.csv")
    return booksTags


# Se crea el controlador asociado a la vista
control = newController()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input("Seleccione una opción para continuar\n")
    if int(inputs[0]) == 1:
        print("Cargando información de libros....")
        books = loadBooks(control)
        print("Total de libros cargados: " + str(books))

    elif int(inputs[0]) == 2:
        print("Cargando información de tags....")
        tags = loadTags(control)
        print("Total de tags cargados: " + str(tags))

    # TODO: Modificaciones lab 1, agregar la opcion 3, ladBookTags().
    elif int(inputs[0])==3:
        print("Cargando información de libros con tags...")
        booksTags=loadBooksTags(control)
        print("Total de libros con tags cargados: "+str(booksTags))
    else:
        sys.exit(0)
sys.exit(0)
