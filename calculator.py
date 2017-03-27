"""
Resolucion a problema py2:
Que reciba como entrada una lista de números números y 
que de salida regrese la suma de los mismos.
"""


class calculator_class:
    # Mediente una lista, almacenaremos los numeros a sumar en el metodo
    list = []
    sum_number = 0

    def sum(self):
        # El valor ingresado en La Variable "x" por el usuario, determinara el
        # tamano del arreglo
        x = int(raw_input("Cantidad de numeros a Sumar:"))
        for i in range(x):
            # El usuario ingresara los numeros a sumar
            self.list.append(int(raw_input("Registre el Numero:")))
        for i in self.list:
            self.sum_number += i
        print "\n Total de la Suma:", self.sum_number

# Se muestra el resultado mediante el metodo "sum"
obj = calculator_class()
obj.sum()
