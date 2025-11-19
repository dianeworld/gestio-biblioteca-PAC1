## PROJECTE PAC-1: GESTIÓ DE BIBLIOTECA I SOCIS

Fitxer principal: main.py
Fitxer model: model.py
Fitxer de Dades: cataleg.json
Autors: Oscar Fouz Robles i Diana Urbano Fernández
Data: *05-06 Novembre 2025 (10h Total)*

## Nom de participants

**Oscar Fouz Robles**
**Diana Urbano Fernández**

## Descripció del projecte

Gestió bàsica de biblioteca amb menú de text.Permet:

- Afegir llibres i socis
- Prestar i retornar llibres
- Consultar informació guardada a `cataleg.json`
- Buscar llibres per autor
- Mostrar llistes completes de llibres

## Gestió de socis

- **Afegir soci** – permet registrar un nou soci a la biblioteca.
- **Mostrar socis** – llista completa dels socis registrats.

## Distribució del treball

1. Estructura bàsica de `main.py` ........... **Diana**
2. Creació i manteniment de `cataleg.json` .. **Diana / Oscar**
3. Desenvolupament del menú i interacció .... **Diana / Oscar**
4. Proves i depuració del programa .......... **Oscar**
5. Documentació i `README` final ............ **Diana / Oscar**
6. Estructura de `modelo.py` ................ **Diana / Oscar**

## Ús de la IA generativa

En aquest projecte hem fet ús puntual de **ChatGPT** per:

- Comprovar si el codi estava optimitzat o millorable
- Revisar estructures de JSON i funcions
- Creació de llista de llibres inicial en copilot:
  · promt:Genera un text que serà un arxiu csv separat amb menges, amb 40 llibres de diferents gèneres i autors de diferents nacionalitats que continguin
         la següent informació: títol, autor i genero del llibre, escrit com una llista de llibres
- Consulta copilot la reescriptura d'arxiu json
  · prompt: Com fer perquè aquest codi XXXX validi si ja existeix l'arxiu i si és així escrigui un nou moviment en lloc de reescriure sempre l'existent
- Resolució d'errors de sintaxis
- Consulta copilot lael format de sortida en la consulta de llibres per títol

## Funcionalitats principals

1. **Afegir llibre** – introduir llibre nou a la biblioteca.
2. **Prestar llibre** – assignar un llibre a un alumne.
3. **Retornar llibre** – tornar un llibre prestat.
4. **Buscar llibres per autor** – cerca per autor.
5. **Mostrar tots els llibres** – llista completa.
6. **Sortir del programa** – tanca l'aplicació.

## Mòduls / biblioteques Python

- `json`  → llegir i escriure `cataleg.json`
- `os`    → opcional, gestió de fitxers
- `sys`   → opcional, control del programa

## Control de versions i GitHub

- El repositori principal (**main**) va ser creat per **Oscar**.
- A partir de la branca principal, es van crear dues branques:
  - `branch_diana` → Diana (col·laboradora)
  - `branch_oscar` → Oscar
- Cada participant ha treballat a la seva pròpia branca segons les tasques assignades.
- Les branques s’han fusionat a la branca principal (`main`) un cop finalitzades les funcionalitats.

 **Enllaç del repositori GitHub:**
https://github.com/OscarFouz/Biblioteca_Python.git
