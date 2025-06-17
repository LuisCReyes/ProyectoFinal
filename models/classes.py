class Product:
    def __init__(self, name, price, discount, stock, provider):
        self.name = name
        self.price = price
        self.discount = discount
        self.stock = stock
        self.provider = provider
        
        
    def __str__(self):
        return(f"Nombre: {self.name} \nPrecio: {self.price} \nDescuento: {self.discount} \nStock del producto: {self.stock} \nProveedor: {self.provider}")
        