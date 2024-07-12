import random
import csv


def generar_sueldos_aleatorios():
    random.randint(300000, 2500000)
    return sueldos

sueldos = generar_sueldos_aleatorios()
print(sueldos)

def asignar_sueldos_aleatorios():
    sueldos = generar_sueldos_aleatorios()
    print("\nSueldos asignados aleatoriamente:")
    for i, trabajador in enumerate(trabajadores):
        print(f"{trabajador}: {sueldos[i]}")

def clasificar_sueldos():
    menores_800000 = []
    entre_800000_y_2000000 = []
    superiores_2000000 = []

    for i, sueldo in enumerate(sueldos):
        if sueldo < 800000:
            menores_800000.append((trabajadores[i], sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800000_y_2000000.append((trabajadores[i], sueldo))
        else:
            superiores_2000000.append((trabajadores[i], sueldo))
    total_sueldos = sum(sueldos)

    print("\nSueldos menores a $800.000")
    print(f"TOTAL: {len(menores_800000)}")
    for trabajador, sueldo in menores_800000:
        print(f"Nombre empleado: {trabajador}, Sueldo: ${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(entre_800000_y_2000000)}")
    for trabajador, sueldo in entre_800000_y_2000000:
        print(f"Nombre empleado: {trabajador}, Sueldo: ${sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(superiores_2000000)}")
    for trabajador, sueldo in superiores_2000000:
        print(f"Nombre empleado: {trabajador}, Sueldo: {sueldo}")

trabajadores = ["andres trigo", "cecilia caro", "camila lopez", "natanael rebeco", 
                "javier rodriguez", "Laura Hernández", "cristiano ronaldo", 
                "Isabel caro", "Francisco sepulveda", "leonel andres"]