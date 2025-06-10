import models.classes as c
import dao.functions as f

productos = f.InventarioDao()

def menu():
    print("""
          1. Agregar
          2. Mostrar
          6. Salir
          Digite una opcion:
          """)
def main():
        while (True):
            menu()
            option = input()
            if option == '1':
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio sin descuento: "))
                descuento = int(input("Descuento en entero y postivo: "))
                if descuento > 100 or descuento < 0:
                    print("Descuento inválido, debe ser un número no menor a 0 y no igual a 100")
                existencia = int(input("Existencia: "))
                if existencia < 0:
                    print("La existencia no puede ser negativa, pero si igual a 0")
                    continue
                proveedor = input("Proveedor del producto: ")
                producto = c.Product(nombre, precio, descuento, existencia, proveedor)
                productos.add(producto)
                
            elif option == '2':
                print("Prodcutos")
                productos.show()
            elif option == '6':
                print("Ádios")
                False
                
                
                
                break
            else:
                print("Opcion no valida, intente de nuevo")