"""
Funciones

1. Crear una función que reciba un número como parámetro y devuelva si True si es  y False si no lo es

2. Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son s en otra lista

3. Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

4. A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

5. Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
Fórmula 1 : (°C × 9/5) + 32 = °F
Fórmula 2 : °C + 273.15 = °K
Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

6. Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

7. Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo
"""

#%%
# 1. Crear una función que reciba un número como parámetro y devuelva si True si es  y False si no lo es

# def num_ (valor):
#     if  valor % 2 == 0:
#         print('El número {} no es '.format(valor))
#     elif 0 in [valor%x for x in range(2, valor)]:
#         print('El número {} no es '.format(valor))
#     else:
#         print('El número {} es '.format(valor))

# num_(13)

def num_primo (numero):
    for i in range(2, numero):
        if (numero % i) == 0:
            return False
    return True

print(num_primo(9))

#%%
# 2. Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y
# devuelva sólo aquellos que son primos en otra lista

def num_primos (lista):
    lista_primos = []
    for element in lista:
        if num_primo(element) == True:
            lista_primos.append(element)
    return lista_primos


print(num_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))

#%%
# 3. Crear una función que al recibir una lista de números, devuelva el que más se repite y
# cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

def most_repeated_numbers(lista):
    lista_unique = list(set(lista))
    count = 0
    lista_count = []
    result = []
    
    for i in range(len(lista_unique)):
        lista_count.append([lista_unique[i], lista.count(lista_unique[i])])
    
    for i in range(len(lista_count)-1):
        if lista_count[i][1] > lista_count[0][1]:
            result = (lista_count[i][0], lista_count[i][1])
    return result

lis = [1,1,5,6,8,10,22,5,6,4,11,9,5]
value, repeated =  most_repeated_numbers(lis)
print('The number {} is most repeated with {} times'.format(value, repeated))

# %%
# 4. A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el
# menor o el mayor de los mas repetidos.

def most_less_repeated_numbers(lista, funcion):
    lista_unique = list(set(lista))
    lista_count = []
    for i in range(len(lista_unique)):
        lista_count.append([lista_unique[i], lista.count(lista_unique[i])])

    result = lista_count[1]
    for i in range(len(lista_count)):
        if funcion == 'M':
            if lista_count[i][1] > result[1]:
                result = [lista_count[i][0], lista_count[i][1]]
                print(result)

        elif funcion == 'L':
            if lista_count[i][1] < result[1]:
                result = [lista_count[i][0], lista_count[i][1]]
        
    return result

lis = [1,22,1,5,6,8,10,22,5,6,4,22,11,9,5,22]
funcion = input('Escriba M to find the mos repeated number or L to find the less repeated number:')
value, repeated =  most_less_repeated_numbers(lis, funcion)
print('The number {} is most repeated with {} times'.format(value, repeated))

# %%
# 5. Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
# Fórmula 1 : (°C × 9/5) + 32 = °F
# Fórmula 2 : °C + 273.15 = °K
# Debe recibir 3 parámetros: el valor, la medida de origen y la medida de destino

def trans_temperature (value, unit_int, unit_out):
    # transformation functions
    def C_K(valor):
        return (valor + 273.15)
    def C_F(valor):
        return ((valor * 9/5) + 32)
    def F_C(valor):
        return((valor - 32) * 5/9)
    def K_C(valor):
        return (valor - 273.15)

    # options
    if unit_int == 'K':
        if unit_out == 'C':
            print('{}°K = {:.2f}°C'.format(value, K_C(value)))
        elif unit_out == 'F':
            print('{}°K = {:.2f}F'.format(value, C_F(K_C(value))))
        else:
            print('{}°K = {}°K'.format(value, value))

    elif unit_int == 'F':
        if unit_out == 'C':
            print('{}F = {:.2f}C'.format(value, F_C(value)))
        elif unit_out == 'K':
            print('{}F = {:.2f}°K'.format(value, C_K(F_C(value))))
        else:
            print('{}F = {}F'.format(value, value))

    elif unit_int == 'C':
        if unit_out == 'K':
            print('{}°C = {:.2f}°K'.format(value, C_K(value)))
        elif unit_out == 'F':
            print('{}°C = {:.2f}F'.format(value, C_F(value)))
        else:
            print('{}°C = {}°C'.format(value, value))

    else: 
        print("La opción seleccionada es incorrecta")

trans_temperature (15, 'F', 'K')

# 6. Iterando una lista con los tres valores posibles de temperatura que recibe la
# función del punto 5, hacer un print para cada combinación de los mismos:

tem_unit = ['F', 'C', 'K']

for i in range(len(tem_unit)):
    for j in range(len(tem_unit)):
        trans_temperature (15, tem_unit[i], tem_unit[j])

# %%
# 7. Armar una función que devuelva el factorial de un número. Tener en cuenta que
# el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

def factorial (valor):
    if valor < 0:
        return('the value must be positive')

    if not type(valor) == int:
        return('the value must be int')

    if valor > 1 and type(valor) == int:
        val_factorial = 1
        n = 1
        while n < valor:
            val_factorial *= n
            n += 1
        return (val_factorial)

number = 10
print('the factorial of', number, 'is', factorial (number))
print(factorial (-5))
print(factorial (2.8))
# %%
