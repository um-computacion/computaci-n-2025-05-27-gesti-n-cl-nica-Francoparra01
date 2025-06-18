# 🏥 Sistema de Gestión para una Clínica Médica
**Trabajo clinica – Computación I – Universidad de Mendoza**  
Carrera: Ingeniería en Informática – Año: 2025

---

## 📁 Estructura del Proyecto

/trabajo_clinica/
│
├── clases/ # Lógica del modelo
│ ├── paciente.py
│ ├── medico.py
│ ├── especialidad.py
│ ├── turno.py
│ ├── receta.py
│ ├── historia_clinica.py
│ ├── clinica.py
│ └── excepciones.py
│
├── cli/ # Interfaz por consola
│ └── interfaz.py
│
├── tests/ # Pruebas unitarias por clase
│ ├── test_paciente_y_medico.py
│ ├── test_especialidad.py
│ ├── test_turno.py
│ ├── test_receta.py
│ ├── test_historia_clinica.py
│ ├── test_clinica.py
│ └── init.py
│
├── main.py # Archivo principal de entrada
├── README_INSTRUCTIVO.md # Documentación

## ✅ **Ejecutar los tests**
Desde el directorio raíz del proyecto, ejecutar todos los tests:
python -m unittest discover -s tests

### **O ejecutar uno en particular:**
python tests/test_clinica.py

## **Menú disponible**
➕ Agregar paciente o médico

📅 Agendar turno (valida fecha, día y disponibilidad)

💊 Emitir receta (verifica existencia y contenido)

📘 Ver historia clínica

📋 Listar pacientes, médicos y turnos

# 🧠 Diseño general
🔹 Separación por responsabilidades
clases/: entidades y lógica del dominio

cli/: interfaz de consola para el usuario

tests/: tests organizados por clase usando unittest

# 🔸 Principales clases y responsabilidades

| Clase             | Rol principal                                        |
| ----------------- | ---------------------------------------------------- |
| `Paciente`        | Datos del paciente                                   |
| `Medico`          | Datos del médico y sus especialidades                |
| `Especialidad`    | Tipo y días de atención                              |
| `Turno`           | Relación paciente-médico en fecha y hora             |
| `Receta`          | Lista de medicamentos recetados                      |
| `HistoriaClinica` | Registro de turnos y recetas por paciente            |
| `Clinica`         | Orquesta todo el sistema                             |
| `Cli`             | Interfaz por consola del sistema (`cli/interfaz.py`) |


## ⚠️ Excepciones personalizadas
PacienteNoEncontradoException

MedicoNoDisponibleException

TurnoOcupadoException

RecetaInvalidaException

# 🧪 Cobertura de pruebas
✔️ Cada clase tiene su propio archivo de test.

✔️ Se utilizan unittest.TestCase, mock.patch y asserts personalizados.

✔️ El CLI se prueba simulando entradas con unittest.mock.

