class GestorClientes:
    def __init__(self, lista_clientes):
        self.clientes = lista_clientes

    def buscar_por_id(self, id_busqueda):
        cliente = next((c for c in self.clientes if c.id == id_busqueda), None)
        if cliente is None:
            print("Cliente no encontrado.")
        return cliente

    def listar_por_ciudad(self, ciudad):
        resultados = [c for c in self.clientes if c.ciudad == ciudad]
        if not resultados:
            print("No se encontraron clientes para la ciudad ingresada.")
        return resultados

    def ordenar_por_edad(self):
        return sorted(self.clientes, key=lambda c: c.edad)
