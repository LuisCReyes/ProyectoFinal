# dao/historial_dao.py

from models.cotizacion import Cotizacion

class HistorialDAO:
    def __init__(self):
        self.historial = []

    def agregar_cotizacion(self, cotizacion: Cotizacion):
        self.historial.append(cotizacion)

    def buscar_producto(self, nombre_producto):
        return [cot for cot in self.historial if cot.producto.lower() == nombre_producto.lower()]

    def mostrar_historial(self):
        return self.historial
