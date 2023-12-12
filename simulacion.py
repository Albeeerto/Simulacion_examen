class Curso:
    def __init__(self, id_curso, nombre, creditos, años_estudio):
        self.id_curso = id_curso
        self.nombre = nombre
        self.creditos = creditos
        self.años_estudio = años_estudio

    def mostrar_ficha(self):
        print(f"Ficha del Curso {self.id_curso}:")
        print(f"Nombre: {self.nombre}")
        print(f"Créditos: {self.creditos}")
        print(f"Años de estudio: {self.años_estudio}")
        print()

class Alumno:
    def __init__(self, id_alumno, nombre, email):
        self.id_alumno = id_alumno
        self.nombre = nombre
        self.email = email

    def mostrar_ficha(self):
        print(f"Ficha del Alumno {self.id_alumno}:")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print()

class Matricula:
    def __init__(self, id_matricula, fecha_matricula, id_alumno, id_curso):
        self.id_matricula = id_matricula
        self.fecha_matricula = fecha_matricula
        self.id_alumno = id_alumno
        self.id_curso = id_curso

    def mostrar_datos_matricula(self):
        print(f"Información de la Matrícula {self.id_matricula}:")
        print(f"Fecha de matrícula: {self.fecha_matricula}")
        print(f"ID Alumno: {self.id_alumno}")
        print(f"ID Curso: {self.id_curso}")
        print()

class Centro:
    def __init__(self):
        self.matriculas = []

    def realizar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def mostrar_matriculas(self):
        print("Matrículas realizadas en el centro:")
        for matricula in self.matriculas:
            matricula.mostrar_datos_matricula()

# Crear instancias de las clases
centro = Centro()
curso1 = Curso(1, "Programación en Python", 4, 2)
curso2 = Curso(2, "Bases de Datos", 3, 1)
alumno1 = Alumno(101, "Juan Perez", "juan@example.com")
alumno2 = Alumno(102, "Maria Gomez", "maria@example.com")

alumno1.mostrar_ficha()

alumno2.mostrar_ficha()

curso1.mostrar_ficha()
curso2.mostrar_ficha()

matricula1_curso1 = Matricula(1001, "2023-01-15", alumno1.id_alumno, curso1.id_curso)
centro.realizar_matricula(matricula1_curso1)

matricula2_curso1 = Matricula(1002, "2023-02-01", alumno2.id_alumno, curso1.id_curso)
centro.realizar_matricula(matricula2_curso1)

matricula3_curso2 = Matricula(1003, "2023-02-05", alumno2.id_alumno, curso2.id_curso)
centro.realizar_matricula(matricula3_curso2)

centro.mostrar_matriculas()
