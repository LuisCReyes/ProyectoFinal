# main/app.py

import sys
import os

# Agregar la carpeta raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dao.historial_dao import HistorialDAO
from models.cotizacion import Cotizacion

def mostrar_menu():
    print("\n--- Menú de Cotizaciones ---")
    print("1. Registrar cotización")
    print("2. Buscar producto en historial")
    print("3. Ver historial completo")
    print("4. Salir")

def main():
    historial = HistorialDAO()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio unitario: "))
            cotizacion = Cotizacion(producto, cantidad, precio)
            historial.agregar_cotizacion(cotizacion)
            print("✅ Cotización registrada con éxito.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = historial.buscar_producto(nombre)
            if resultados:
                print("🔍 Producto encontrado:")
                for cot in resultados:
                    print(cot)
            else:
                print("❌ El producto no se encuentra en el historial.")

        elif opcion == "3":
            historial_total = historial.mostrar_historial()
            print("📋 Historial completo de cotizaciones:")
            if historial_total:
                for cot in historial_total:
                    print(cot)
            else:
                print("Aún no hay cotizaciones registradas.")

        elif opcion == "4":
            print("👋 Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print("⚠️ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
