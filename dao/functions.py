#Data Access Object
""" Agregar prodcutos al intventario y mostrarlos """
class InventarioDao:
    def __init__(self, inventario=None):
        if inventario is None:
            self.products = []
        else:
            self.products = inventario
    
    def add(self, producto_nuevo):
        self.products.append(producto_nuevo)
        print("Se ha agregado un producto al inventario")
        
    def remove(self, product):
        if product in self.products:
            self.products.remove(product)
            print("El producto ha sido eliminado del inventario")
        else:
            print("El producto no ha sido encontrado en el inventario")
            
    def show(self):
        for product in self.products:
            print(product)