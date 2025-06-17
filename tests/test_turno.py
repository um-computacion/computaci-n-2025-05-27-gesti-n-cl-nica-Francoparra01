import unittest
from datetime import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad
from clases.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
)

class TestTurnos(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()

        # Paciente válido
        self.paciente = Paciente("Juan Perez", "12345678", "1990-01-01")
        self.clinica.agregar_paciente(self.paciente)

        # Médico válido con especialidad "Cardiología" lunes y miércoles
        self.medico = Medico("Dr. Gómez", "MAT123")
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(esp)
        self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_exitoso(self):
        fecha_turno = datetime(2025, 6, 23, 10, 0)  # lunes
        self.clinica.agendar_turno("12345678", "MAT123", "Cardiología", fecha_turno)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "MAT123")

    def test_error_paciente_no_encontrado(self):
        fecha_turno = datetime(2025, 6, 23, 10, 0)  # lunes
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("00000000", "MAT123", "Cardiología", fecha_turno)

    def test_error_medico_no_encontrado(self):
        fecha_turno = datetime(2025, 6, 23, 10, 0)  # lunes
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MAT999", "Cardiología", fecha_turno)

    def test_error_turno_duplicado(self):
        fecha_turno = datetime(2025, 6, 23, 10, 0)  # lunes
        self.clinica.agendar_turno("12345678", "MAT123", "Cardiología", fecha_turno)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "MAT123", "Cardiología", fecha_turno)

    def test_error_especialidad_no_atendida(self):
        fecha_turno = datetime(2025, 6, 23, 10, 0)  # lunes
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MAT123", "Pediatría", fecha_turno)

    def test_error_medico_no_atiende_dia(self):
        fecha_turno = datetime(2025, 6, 24, 10, 0)  # martes (no trabaja martes)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MAT123", "Cardiología", fecha_turno)

if __name__ == "__main__":
    unittest.main()
