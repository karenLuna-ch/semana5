class Cliente:
    def __init__(self, nombre_completo: str, numero_mesa: int, es_frecuente: bool):
        
        self.nombre_completo: str = nombre_completo  
        self.numero_mesa: int = numero_mesa          
        self.es_frecuente: bool = es_frecuente       

    def __str__(self) -> str:
        
        tipo_cliente = "Frecuente" if self.es_frecuente else "Regular"
        return f"Cliente: {self.nombre_completo} | Mesa: {self.numero_mesa} | Tipo: {tipo_cliente}"

