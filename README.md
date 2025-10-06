# Sistema Académico - Prototipo de Baja Fidelidad

## Descripción
Sistema básico de gestión académica que permite registrar estudiantes, calificaciones y asistencia. Los datos se almacenan en un archivo JSON local.

## Características
- Registro de estudiantes con ID único
- Gestión de calificaciones por materia
- Control de asistencia diaria
- Consulta de calificaciones
- Generación de boletines de notas

## Requisitos
- Python 3.6 o superior
- No requiere librerías externas

## Instalación y Uso

### Ejecutar el programa
```bash
python prototipo_baja.py
```

### Estructura de datos
El sistema utiliza un archivo `db.json` con la siguiente estructura:
```json
{
  "students": {
    "ID_estudiante": {
      "name": "Nombre completo",
      "grade": "Grado escolar"
    }
  },
  "grades": {
    "ID_estudiante": {
      "materia": calificacion
    }
  },
  "attendance": {
    "ID_estudiante": {
      "YYYY-MM-DD": "P/A/T"
    }
  }
}
```

## Funcionalidades

### 1. Registrar Estudiante
- **Entrada**: ID único, nombre completo, grado
- **Función**: Almacena información básica del estudiante
- **Validación**: Verifica que se ingresen todos los campos

### 2. Registrar Nota
- **Entrada**: ID estudiante, materia, calificación (0-5)
- **Función**: Guarda calificaciones por materia
- **Validación**: Verifica que el estudiante exista y la nota sea numérica

### 3. Registrar Asistencia
- **Entrada**: ID estudiante, fecha (YYYY-MM-DD), estado (P/A/T)
- **Función**: Registra asistencia diaria
- **Estados**:
  - P: Presente
  - A: Ausente  
  - T: Tarde

### 4. Consultar Calificaciones
- **Entrada**: ID estudiante
- **Salida**: Lista de materias y calificaciones del estudiante

### 5. Generar Boletín
- **Entrada**: ID estudiante
- **Salida**: Reporte completo con:
  - Información personal
  - Todas las calificaciones
  - Últimos 10 registros de asistencia
  - Promedio general

## Ejemplo de Uso

```
--- SISTEMA ACADÉMICO (BAJA FIDELIDAD) ---
1) Registrar estudiante
2) Registrar nota
3) Registrar asistencia
4) Consultar calificaciones
5) Generar boletín (texto)
6) Salvar y salir
Opción: 1

ID del estudiante: 001
Nombre completo: Juan Pérez
Grado (ej: 6°): 6°
Estudiante Juan Pérez registrado con ID 001.
```

## Archivos del Sistema

### `prototipo_baja.py`
Archivo principal que contiene toda la lógica del sistema:
- `load_db()`: Carga datos desde JSON
- `save_db()`: Guarda datos en JSON
- `register_student()`: Registra nuevo estudiante
- `record_grade()`: Registra calificación
- `record_attendance()`: Registra asistencia
- `consult_grades()`: Consulta calificaciones
- `generate_report()`: Genera boletín completo
- `main()`: Menú principal del sistema

### `db.json`
Base de datos en formato JSON que se crea automáticamente al ejecutar el programa por primera vez.

## Limitaciones
- Almacenamiento local únicamente
- Sin validación avanzada de fechas
- Sin autenticación de usuarios
- Interfaz de línea de comandos básica
- Sin respaldo automático de datos

## Posibles Mejoras
- Interfaz gráfica
- Base de datos real
- Validaciones más robustas
- Sistema de usuarios y permisos
- Exportación a PDF
- Estadísticas y reportes avanzados

## Autor
Sistema desarrollado como prototipo de baja fidelidad para gestión académica básica.