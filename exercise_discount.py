def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos

    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)

    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento

    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final

    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0
    """
    precio = float(input())
    cantidad = int(input())
    no_descuento = cantidad*precio
    descuento = (cantidad*precio) * 0.10
    descue = (cantidad*precio) * 0.20

    if cantidad < 5: print(f"Subtotal: {no_descuento}\nDescuento aplicado: 0%\nMonto de descuento: 0.0\nTotal final: {no_descuento}")
    elif 5 <= cantidad <=9: print(f"Subtotal: {no_descuento}\nDescuento aplicado: 10%\nMonto de descuento: {descuento}\nTotal final: {no_descuento - descuento}")
    else: print(f"Subtotal: {no_descuento}\nDescuento aplicado: 20%\nMonto de descuento: {descue}\nTotal final: {no_descuento - descue}")
