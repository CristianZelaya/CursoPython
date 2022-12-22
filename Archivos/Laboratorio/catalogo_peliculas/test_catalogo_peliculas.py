from dominio.Pelicula import Pelicula
from servicio.CatalogoPelicula import CatalogoPelicula

opcion = None
while opcion != 4:

    try:
        print('Menu'.center(50, '-'))
        print("""
        1. Agregar Pelicula
        2. Listar Peliculas
        3. Eliminar Archivo de Peliculas
        4. Salir
        """)
        opcion = int(input('Ingresa una opcion (1 al 4): '))
    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None

    if opcion == 1:
        print('1. Agregar Pelicula')
        nombre_pelicula = input(f'Nombre de pelicula: ')
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPelicula.agregar_pelicula(pelicula)
        opcion = None
    elif opcion == 2:
        CatalogoPelicula.listar_peliculas()
        opcion = None
    elif opcion == 3:
        print('Eliminando archivo...')
        CatalogoPelicula.eliminar_archivo()
        opcion = None
    elif opcion == 4:
        print('Saliendo...')
        opcion = 4
    else:
        print('Agrega un valor valido...')
        opcion = None


#pelicula = Pelicula('Spiderman')
#pelicula2 = Pelicula('Superman')
#print(pelicula)
#print(pelicula2)

#CatalogoPelicula.agregar_pelicula(pelicula)
#CatalogoPelicula.agregar_pelicula(pelicula2)

#CatalogoPelicula.listar_peliculas()
#CatalogoPelicula.eliminar_archivo()
