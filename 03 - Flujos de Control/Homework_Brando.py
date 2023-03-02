#%% FLUJOS DE CONTROL

# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
var_int = 5
if var_int > 0:
    print('El número {} es mayor a cero'. format(var_int))
elif var_int < 0:
    print('El número {} es menor a cero'. format(var_int))
else:
    print('El número {} es igual a cero'. format(var_int))


# 2. Crear dos variables y un condicional que informe si son del mismo tipo de dato
var_float = 5.63

if type(var_int) == type(var_float):
    print('la var_1 de tipo {} ES IGUAL a la var_2 de tipo {}'. format(type(var_int), type(var_float)))
else:
    print('la var_1 de tipo {} es NO ES IGUAL a la var_2 de tipo {}'. format(type(var_int), type(var_float)))


# 5. Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for num in range(1,21):
    if num % 2 == 0:
        print('{} es PAR'.format(num))
    else:
        print('{} es IMPAR'.format(num))


# 6. En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for num in range(20):
    if num > 5:
        break
    print(num**3)


# 7. Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
for i in range (var_int):
    print(i+1)


# 8. Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
n = var_int
if n > 0:
    factorial = n
    while n > 2:
        n -= 1
        factorial *= n
    print('El factorial es:', factorial)
else:
    print('La variable no es mayor a cero')


# 9. Crear un ciclo for dentro de un ciclo while
n=0
while (5 > n):
    print('Este la iteración {} del bucle While'. format(n+1))
    for elem in range(1,6):
        print('Este la iteración {} del bucle For'. format(elem))
    n += 1


# 10. Crear un ciclo while dentro de un ciclo for
lista = ['a', 'b', 'c', 'd', 'e']
n=0
for i in range(len(lista)):
    while len(lista) > n:
        print(lista[n])
        n += 1
        if len(lista) > n:
            break


# 11. Imprimir los números primos existentes entre 0 y 30
n = 0
primo = True
while n < 30:
    for div in range(2, n):
        if n % div == 0:
            primo = False
    if primo:
        print(n)
    else:
        primo = True
    n += 1


# 12. ¿Se puede mejorar el proceso del punto 11? Utilizar las sentencias break y/ó continue para tal fin
n = 0
primo = True
while n < 30:
    for div in range(2, n):
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n)
    else:
        primo = True
    n += 1


# 13. En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
print('Solución A')
n = 0
count = 0
primo = True
while n < 30:
    for div in range(2, n):
        count += 1
        if n % div == 0:
            primo = False
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print(count)

print('Solución B')
n = 0
count = 0
primo = True
while n < 30:
    for div in range(2, n):
        count += 1
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print(count)


# 14. Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
print('Solución C')
n = 0
max_value = 100
count_1 = 0
primo = True
while n < max_value:
    for div in range(2, n):
        count_1 += 1
        if n % div == 0:
            primo = False
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print(count_1)

print('Solución D')
n = 0
count_2 = 0
primo = True
while n < max_value:
    for div in range(2, n):
        count_2 += 1
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print(count_2)
print(count_1/count_2*100)

#%%
# 15. Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
n = 99
while n <= 300:
    n +=1
    if n % 12 != 0:
        continue
    else:
        print(n)

#%%
# Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usuario de buscar el siguiente
num = int(input('Ingrese el valor: '))
print('El valor seleccionado es:', num)

seguir = True
primo = True
n = 0
while n <= num:
    for div in range(2, n):
        if n % div == 0:
            primo = False
            if seguir:
                valor = input('deseas continuar, pon S para Sí, o N para NO:')
                if valor == 'S':
                    num += 1
                else:
                    seguir = False
                    break
            break
    if primo:
        print(n)
    else:
        primo = True

    n += 1
    

# %%
# Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

n = 100
while n < 301:
    if n % 3 == 0:
        print(n*6)
        break
    n += 1


# %%
