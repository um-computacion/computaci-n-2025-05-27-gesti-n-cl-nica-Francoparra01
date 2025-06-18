# modelo/turno.py

from datetime import datetime
from clases.paciente import Paciente
from clases.medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (f"Turno:\n"
                f"  Paciente: {self.__paciente}\n"
                f"  Médico: {self.__medico}\n"
                f"  Especialidad: {self.__especialidad}\n"
                f"  Fecha y Hora: {self.__fecha_hora.strftime('%d/%m/%Y %H:%M')}")
