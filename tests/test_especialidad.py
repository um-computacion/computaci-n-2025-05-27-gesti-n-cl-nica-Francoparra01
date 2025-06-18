import unittest
from clases.clinica import Clinica
from clases.medico import Medico
from clases.especialidad import Especialidad
from clases.excepciones import MedicoNoDisponibleException

class TestEspecialidades(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.medico = Medico("Dr. House", "M123")
        self.clinica.agregar_medico(self.medico)

    def test_agregar_especialidad_nueva(self):
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.clinica.agregar_especialidad_a_medico(self.medico.obtener_matricula(), esp)
        especialidad_obtenida = self.medico.obtener_especialidad_para_dia("lunes")
        self.assertEqual(especialidad_obtenida, "Cardiología")

    def test_evitar_duplicados_de_especialidad(self):
        esp1 = Especialidad("Cardiología", ["lunes", "miércoles"])
        esp2 = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.clinica.agregar_especialidad_a_medico(self.medico.obtener_matricula(), esp1)
        self.clinica.agregar_especialidad_a_medico(self.medico.obtener_matricula(), esp2)
        # Debe existir solo una especialidad Cardiología
        especialidades = [esp.nombre for esp in self.medico._Medico__especialidades]
        self.assertEqual(especialidades.count("Cardiología"), 1)

    def test_dias_de_atencion_invalidos(self):
        # Especialidad con días inválidos (por ejemplo, "funday")
        esp = Especialidad("Neurología", ["funday", "martes"])
        self.clinica.agregar_especialidad_a_medico(self.medico.obtener_matricula(), esp)
        # "martes" sí debe devolver la especialidad
        self.assertEqual(self.medico.obtener_especialidad_para_dia("martes"), "Neurología")
        # "funday" no es un día válido, no debería devolver nada
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("funday"))

    def test_error_agregar_especialidad_medico_no_registrado(self):
        esp = Especialidad("Pediatría", ["jueves"])
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agregar_especialidad_a_medico("M999", esp)  # Matrícula no registrada

if __name__ == '__main__':
    unittest.main()
