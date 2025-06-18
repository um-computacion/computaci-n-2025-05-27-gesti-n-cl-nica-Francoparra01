import unittest
from datetime import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()

        self.paciente = Paciente("Laura Gómez", "12345678", "1990-03-10")
        self.clinica.agregar_paciente(self.paciente)

        self.medico = Medico("Dr. Pérez", "MAT123")
        self.clinica.agregar_medico(self.medico)

        # Especialidad válida para lunes y miércoles
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.clinica.agregar_especialidad_a_medico("MAT123", self.especialidad)

    def test_guardar_turno_en_historia(self):
        # Fecha: lunes 23 junio 2025, 10:00
        fecha_turno = datetime(2025, 6, 23, 10, 0)
        self.clinica.agendar_turno("12345678", "MAT123", "Cardiología", fecha_turno)

        historia = self.clinica.obtener_historia_clinica("12345678")
        turnos = historia.obtener_turnos()

        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "MAT123")
        self.assertEqual(turnos[0].obtener_fecha_hora(), fecha_turno)

    def test_guardar_receta_en_historia(self):
        medicamentos = ["Aspirina"]
        self.clinica.emitir_receta("12345678", "MAT123", medicamentos)

        historia = self.clinica.obtener_historia_clinica("12345678")
        recetas = historia.obtener_recetas()

        self.assertEqual(len(recetas), 1)
        # Suponiendo que Receta tiene método obtener_medico()
        self.assertEqual(recetas[0].obtener_medico().obtener_matricula(), "MAT123")

if __name__ == "__main__":
    unittest.main()
