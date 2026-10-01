from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        
        if type(descripcion) is not str:
            raise TypeError("la descripcion debe ser un string")
        if type(id_producto) is not int:
            raise TypeError("la descripcion debe ser un entero")
        if type(fecha_vencimiento) is not date:
            raise TypeError("la descripcion debe ser tipo date")
        if type(precio) is not float:
            raise TypeError("la descripcion debe ser tipo float")
        if type(stock) is not int:
            raise TypeError("la descripcion debe ser de tipo entero") #utilice raise para que no se ingresen datos de un tipo que no se pide 

        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock

    def cambiar_datos(self, descripcion=None, precio=None, stock=None):

        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def calcular_vencimiento(self):
        dias = (self.fecha_vencimiento - date.today()).days
        if dias < 0:
            self.stock = 0
            return f'el producto: {self.descripcion} esta vencido, se retiro el stock.'
        else:
            return dias

    def dias_para_vencer(self):
        dias_para_vencer = (self.fecha_vencimiento - date.today()).days
        return dias_para_vencer
 
    def __str__(self):
        return f' Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio} | Stock: {self.stock} '
    
    def __eq__(self, producto):
        return self.id_producto == producto.id_producto or self.descripcion == producto.descripcion