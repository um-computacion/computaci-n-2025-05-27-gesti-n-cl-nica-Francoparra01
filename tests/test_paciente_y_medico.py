# tests/test_paciente_y_medico.py

import unittest
from clases.paciente import Paciente
from clases.medico import Medico
from clases.clinica import Clinica
from clases.excepciones import MedicoNoDisponibleException, PacienteNoEncontradoException

class TestRegistroPacientesYMedicos(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()

    def test_registro_exitoso_paciente(self):
        paciente = Paciente("Juan Pérez", "12345678", "1990-01-01")
        self.clinica.agregar_paciente(paciente)
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(pacientes[0].obtener_dni(), "12345678")

    def test_registro_exitoso_medico(self):
        medico = Medico("Dra. Gómez", "MAT-001")
        self.clinica.agregar_medico(medico)
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0].obtener_matricula(), "MAT-001")

    def test_no_permite_paciente_duplicado(self):
        paciente1 = Paciente("Ana", "111", "2000-01-01")
        paciente2 = Paciente("Ana duplicada", "111", "2000-01-01")
        self.clinica.agregar_paciente(paciente1)
        self.clinica.agregar_paciente(paciente2)  # pisa el anterior
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)  # falla si no se previene duplicado

    def test_no_permite_medico_duplicado(self):
        medico1 = Medico("Dr. A", "MAT-999")
        medico2 = Medico("Dr. B", "MAT-999")
        self.clinica.agregar_medico(medico1)
        self.clinica.agregar_medico(medico2)  # pisa el anterior
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)  # falla si no se previene duplicado

    def test_error_por_datos_invalidos(self):
        with self.assertRaises(TypeError):
            Paciente(None, None, None)

        with self.assertRaises(TypeError):
            Medico(None, None)

if __name__ == "__main__":
    unittest.main()
