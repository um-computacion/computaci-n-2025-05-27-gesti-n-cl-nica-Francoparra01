# modelo/receta.py

from datetime import datetime
from clases.paciente import Paciente
from clases.medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        meds = ", ".join(self.__medicamentos)
        fecha_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        return (f"Receta:\n"
                f"  Fecha: {fecha_str}\n"
                f"  Médico: {self.__medico}\n"
                f"  Paciente: {self.__paciente}\n"
                f"  Medicamentos: {meds}")

