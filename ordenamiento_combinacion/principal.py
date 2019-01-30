"""
    Ejemplo tomado de 
    http://www.pythondiario.com/2018/08/ordenamiento-por-mezcla-merge-sort.html
"""
"""
    Importamos todos lso paquetes y ficheros respectivos
"""
from ordenamiento_combinacion.funciones.combinacion import *
from ordenamiento_combinacion.funciones.miarchivo import *
from ordenamiento_combinacion.objetos.estudiante import *

a= MiArchivo("data/ejemplo.txt") # Creamos un objeto archvio mandando la ubicion de nuestro data
l_a=a.obtener_informacion() # obtenemos la informacion en una lista
l_a=[l.split(";") for l in l_a] # Separamso cada linea por un separador este caso (;)
l_edades=[] # Creamos uan lista auxiliar para las edades(nuestro caso)
# Creamos un objeto ocn cada linea de la lista de todos los datos
for l in l_a:
    e = estudiante(l[0],l[1],l[2]) # creamos le objeto estudiante con lso datos de la linea actual
    l_edades.append(e.edad) # aniadimso al edad a la lista de edaes

merge_sort_result = merge_sort(l_edades) # creamos uan nueva lista con la lista de edades ordenada mediante el ordenamiento de combinacion

print(merge_sort_result) # imprimimso al nueva lista

