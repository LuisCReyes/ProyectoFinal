# models/cotizacion.py

class Cotizacion:
    def __init__(self, producto, cantidad, precio_unitario):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def __str__(self):
        return f"Producto: {self.producto}, Cantidad: {self.cantidad}, Precio Unitario: ${self.precio_unitario:.2f}"
