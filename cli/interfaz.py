# cli/interfaz.py

from datetime import datetime
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad
from clases.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
)
import sys

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n--- Menú Clínica ---")
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agendar turno")
        print("4) Agregar especialidad a médico")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.agregar_especialidad_medico()
            elif opcion == "5":
                self.emitir_receta()
            elif opcion == "6":
                self.ver_historia_clinica()
            elif opcion == "7":
                self.ver_todos_los_turnos()
            elif opcion == "8":
                self.ver_todos_los_pacientes()
            elif opcion == "9":
                self.ver_todos_los_medicos()
            elif opcion == "0":
                print("Gracias por usar el sistema de la clínica. ¡Hasta luego!")
                sys.exit()
            else:
                print("Opción inválida, intente nuevamente.")

    def agregar_paciente(self):
        try:
            nombre = input("Nombre completo del paciente: ").strip()
            dni = input("DNI del paciente: ").strip()
            fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
            # Podrías agregar validación básica de fecha aquí si querés
            paciente = Paciente(nombre, dni, fecha_nac)
            self.clinica.agregar_paciente(paciente)
            print(f"Paciente {nombre} agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar paciente: {e}")

    def agregar_medico(self):
        try:
            nombre = input("Nombre completo del médico: ").strip()
            matricula = input("Matrícula profesional: ").strip()
            medico = Medico(nombre, matricula)

            while True:
                agregar_esp = input("¿Desea agregar una especialidad? (s/n): ").strip().lower()
                if agregar_esp != "s":
                    break
                tipo = input("Nombre de la especialidad: ").strip()
                dias_str = input("Días de atención separados por comas (ej: lunes,martes): ").strip()
                dias = [d.strip().lower() for d in dias_str.split(",") if d.strip()]
                especialidad = Especialidad(tipo, dias)
                medico.agregar_especialidad(especialidad)

            self.clinica.agregar_medico(medico)
            print(f"Médico {nombre} agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar médico: {e}")

    def agendar_turno(self):
        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            especialidad = input("Especialidad: ").strip()
            fecha_hora_str = input("Fecha y hora del turno (dd/mm/aaaa HH:MM): ").strip()
            fecha_hora = datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M")

            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado exitosamente.")
        except PacienteNoEncontradoException:
            print("Error: Paciente no encontrado.")
        except MedicoNoDisponibleException as e:
            print(f"Error: {e}")
        except TurnoOcupadoException:
            print("Error: El médico ya tiene un turno en esa fecha y hora.")
        except ValueError:
            print("Error: Formato de fecha/hora inválido. Use dd/mm/aaaa HH:MM.")
        except Exception as e:
            print(f"Error al agendar turno: {e}")

    def agregar_especialidad_medico(self):
        try:
            matricula = input("Matrícula del médico: ").strip()
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            tipo = input("Nombre de la especialidad: ").strip()
            dias_str = input("Días de atención separados por comas (ej: lunes,martes): ").strip()
            dias = [d.strip().lower() for d in dias_str.split(",") if d.strip()]
            especialidad = Especialidad(tipo, dias)
            medico.agregar_especialidad(especialidad)
            print(f"Especialidad {tipo} agregada al médico {medico}.")
        except MedicoNoDisponibleException:
            print("Error: Médico no encontrado.")
        except Exception as e:
            print(f"Error al agregar especialidad: {e}")

    def emitir_receta(self):
        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            medicamentos_str = input("Medicamentos separados por comas: ").strip()
            medicamentos = [m.strip() for m in medicamentos_str.split(",") if m.strip()]
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida exitosamente.")
        except PacienteNoEncontradoException:
            print("Error: Paciente no encontrado.")
        except MedicoNoDisponibleException:
            print("Error: Médico no encontrado.")
        except RecetaInvalidaException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error al emitir receta: {e}")

    def ver_historia_clinica(self):
        try:
            dni = input("DNI del paciente: ").strip()
            historia = self.clinica.obtener_historia_clinica(dni)
            print("\n--- Historia Clínica ---")
            print(historia)
        except PacienteNoEncontradoException:
            print("Error: Paciente no encontrado.")
        except Exception as e:
            print(f"Error al obtener historia clínica: {e}")

    def ver_todos_los_turnos(self):
        turnos = self.clinica.obtener_turnos()
        if not turnos:
            print("No hay turnos agendados.")
            return
        print("\n--- Turnos agendados ---")
        for turno in turnos:
            print(turno)

    def ver_todos_los_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        if not pacientes:
            print("No hay pacientes registrados.")
            return
        print("\n--- Pacientes registrados ---")
        for paciente in pacientes:
            print(paciente)

    def ver_todos_los_medicos(self):
        medicos = self.clinica.obtener_medicos()
        if not medicos:
            print("No hay médicos registrados.")
            return
        print("\n--- Médicos registrados ---")
        for medico in medicos:
            print(medico)


if __name__ == "__main__":
    cli = CLI()
    cli.ejecutar()

