#problema 1
def multiplicar_diccionario(diccionario):
    resultado = 1
    for valor in diccionario.values():
        resultado *= valor
    return resultado


diccionario = {'a': 5, 'b': 2, 'c': 3}
resultado = multiplicar_diccionario(diccionario)
print("El resultado de la multiplicación de todos los elementos del diccionario es:", resultado)

#problema 2
def eliminar_clave(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
        print("Clave eliminada:", clave)
    else:
        print("La clave no existe en el diccionario.")


diccionario = {'a': 1, 'b': 2, 'c': 3}
clave = 'b'
eliminar_clave(diccionario, clave)
print("Diccionario actualizado:", diccionario)

#problema 3
def listas_a_diccionario(list1, list2):
    if len(list1) == len(list2):
        diccionario = dict(zip(list1, list2))
        return diccionario
    else:
        print("Las listas no tienen la misma longitud.")
        return None


lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
diccionario = listas_a_diccionario(lista1, lista2)
print("Diccionario resultante:", diccionario)

#problema 4
def ordenar_diccionario_por_clave(diccionario):
    return dict(sorted(diccionario.items()))


diccionario = {'b': 3, 'a': 1, 'c': 2}
dicc_ord = ordenar_diccionario_por_clave(diccionario)
print("Diccionario ordenado:", dicc_ord)

#problema 5
def valores_maximo_minimo(diccionario):
    valores = list(diccionario.values())
    maximo = max(valores)
    minimo = min(valores)
    return maximo, minimo

diccionario = {'a': 5, 'b': 2, 'c': 7, 'd': 1}
maximo, minimo = valores_maximo_minimo(diccionario)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)

#problema 6
class Objeto:
    def __init__(self):
        self.nombre = "John"
        self.edad = 30
        self.pais = "USA"

    def a_diccionario(self):
        return self.__dict__

objeto = Objeto()
diccionario = objeto.a_diccionario()
print("Diccionario a partir de los campos del objeto:", diccionario)

#problema 7
def eliminar_duplicados(diccionario):
    dicc_noduplicados = {}
    for clave, valor in diccionario.items():
        if valor not in dicc_noduplicados .values():
            dicc_noduplicados [clave] = valor
    return dicc_noduplicados 


diccionario = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
dicc_noduplicados  = eliminar_duplicados(diccionario)
print("Diccionario sin duplicados:", dicc_noduplicados )

#problema 8
def diccionario_vacio(diccionario):
    return len(diccionario) == 0

dicc1 = {}
dicc2 = {'a': 1, 'b': 2, 'c': 3}
print("¿El diccionario 1 está vacío?", diccionario_vacio(dicc1))
print("¿El diccionario 2 está vacío?", diccionario_vacio(dicc2))

#problema 9 
def extraer_valores(lista_diccionarios, asignatura):
    valores = []
    for diccionario in lista_diccionarios:
        if asignatura in diccionario:
            valores.append(diccionario[asignatura])
    return valores

# Ejemplo
diccionarios = [{'matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'matematicas': 92, 'ciencia': 88}]
valores_ciencia = extraer_valores(diccionarios, 'ciencia')
print("Valores de la asignatura Ciencia:", valores_ciencia)

# problema 10
def extraer_valores(lista_diccionarios, asignatura):
    valores = []
    for diccionario in lista_diccionarios:
        if asignatura in diccionario:
            valores.append(diccionario[asignatura])
    return valores
# Ejemplo
diccionarios = [{'matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'matematicas': 92, 'ciencia': 88}]
valores_matematicas = extraer_valores(diccionarios, 'matematicas')
print("Valores de la asignatura Matemáticas:", valores_matematicas)

# problema 11
def longitud_diccionario(diccionario):
    return len(diccionario) 

# Ejemplo
diccionario = {'a': 1, 'b': 2, 'c': 3}
longitud = longitud_diccionario(diccionario)
print("Longitud del diccionario:", longitud)

# problema 12
def profundidad_diccionario(diccionario):
    if not isinstance(diccionario, dict): 
     return 0 
    max_profundidad = 0 
    for valor in diccionario.values():
         max_profundidad = max(max_profundidad, profundidad_diccionario(valor)) 
    return 1 + max_profundidad 
# Ejemplo
diccionario = {'a': {'b': {'c': 1}}}
profundidad = profundidad_diccionario(diccionario)
print("Profundidad del diccionario:", profundidad)

# problema 13
diccionario = {'fisica': 1, 'matematicas': 2, 'quimica': 3}
claves = list(diccionario.keys()) # "list" convierte las llaves [keys] en un diccionario
# Despues, "keys()" devuelve el nombre clave de cada objeto dentro de la lista, la clave es fisica y su valor es 1, pero solo nos interesa la clave que tiene
print("Salida esperada:", *claves) #El "*" simplemente pone un espacio despues de cada clave para que se imprima bonito

# problema 14
def convertir_diccionario_a_lista_de_listas(diccionario):
    lista_de_listas = []
    for key, value in diccionario.items(): 
        sublist = [key, value] 
        lista_de_listas.append(sublist)
    return lista_de_listas
# Ejemplo 
diccionario = {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'}
lista_de_listas = convertir_diccionario_a_lista_de_listas(diccionario)
print("Diccionario original convertido en lista de listas:", lista_de_listas)

# problema 15
def filtrar_numeros_pares(diccionario):
    diccionario_filtrado = {}
    for key, valores in diccionario.items(): 
        valores_pares = []
        for num in valores:
            if num % 2 == 0:
                valores_pares.append(num)
        diccionario_filtrado[key] = valores_pares
    return diccionario_filtrado
# Ejemplo
diccionario = {'II': [1, 3, 5], 'III': [1, 5], 'IV': [2, 7, 9], 'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
diccionario_filtrado1 = filtrar_numeros_pares(diccionario)
print("Diccionario filtrado:", diccionario_filtrado1) # En II y III no hay valores porque no tienen numeros pares




