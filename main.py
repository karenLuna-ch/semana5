from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def ejecutar_sistema():
    
    mi_restaurante = Restaurante("Gourmet Modular")
    print("--- Iniciando Operaciones del Restaurante ---\n")

    
    platillo_uno = Producto(nombre="Asado de Tira", precio=18.50, disponible=True)
    platillo_dos = Producto(nombre="Limonada Imperial", precio=3.75, disponible=True)
    platillo_tres = Producto(nombre="Volcán de Chocolate", precio=5.50, disponible=False)

    
    cliente_uno = Cliente(nombre_completo="Karen Chango", numero_mesa=4, es_frecuente=True)
    cliente_dos = Cliente(nombre_completo="Carlos Mendoza", numero_mesa=9, es_frecuente=False)

    
    mi_restaurante.registrar_producto(platillo_uno)
    mi_restaurante.registrar_producto(platillo_dos)
    mi_restaurante.registrar_producto(platillo_tres)
    
    print()  
    
    mi_restaurante.registrar_cliente(cliente_uno)
    mi_restaurante.registrar_cliente(cliente_dos)

    
    mi_restaurante.mostrar_menu_y_clientes()


if __name__ == "__main__":
    ejecutar_sistema()