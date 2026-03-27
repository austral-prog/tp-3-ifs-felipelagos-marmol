def age_check():
    """
    Ejercicio 3 - Verificar Mayoría de Edad

    Leer una edad y un límite de edad mediante input(). Verificar que ambos números sean
    válidos (positivos), y luego determinar si la persona es mayor de edad comparando
    con el límite ingresado.

    Si alguno de los números es negativo o cero, imprimir "Entrada invalida".

    Ejemplo:
        Para las entradas "20" y "18", la salida esperada es:
        Eres mayor de edad

        Para las entradas "16" y "18", la salida esperada es:
        Eres menor de edad

        Para las entradas "-5" y "18", la salida esperada es:
        Entrada invalida
    """
    edad_1 = int(input())
    edad_lim = int(input())
    if edad_1 >= 18 and edad_lim >= 18: print("Eres mayor de edad")
    elif edad_1 <= 0 or edad_lim <= 0: print("Entrada invalida")
    elif edad_1<edad_lim: print("Eres menor de edad")
