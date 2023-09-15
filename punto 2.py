import numpy as np
carreras = ['ingenieria de sistemas', 'medicina', 'arquitectura', 'ingenieria quimica', 'ingenieria metalurgica', 'ingenieria civil', 'ingenieria biomedica', 'ingenieria mecanica', 'derecho']
np.random.seed(0) 
num_estudiantes = 6500 
codigos = np.arange(1, num_estudiantes + 1)
nombres = np.random.choice(['Juan', 'Maria', 'Luisa', 'Marta', 'Carolina', 'Daniel', 'Gabbriel', 'Pedro', 'Ana', 'Luis'], num_estudiantes)
carrera_alumnos = np.random.choice(carreras, num_estudiantes)
promedios = np.random.uniform(2.0, 5.0, num_estudiantes)
estudiantes = []
for codigo, nombre, carrera, promedio in zip(codigos, nombres, carrera_alumnos, promedios):
    estudiante = {
        'codigo': codigo,
        'nombre': nombre,
        'carrera': carrera,
        'promedio': promedio
    }
    estudiantes.append(estudiante)
print("los 30 primeros estudiantes")
for estudiante in estudiantes[:30]:
    print(estudiante)
