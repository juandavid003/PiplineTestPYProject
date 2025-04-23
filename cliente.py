class Cliente:
    def __init__(self, id, nombre, email, ciudad, edad):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.ciudad = ciudad
        self.edad = int(edad)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.email} - {self.ciudad} - {self.edad} años"