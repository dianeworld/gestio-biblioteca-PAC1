# ----------------------------------------------
# Projecte 05-11-2025: Gestió de Biblioteca (PAC-1)
# Fitxer: menu.py
# Autors: Oscar Fouz Robles i Diana Urbano Fernández
# Data: 05 Novembre de 2025
# Descripció: - Primer commit
# Mostrar menú senzill per interactuar amb la biblioteca.
# Permet afegir llibres i alumnes per fer préstecs, retorns...
# i consultar la informació desada als fitxers JSON.
# ----------------------------------------------

#imports
import modelo as mo
# from model import biblioteca
# Crear una instància de la biblioteca
# biblio = Biblioteca()



#variables
archiu_carrega_llibres = 'Llibres.csv'
archiu_carrega_socis = 'Socis.csv'
archiu_carrega_moviments = 'catalogo.json'
soci_obj = [] # Socis
llibre_obj = [] # Llibres


# Gestió de directoris
ruta_llibre = mo.carga_ruta(archiu_carrega_llibres)
ruta_soci = mo.carga_ruta(archiu_carrega_socis)
ruta_moviments = mo.carga_ruta(archiu_carrega_moviments)

# Gestió d'escriptura d'arxius
escri = mo.param_archivos('csv','w')
lectu = mo.param_archivos('csv','r')
escri_json = mo.param_archivos('json','w')
lectu_json = mo.param_archivos('json','r')
# afegeix_json = mo.param_archivos('json','r+')

# Carrega inicial
mo.carrega_inicial(ruta_llibre,ruta_soci,escri,lectu)
llibre_obj = mo.llegir_csv_llibres(ruta_llibre,lectu)
soci_obj = mo.llegir_csv_socis(ruta_soci,lectu)


# Funció per mostrar el menú d'opcions
def mostrar_menu():    
    print("\n")
    print("== Catàleg Llibres Biblioteca ===")  # <-- Títol afegit
    print("1. Afegir llibre")
    print("2. Prestar llibre")
    print("3. Retornar llibre")
    print("4. Buscar per títol")
    print("5. Mostrar tots els llibres")
    print("0. Sortir!!!")
    print("\n")


# Funció per llegir l'opció de l'usuari amb gestió bàsica d'errors
def get_option():
    try:
        return int(input("Tria opció: "))
    except ValueError:
        print("\nSi us plau, introdueix un número.")
        return -1  # Opció no vàlida


# Bucle principal del programa
while True:
    mostrar_menu()                          # Mostrar menú cada vegada
    op = get_option()                       # Llegir opció de l'usuari
    mo.borra()
    match op:    
        case 1:
            # Anem a afegir un llibre
            t = input("Títol: ")
            a = input("Autor: ")
            g = input("Genere: ")
            mo.afegir_llibre(t,a,g,llibre_obj)      # Cridar la funció de biblioteca
            

        case 2:
            # Prestar un llibre
            mo.mostrar_llibres(llibre_obj)
            t = input('\nTítol a prestar: ')
            mo.borra()
            mo.mostrar_socis(soci_obj)
            s = input('\nSoci que retorna: ')
            mo.borra()
            mo.prestar_llibre(t,s,llibre_obj,escri_json,ruta_moviments,soci_obj,lectu_json)      # Cridar la funció de biblioteca
            
        case 3:
            # Retornar un llibre
            mo.mostrar_llibres(llibre_obj) # fer una llista dels prestats
            t = input('\nTítol a retornar: ')
            mo.borra()
            mo.mostrar_socis(soci_obj)
            s = input('\nSoci que retorna: ')
            mo.borra()
            mo.retornar_llibre(t,s,llibre_obj,escri_json,ruta_moviments,soci_obj,lectu_json)      # Cridar la funció de biblioteca
        
        case 4:
            # Buscar llibres per autor
            t = input("\nTitol: ")
            mo.buscar_llibre(t,llibre_obj)
        case 5:
            # Mostrar tots els llibres
            mo.mostrar_llibres(llibre_obj)
        case 0:
            # Sortir del programa
            break
        case _:
            print(f'\nL\'opció {op} introduïda no és correcta')

