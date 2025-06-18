import unittest
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.excepciones import PacienteNoEncontradoException, MedicoNoDisponibleException, RecetaInvalidaException

class TestRecetas(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        # Paciente válido
        self.paciente = Paciente("Ana López", "87654321", "1985-05-05")
        self.clinica.agregar_paciente(self.paciente)
        # Médico válido
        self.medico = Medico("Dra. Ruiz", "MAT456")
        self.clinica.agregar_medico(self.medico)

    def test_emitir_receta_exitosa(self):
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        # No debería lanzar excepción
        self.clinica.emitir_receta("87654321", "MAT456", medicamentos)
        # Opcional: verificar que la receta quedó guardada en la historia clínica
        historia = self.clinica.obtener_historia_clinica("87654321")
        self.assertTrue(len(historia.obtener_recetas()) > 0)

    def test_error_paciente_no_encontrado(self):
        medicamentos = ["Paracetamol"]
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("00000000", "MAT456", medicamentos)

    def test_error_medico_no_encontrado(self):
        medicamentos = ["Paracetamol"]
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.emitir_receta("87654321", "MAT999", medicamentos)

    def test_error_medicamentos_vacio(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("87654321", "MAT456", [])

if __name__ == "__main__":
    unittest.main()
