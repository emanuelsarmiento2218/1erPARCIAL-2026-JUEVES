from ejercicio5 import ProductoKwikE

class KwikEMart:
    def __init__(self):
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []
    
    def anadir_producto(self, producto, pasillo):
        assert isinstance(producto, ProductoKwikE), "El producto es invalido"
        if pasillo == "bebidas":
            self.bebidas.append(producto)
        elif pasillo == "snacks":
            self.snacks.append(producto)
        elif pasillo == "conveniencia":
            self.conveniencia.append(producto)
    
    def remover_del_inventario(self, producto_elim):
        inventario = self.bebidas + self.snacks + self.conveniencia
        for producto in inventario:
            if producto == producto_elim:
                if producto_elim in self.bebidas:
                    self.bebidas.remove(producto_elim)
                elif producto_elim in self.snacks:
                    self.snacks.remove(producto_elim)
                elif producto_elim in self.conveniencia:
                    self.conveniencia.remove(producto_elim)
                return

    def actualizar_stock(self, producto_act, stock_nuevo):
        inventario = self.bebidas + self.snacks + self.conveniencia
        for producto in inventario:
            if producto == producto_act:
                producto_act.stock = stock_nuevo
                return
    
    def sacar_prox_vencidos(self):
        inventario = self.bebidas + self.snacks + self.conveniencia
        for producto in inventario:
            if 0 <= producto.dias_para_vencer() <= 1:
                if producto in self.bebidas:
                    self.bebidas.remove(producto)
                elif producto in self.snacks:
                    self.snacks.remove(producto)
                elif producto in self.conveniencia:
                    self.conveniencia.remove(producto)

    def buscar_por_id(self, id_producto):
        inventario = self.bebidas + self.snacks + self.conveniencia
        for producto in inventario:
            if producto.id_producto == id_producto:
                return producto
        return None



