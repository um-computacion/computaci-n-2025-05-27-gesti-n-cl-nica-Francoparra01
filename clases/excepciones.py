# modelo/excepciones.py

class PacienteNoEncontradoException(Exception):
    def __init__(self, mensaje="Paciente no encontrado. Verifique el DNI ingresado."):
        super().__init__(mensaje)

class MedicoNoDisponibleException(Exception):
    def __init__(self, mensaje="El médico no está disponible para la especialidad o día solicitado."):
        super().__init__(mensaje)

class TurnoOcupadoException(Exception):
    def __init__(self, mensaje="Ya existe un turno asignado en esa fecha y hora."):
        super().__init__(mensaje)

class RecetaInvalidaException(Exception):
    def __init__(self, mensaje="La receta no es válida. Verifique los datos ingresados."):
        super().__init__(mensaje)

#class DniDuplicadoException(Exception):
    #def __init__(self, mensaje="Ya existe un paciente registrado con ese DNI."):
        #super().__init__(mensaje)

#class MatriculaDuplicadaException(Exception):
    #def __init__(self, mensaje="Ya existe un médico registrado con esa matrícula."):
        #super().__init__(mensaje)
