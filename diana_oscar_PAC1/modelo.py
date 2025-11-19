
#Imports
import csv
import json
import os
from pathlib import Path

#Clases

class Llibre:
    def __init__(self, titul, autor, genere):
        self.titul = titul
        self.autor = autor
        self.genere = genere
        self.prestado_a = 'Disponible'  

    def prestar_a(self, nom_soci):
        self.prestado_a = nom_soci

    def retornar(self):
        self.prestado_a = 'Disponible'

    def __str__(self):
        return f'{self.titul} ({self.autor}, {self.genere}) - {self.prestado_a}'
        

class Soci:
    def __init__(self,nom):
        self.nom = nom
    
    def __str__(self):
        return f'{self.nom}'


# Funcions generiques

# Limpieza consola
def borra():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

def param_archivos(exten,tipo):
        """
        Función que genera diccionario para las aperturas de ficheros 
        Parametros:
            - exten: tipo de fichero que se va a tratar
            - tipo: 'W'- escritura 'R'- lectura
        Retorno
            - diccionario con los parámetros de una apertura de fichero
        """
        codigo = 'utf-8'
        if exten == 'csv':
            return {
                'mode': tipo,
                'newline': '',
                'encoding': codigo
                }
        elif exten == 'txt':
            return {
                'mode': tipo,
                'encoding': codigo
                }  
        elif exten == 'json':
            return {
                'mode': tipo,
                'encoding': codigo
                }   

def carga_ruta(archivo):
    # Obtiene el directorio actual donde se ejecuta el script
    dir_actual = Path(__file__).parent
    # Construye la ruta deseada
    ruta = Path(dir_actual) / 'datos' / archivo
    ruta.parent.mkdir(exist_ok=True)  # crea la carpeta 'datos' si no existe en el raiz
    return ruta

# Funcions projecte
def carrega_inicial(ruta_llibre,ruta_soci,escri,lectu):
    """
    Funció que anomena a les funcions
        · carrega_*csv_*llibres(ruta_*llibre,escri)
        · carrega_*csv_*socis(ruta_*soci,escri)
        per a la càrrega incial de dades necessàries per al programa
    Paràmetres:
        - ruta_llibre: ruta de l'arxiu dels llibres
        - ruta_soci: ruta de l'arxiu dels socis
        - escri: paràmetres necessaris per a obrir
        arxiu en mode escriptura
    Retorn:
        - Sense retorn
    """
    carrega_csv_llibres(ruta_llibre,escri)
    carrega_csv_socis(ruta_soci,escri)
    llegir_csv_llibres(ruta_llibre,lectu)
    llegir_csv_socis(ruta_soci,lectu)


def carrega_csv_llibres(ruta,escri):
    """
        Funció que escriu un csv per a càrrega inicial
        Paràmetres:
        - ruta: ruta de l'arxiu
        - escri: paràmetres necessaris per a obrir
                 arxiu en mode escriptura
        Retorn
        - Sense retorn, escriu arxiu
    """        
    # definición de la lista de libros
    llibres = [
                ["Cien años de soledad", "Gabriel García Márquez", "Realismo mágico"],
                ["1984", "George Orwell", "Distopía"],
                ["Orgullo y prejuicio", "Jane Austen", "Romántico"],
                ["El nombre de la rosa", "Umberto Eco", "Misterio histórico"],
                ["Crónica del pájaro que da cuerda al mundo", "Haruki Murakami", "Ficción surrealista"],
                ["La sombra del viento", "Carlos Ruiz Zafón", "Misterio"],
                ["El alquimista", "Paulo Coelho", "Fábula espiritual"],
                ["Los pilares de la Tierra", "Ken Follett", "Histórico"],
                ["La carretera", "Cormac McCarthy", "Post-apocalíptico"],
                ["El gran Gatsby", "F. Scott Fitzgerald", "Clásico"],
                ["La tregua", "Mario Benedetti", "Romántico"],
                ["Tokio Blues", "Haruki Murakami", "Drama"],
                ["El guardián entre el centeno", "J.D. Salinger", "Juvenil"],
                ["La metamorfosis", "Franz Kafka", "Existencialismo"],
                ["Rayuela", "Julio Cortázar", "Experimental"],
                ["Matar a un ruiseñor", "Harper Lee", "Drama social"],
                ["El retrato de Dorian Gray", "Oscar Wilde", "Ficción gótica"],
                ["La ladrona de libros", "Markus Zusak", "Histórico juvenil"],
                ["El señor de los anillos", "J.R.R. Tolkien", "Fantasía épica"],
                ["Juego de tronos", "George R.R. Martin", "Fantasía"],
                ["La chica del tren", "Paula Hawkins", "Thriller psicológico"],
                ["La mujer habitada", "Gioconda Belli", "Feminismo"],
                ["El código Da Vinci", "Dan Brown", "Misterio"],
                ["La casa de los espíritus", "Isabel Allende", "Realismo mágico"],
                ["El psicoanalista", "John Katzenbach", "Thriller"],
                ["El perfume", "Patrick Süskind", "Ficción histórica"],
                ["La isla bajo el mar", "Isabel Allende", "Histórico"],
                ["La elegancia del erizo", "Muriel Barbery", "Filosófico"],
                ["La invención de Morel", "Adolfo Bioy Casares", "Ciencia ficción"],
                ["El túnel", "Ernesto Sabato", "Psicológico"],
                ["La ciudad y los perros", "Mario Vargas Llosa", "Realismo social"],
                ["La pasión según G.H.", "Clarice Lispector", "Existencialismo"],
                ["La historia interminable", "Michael Ende", "Fantasía"],
                ["El hereje", "Miguel Delibes", "Histórico"],
                ["La fórmula preferida del profesor", "Yoko Ogawa", "Ficción matemática"],
                ["La mujer de papel", "Rabih Alameddine", "Metaficción"],
                ["El lector", "Bernhard Schlink", "Drama histórico"],
                ["La muerte lenta de Luciana", "Guillermo Martínez", "Misterio"],
                ["La biblioteca de los muertos", "Glenn Cooper", "Thriller histórico"],
                ["El tiempo entre costuras", "María Dueñas", "Romántico histórico"]
            ]

    # escriptura de l'arxiu de llibres
    with ruta.open(**escri) as f:
        writer = csv.writer(f,)
        writer.writerow(["títol","autor","gènere"])
        writer.writerows(llibres)
    

def carrega_csv_socis(ruta,escri):
    """
        Funció que escriu un csv per a càrrega inicial
        Paràmetres:
        - ruta: ruta de l'arxiu
        - escri: paràmetres necessaris per a obrir
                 arxiu en mode escriptura
        Retorn
        - Sense retorn, escriu arxiu
    """        
    # definiciò de la llista de llibres
    socis = [
                ["Alex"],
                ["Germán"],
                ["Adeel"],
                ["Xabi"],
                ["Franco"],
                ["Nacho"],
                ["Mary"],
                ["Arnau"],
                ["Andreu"],
                ["Diana"],
                ["Óscar"],
                ["Carlos"],
                ["José Francisco"],
                ["Mamá de Mary"]
            ]

    # escriptura de l'arxiu de socis
    with ruta.open(**escri) as f:
        writer = csv.writer(f,)
        writer.writerow(['nombre'])
        writer.writerows(socis)
    

def  llegir_csv_llibres(ruta_llibre,lectu):
    """
    Funció que llegeix un CSV i crea objectes Llibre
    Paràmetres:
    - ruta_llibre: ruta de l'arxiu
    - escri: paràmetres necessaris per a obrir l'arxiu
    Retorn:
    - Llista d'objectes Llibre
    """
    llibres_obj = []

    with ruta_llibre.open(**lectu) as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la capçalera
        for fila in reader:
            if len(fila) == 3:
                titul, autor, genere = fila
                llibre = Llibre(titul, autor, genere)
                llibres_obj.append(llibre)

    return llibres_obj
    
    
def llegir_csv_socis(ruta_soci,lectu):
    """
    Funció que llegeix un CSV i crea objectes Soci
    Paràmetres:
    - ruta_soci: ruta de l'arxiu
    - escri: paràmetres necessaris per a obrir l'arxiu
    Retorn:
    - Llista d'objectes soci
    """
    soci_obj = []

    with ruta_soci.open(**lectu) as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la capçalera
        for fila in reader:
            if len(fila) == 1:
                nom = fila[0]
                soci = Soci(nom)
                soci_obj.append(soci)

    return soci_obj

def registrar_moviment(soci, llibre, accio, ruta_moviments, escri_json,lectu_json):
    """
    Registra un moviment en el fitxer catalogo.json
    Paràmetres:
        - soci: nom del soci (o 'Nova compra')
        - llibre: títol del llibre
        - accio: acció realitzada ('préstec', 'retorn', 'adquisició')
    Return: Afegir línia a arxiu
    """
    moviment = {
        'soci': soci,
        'llibre': llibre,
        'accio': accio
    }

    # # Si el fitxer no existeix
    # with ruta_moviments.open(**escri_json) as f:
    #     json.dump([moviment],f,ensure_ascii= False,indent=3)

    try:
        # Intentar llegir el fitxer existent
        with ruta_moviments.open(**lectu_json) as f:
            dades = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si no existeix o està buit/corrupt, començar amb llista nova
        dades = []

    # Afegir el nou moviment
    dades.append(moviment)

    # Escriure la llista actualitzada
    with ruta_moviments.open(**escri_json) as f:
        json.dump(dades, f, ensure_ascii=False, indent=3)
        

def mostrar_llibres(llibre_obj):
    """
    Funció: Funció que pinta la llista de llibres
    Paràmetres: llibre_obj - lllista d'objectes llibre
    Return: sense retorn
    """       
    # print(f'\nTots els llibres:')
    # for l in llibre_obj:
    #     print(l)  # gràcies al __str__ personalitzat
    # Calcular longitud màxima de cada columna
    max_titul = max(len(l.titul) for l in llibre_obj)
    max_autor = max(len(l.autor) for l in llibre_obj)
    max_genere = max(len(l.genere) for l in llibre_obj)
    max_prestat = max(len(l.prestado_a) for l in llibre_obj)

    # Imprimir capçalera
    print("\nTítol".ljust(max_titul), "Autor".ljust(max_autor), "Génere".ljust(max_genere), "Prestat".ljust(max_prestat))
    print("=" * max_titul, "=" * max_autor, "=" * max_genere, "=" * max_prestat)

    # Imprimir cada llibre
    for l in llibre_obj:
        print(
            l.titul.ljust(max_titul),
            l.autor.ljust(max_autor),
            l.genere.ljust(max_genere),
            l.prestado_a.ljust(max_prestat)
        )

def mostrar_socis(soci_obj):
    """
    Funció: Funció que pinta la llista de socis
    Paràmetres: soci_obj - lllista d'objectes soci
    Return: sense retorn
    """    
    print('\nLlista de socis:')
    for s in soci_obj:
        print(s)  # gràcies al __str__ personalitzat

def afegir_llibre(titul, autor, genere,libres_obj):
    """
    Funció: Funció que crea un llibre(objecte) i ho afegeix a la llista
    Paràmetres: titol - títol del llibre
                autor - autor del llibre
                gènere: gènere del llibres
    Return: sense retorn
    """
    llibre = Llibre(titul, autor, genere)
    libres_obj.append(llibre)

def buscar_llibre(titol,llibres_obj):
    """
    Funció: Funció que busca un llibres per t´titol
    Paràmetres: titol - títol del llibre
                soci - sòcia al qual se li presta el llibre
                llibres_*obj: llista de llibres
    Return: sense retorn
    """        
    si = False
    for l in llibres_obj:
        if l.titul.lower() == titol.lower():
            si =True
            break
    if si:
        print(l)
    else:
        print(f"El llibre amb títol {titol} no s'ha trobat" )


def valida_soci(soci,socis_obj):
    """
    Funció: Funció que valida si existeix un soci
    Paràmetres: titol - títol del llibre
                soci - nom del soci a validar
                socis_obj: llista de socis
    Return: sense retorn
    """               
    valida = True
    if not any(s.nom.lower() == soci.lower() for s in socis_obj):
        valida = False
        print(f'\nEl soci introduït "{soci}" no està inclòs.')
    return valida

def prestar_llibre(titol, soci,llibres_obj,escri_json,ruta_moviments,socis_obj,lectu_json):
    """
    Funció: Funció que fa el prestamo de llibres
    Paràmetres: titol - títol del llibre
                soci - sòcia al qual se li presta el llibre
                llibres_obj: llista de llibres
    Return: llibres_*obj
    """
    valida = valida_soci(soci,socis_obj)

    if valida:
    # Cerca del llibre
        for l in llibres_obj:
            if l.titul.lower() == titol.lower():
                if l.prestado_a == 'Disponible':
                    l.prestar_a(soci)
                    registrar_moviment(soci, titol, 'préstec', ruta_moviments, escri_json, lectu_json)
                    print(f'Llibre "{titol}" prestat a {soci}.')
                else:
                    print(f'\nEl llibre "{titol}" ja està prestat a {l.prestado_a}.')
                return

        print(f'\nEl llibre "{titol}" no existeix.')
    return llibres_obj

def retornar_llibre(titol, soci,llibres_obj,escri_json,ruta_moviments,socis_obj,lectu_json):
    """
    Funció: Funció que fa la devolució de llibres
    Paràmetres: titol - títol del llibre
                soci - soci al qual se li presta el llibre
                llibres_*obj: llista de llibres
    Return: llibres_*obj
    """    
    valida = valida_soci(soci,socis_obj)

    if valida:   
        for l in llibres_obj:
            if l.titul.lower() == titol.lower():
                if l.prestado_a == soci:
                    l.retornar()
                    registrar_moviment(soci, titol, 'retorn', ruta_moviments, escri_json, lectu_json)
                    print(f'Llibre "{titol}" retornat per {soci}.')
                else:
                    print(f'El llibre "{titol}" no està registrat com prestat a {soci}.')
                return

        print(f'El llibre "{titol}" no existeix.')
    return llibres_obj


