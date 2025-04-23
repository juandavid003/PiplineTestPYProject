import csv
import os
import re
from cliente import Cliente

class LectorCSV:
    @staticmethod
    def contiene_tildes(texto):
        return bool(re.search(r"[áéíóúÁÉÍÓÚ]", texto))

    @staticmethod
    def cargar_csv(ruta_archivo):
        if not os.path.exists(ruta_archivo) or os.path.getsize(ruta_archivo) == 0:
            print("Archivo no encontrado o vacío. Verifique la ubicación del archivo.")
            return [], False

        clientes = []
        errores = 0
        try:
            with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                columnas_esperadas = {"id", "nombre", "email", "ciudad", "edad"}
                if not columnas_esperadas.issubset(lector.fieldnames):
                    print("Estructura del archivo inválida. Se requieren las columnas id, nombre, email, ciudad, edad.")
                    return [], False

                for fila in lector:
                    try:
                        id_cliente = fila['id'].strip()
                        nombre = fila['nombre'].strip()
                        email = fila['email'].strip()
                        ciudad = fila['ciudad'].strip()
                        edad_str = fila['edad'].strip()
                        extra = fila.get('extra', '').strip().lower()  # Puede no existir, por eso usamos .get

                        # Validaciones adicionales
                        if not nombre or not ciudad:
                            raise ValueError("Nombre o ciudad vacíos.")
                        if LectorCSV.contiene_tildes(nombre) or LectorCSV.contiene_tildes(ciudad):
                            raise ValueError("Nombre o ciudad con tildes.")
                        if extra == "dato_invalido":
                            raise ValueError("Campo 'extra' con dato inválido.")

                        edad = int(edad_str)  # Lanza excepción si no es numérico

                        cliente = Cliente(id_cliente, nombre, email, ciudad, edad)
                        clientes.append(cliente)

                    except Exception as e:
                        print(f"Registro inválido (ID: {fila.get('id', 'sin ID')}): {e}")
                        errores += 1

            if errores:
                print(f"\nSe ignoraron {errores} registros erróneos o inválidos.")
            return clientes, True

        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return [], False
