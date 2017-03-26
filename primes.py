"""
Resolucion a problema py1:
Codigo que reciba como entrada un número entero y que de salida regrese un True o False.
"""


class prime_class:

    """
    Se crea una variable que captura el numero ingresado    
    """
    input_n = raw_input("Ingrese un numero: ")
    number = int(input_n)

    def is_prime(self):
        counter = 0
        # Se inicializa un bucle para calcular el numero dado.
        for i in range(1, self.number + 1):
            if (self.number % i) == 0:
                counter = counter + 1
            if counter >= 3:
                break
        # Dado el resultado, mediante condiciones se arroja SI es primo o NO
        val_bool = counter
        if val_bool == 2:
            print(val_bool == 2)
        else:
            print(val_bool == 0)
# Se muestra el resultado mediante el metodo "is_prime"
obj = prime_class()
obj.is_prime()
