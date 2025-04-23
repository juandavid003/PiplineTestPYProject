import time
from lector_csv import LectorCSV
from gestor_clientes import GestorClientes

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Buscar cliente por ID")
    print("2. Listar por ciudad")
    print("3. Ordenar por edad")
    print("4. Salir")

def main():
    ruta_csv = "clientes.csv"
    clientes, valido = LectorCSV.cargar_csv(ruta_csv)

    if not valido:
        return

    gestor = GestorClientes(clientes)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_busqueda = input("Ingrese el ID del cliente: ")
            # Medir el tiempo de la búsqueda
            inicio = time.perf_counter()
            for _ in range(100):  # Ejecutar varias veces para medir el tiempo promedio
                cliente = gestor.buscar_por_id(id_busqueda)
            fin = time.perf_counter()

            if cliente:
                print(cliente)
            else:
                print("Cliente no encontrado.")
            print(f"Tiempo promedio de búsqueda por ID: {(fin - inicio) / 100:.6f} segundos")

        elif opcion == "2":
            ciudad = input("Ingrese la ciudad: ")
            # Medir el tiempo de la búsqueda por ciudad
            inicio = time.perf_counter()
            for _ in range(100):  # Ejecutar varias veces para medir el tiempo promedio
                resultados = gestor.listar_por_ciudad(ciudad)
            fin = time.perf_counter()

            if resultados:
                for c in resultados:
                    print(c)
            else:
                print("No se encontraron clientes para la ciudad ingresada.")
            print(f"Tiempo promedio de búsqueda por ciudad: {(fin - inicio) / 100:.6f} segundos")

        elif opcion == "3":
            # Medir el tiempo de ordenar por edad
            inicio = time.perf_counter()
            for _ in range(100):  # Ejecutar varias veces para medir el tiempo promedio
                ordenados = gestor.ordenar_por_edad()
            fin = time.perf_counter()

            for c in ordenados:
                print(c)
            print(f"Tiempo promedio de ordenamiento por edad: {(fin - inicio) / 100:.6f} segundos")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
