# modelo/historia_clinica.py

from clases.paciente import Paciente
from clases.turno import Turno
from clases.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self.__paciente = paciente
        self.__turnos: list[Turno] = []
        self.__recetas: list[Receta] = []

    def agregar_turno(self, turno: Turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        self.__recetas.append(receta)

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()

    def obtener_recetas(self) -> list[Receta]:
        return self.__recetas.copy()

    def __str__(self) -> str:
        turnos_str = "\n  ".join(str(t) for t in self.__turnos) or "Sin turnos"
        recetas_str = "\n  ".join(str(r) for r in self.__recetas) or "Sin recetas"
        return (f"Historia Clínica del paciente:\n"
                f"{self.__paciente}\n\n"
                f"Turnos:\n  {turnos_str}\n\n"
                f"Recetas:\n  {recetas_str}")
