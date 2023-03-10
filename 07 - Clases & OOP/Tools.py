class Tools():
    def __init__(self, lista_números) -> list:
        self.lista = lista_números

    def num_primo(self):
        result = []
        for i in self.lista:
            if (self.__num_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
                result.append(True)
            else:
                print('El elemento', i, 'NO es un numero primo')
                result.append(False)
        return result

    def __num_primo (self, numero) -> int:  # __name se refiere a un método privado, solo se usa dentro de la clase
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
        return True



    def most_repeated_numbers(self):
        lista_unique = list(set(self.lista))
        lista_count = []
        result = []
        
        for i in range(len(lista_unique)):
            lista_count.append([lista_unique[i], self.lista.count(lista_unique[i])])
        
        for i in range(len(lista_count)-1):
            if lista_count[i][1] > lista_count[0][1]:
                result = (lista_count[i][0], lista_count[i][1])
        return result



    def trans_temperature(self, origen, destino):
        result_destino = []
        for i in self.lista:
            result = self.__trans_temperature(i, origen, destino)
            result_destino.append(result)
        return result_destino

    def __trans_temperature (self, value, unit_int, unit_out):
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
                return('{}°K = {:.2f}°C'.format(value, K_C(value)))
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
                return('{}°C = {:.1f}°K'.format(value, C_K(value)))
            elif unit_out == 'F':
                return('{}°C = {:.1f}F'.format(value, C_F(value)))
            else:
                return('{}°C = {}°C'.format(value, value))
        else: 
            print("La opción seleccionada es incorrecta")



    def factorial (self):
        result_factorial = []
        for i in self.lista:
            result = self.__factorial(i)
            print('el factorial de', i, 'es:', result)
            result_factorial.append(result)
        return result_factorial


    def __factorial (self, valor) -> int:
        if valor < 0:
            return('the value must be positive')

        if not type(valor) == int:
            return('the value must be int')

        if valor > 1 and type(valor) == int:
            val_factorial = 1
            n = 1
            while n <= valor:
                val_factorial *= n
                n += 1
            return (val_factorial)