from ejercicio5 import ProductoKwikE

class KwikEMart:
    def __init__(self):
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []
    
    def anadir_producto(self, producto, pasillo):
        if pasillo == "bebidas":
            self.bebidas.append(producto)
        if pasillo == "snacks":
            self.snacks.append(producto)
        if pasillo == "conveniencia":
            self.conveniencia.append(producto)
    
    def remover_del_inventario(self, producto_elim):
        inventario = self.bebidas + self.snacks + self.conveniencia
        
        for producto in inventario:
            if producto == producto_elim:
                if producto_elim in self.bebidas:
                    self.bebidas.remove(producto_elim)
                if producto_elim in self.snacks:
                    self.snacks.remove(producto_elim)
                if producto_elim in self.conveniencia:
                    self.conveniencia.remove(producto_elim)
                return

    def actualizar_stock(self, producto_act, stock_nuevo):
        for producto in inventario:
            if producto == producto_act:
                producto_act.stock = stock_nuevo
                return

    def cambiar_precio(self, precio_nuevo):
        pass

    def proximos_a_vencer(self):
    pass
