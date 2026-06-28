from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante: str = nombre_restaurante
        
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        
        self.lista_productos.append(producto)
        print(f"[Sistema] Producto '{producto.nombre}' registrado con éxito.")

    def registrar_cliente(self, cliente: Cliente) -> None:
        
        self.lista_clientes.append(cliente)
        print(f"[Sistema] Cliente '{cliente.nombre_completo}' registrado en la mesa {cliente.numero_mesa}.")

    def mostrar_menu_y_clientes(self) -> None:
       
        print(f"\n--- BIENVENIDOS A: {self.nombre_restaurante.upper()} ---")
        
        print("\n--- MENÚ DE PRODUCTOS ---")
        for prod in self.lista_productos:
            print(prod)

        print("\n--- CLIENTES EN SALA ---")
        for cli in self.lista_clientes:
            print(cli)
        print("-" * 40)
