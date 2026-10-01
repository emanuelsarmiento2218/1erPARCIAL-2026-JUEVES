from ejercicio5 import ProductoKwikE

class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig


class ListaEnlazada:
    def __init__(self):
        self.header = None

    def agregar_al_principio(self,dato):
        nodo_nuevo = Nodo(dato)
        nodo_nuevo._nxt = self.header
        self.header = nodo_nuevo


    def agregar_al_final(self,dato):
        nodo_nuevo = Nodo(dato)
        if self.header is None:
            self.header = nodo_nuevo
            return
        
        nodo_actual = self.header
        while nodo_actual._nxt is not None:
            nodo_actual = nodo_actual._nxt
        
        nodo_actual._nxt = nodo_nuevo

    def buscar(self, dato):
        nodo_actual = self.header
        while nodo_actual is not None:
            if nodo_actual._elem == dato:
                return nodo_actual
            nodo_actual = nodo_actual._nxt
        return None

    def recorrer_lista(self, dato):
        nodo_actual = self.header 
        while nodo_actual is not None:
            print(nodo_actual._elem)
            nodo_actual = nodo_actual._nxt

class KwikEMartv2:
    def __init__(self):
        self.bebidas = ListaEnlazada()
        self.snacks = ListaEnlazada()
        self.conveniencia = ListaEnlazada()
    
    def anadir_producto(self, producto, pasillo):
        assert isinstance(producto, ProductoKwikE), "El producto es invalido"
        if pasillo == "bebidas":
            self.bebidas.agregar_al_final(producto)
        elif pasillo == "snacks":
            self.snacks.agregar_al_final(producto)
        elif pasillo == "conveniencia":
            self.conveniencia.agregar_al_final(producto)
    
    def remover_del_inventario(self, producto_elim):
        
        for producto in self.bebidas:
            if producto == producto_elim:
                if producto_elim in self.bebidas:
                    self.bebidas.remove(producto_elim)
                    return

        for producto in self.snacks:
            if producto == producto_elim:
                if producto_elim in self.snacks:
                    self.snacks.remove(producto_elim)
                    return

        for producto in self.conveniencia:
            if producto == producto_elim:
                if producto_elim in self.conveniencia:
                    self.conveniencia.remove(producto_elim)
                    return

    def actualizar_stock(self, producto_act, stock_nuevo):

        for producto in self.bebidas:
            if producto == producto_act:
                producto_act.stock = stock_nuevo
                return

        for producto in self.snacks:
            if producto == producto_act:
                producto_act.stock = stock_nuevo
                return

        for producto in self.conveniencia:
            if producto == producto_act:
                producto_act.stock = stock_nuevo
                return
    
    def sacar_prox_vencidos(self):
       
        for producto in self.bebidas:
            if 0 <= producto.dias_para_vencer() <= 1:
                if producto in self.bebidas:
                    self.bebidas.remove(producto)

        for producto in self.snacks:
            if 0 <= producto.dias_para_vencer() <= 1:
                if producto in self.snacks:
                    self.snacks.remove(producto)
        
        for producto in self.conveniencia:
            if 0 <= producto.dias_para_vencer() <= 1:
                if producto in self.conveniencia:
                    self.conveniencia.remove(producto)
        

    def buscar_por_id(self, id_producto):
        for producto in self.bebidas:
            if producto.id_producto == id_producto:
                return producto
        
        for producto in self.snacks:
            if producto.id_producto == id_producto:
                return producto
        
        for producto in self.conveniencia:
            if producto.id_producto == id_producto:
                return producto
        return None