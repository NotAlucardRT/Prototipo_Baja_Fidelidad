import json
from pathlib import Path

DB_FILE = Path("db.json")

DEFAULT_DB = {
    "students": {},
    "grades": {}, #student_id: {subject: grade}
    "attendance": {} #student_id: {"2025-10-01": "P"}
}

def load_db():
    if not DB_FILE.exists():
        save_db(DEFAULT_DB)
    with open(DB_FILE, 'r', encoding = 'utf-8') as f:
        return json.load(f)
    
def save_db(db):
    with open(DB_FILE, 'w', encoding = 'utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def register_student(db):
    student_id = input("ID del estudiante: ").strip()
    name = input("Nombre completo: ").strip()
    grade_level = input("Grado (ej: 6°): ").strip()
    db['students'][student_id] = {"name": name, "grade": grade_level}
    print(f"Estudiante {name} registrado con ID {student_id}.")

def record_grade(db):
    student_id = input("ID del estudiante: ").strip()
    if student_id not in db['students']:
        print("Estudiante no encontrado.")
        return
    subject = input("Materia: ").strip()
    try:
        grade = float(input("Nota (0-5): ").strip())
    except:
        print("Nota inválida.")
        return
    db['grades'].setdefault(student_id, {})[subject] = grade
    print("Nota registrada.")

def record_attendance(db):
    student_id = input("ID del estudiante: ").strip()
    if student_id not in db['students']:
        print("Estudiante no encontrado.")
        return
    date = input("Fecha (YYYY-MM-DD): ").strip()
    status = input("Estado (P=Presente, A=Ausente, T=Tarde): ").strip().upper()
    db['attendance'].setdefault(student_id, {})[date] = status
    print("Asistencia registrada.")

def consult_grades(db):
    student_id = input("ID del estudiante: ").strip()
    student = db['students'].get(student_id)
    if not student:
        print("Estudiante no encontrado.")
        return
    print(f"Boletín de {student['name']} (Grado {student['grade']}):")
    grades = db['grades'].get(student_id, {})
    if not grades:
        print("No hay calificaciones registradas.")
    else:
        for subj, grade in grades.items():
            print(f" - {subj}: {grade}")

def generate_report(db):
    student_id = input("ID del estudiante para generar boletín: ").strip()
    student = db['students'].get(student_id)
    if not student:
        print("Estudiante no encontrado.")
        return
    grades = db['grades'].get(student_id, {})
    attendance = db['attendance'].get(student_id, {})
    avg = None
    if grades:
        avg = sum(grades.values())/len(grades)
    print("----- BOLETÍN -----")
    print(f"Alumno: {student['name']}  |  Grado: {student['grade']}")
    print("Calificaciones:")
    if grades:
        for subj, grade in grades.items():
            print(f"  {subj}: {grade}")
    else:
        print("  No hay calificaciones.")
    print("Asistencia reciente:")
    if attendance:
        for d in sorted(attendance.keys())[-10:]:
            print(f"  {d}: {attendance[d]}")
    else:
        print("  No hay registros de asistencia.")
    if avg is not None:
        print(f"Promedio: {avg:.2f}")
    print("-------------------")

def main():
    db = load_db()
    while True:
        print("\n--- SISTEMA ACADÉMICO (BAJA FIDELIDAD) ---")
        print("1) Registrar estudiante")
        print("2) Registrar nota")
        print("3) Registrar asistencia")
        print("4) Consultar calificaciones")
        print("5) Generar boletín (texto)")
        print("6) Salvar y salir")
        choice = input("Opción: ").strip()
        if choice == '1':
            register_student(db)
        elif choice == '2':
            record_grade(db)
        elif choice == '3':
            record_attendance(db)
        elif choice == '4':
            consult_grades(db)
        elif choice == '5':
            generate_report(db)
        elif choice == '6':
            save_db(db)
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()