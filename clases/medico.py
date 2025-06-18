from clases.especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades: list[Especialidad] = []

    def agregar_especialidad(self, especialidad: Especialidad):
        # Evitar duplicados
        if any(esp.nombre.lower() == especialidad.nombre.lower() for esp in self.__especialidades):
            return
        self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for esp in self.__especialidades:
            if dia.lower() in [d.lower() for d in esp.dias_de_atencion]:
                return esp.nombre
        return None

    def __str__(self) -> str:
        especialidades = ", ".join(
            f"{esp.nombre} ({', '.join(esp.dias_de_atencion)})"
            for esp in self.__especialidades
        )
        return f"Médico: {self.__nombre} - Matrícula: {self.__matricula} - Especialidades: {especialidades}"
