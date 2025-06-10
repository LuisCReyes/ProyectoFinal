class Product:
    def _init_(self, name, price, discount, stock, provider):
        self.name = name
        self.price = price
        self.discount = discount
        self.stock = stock
        self.provider = provider
        
        
        def __str__(Self):
            return(f"Nombre: {self.name} \nPrecio: {self.price} \nDescuento: {self.discount} \nStock del producto: {self.stock} \nProveedor: {self.provider}")
        