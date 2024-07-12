import sueldos

def menu():
    while True:
        print("1. Asignar sueldos aleatorios")
        print("2. clasficar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. salir del programa")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                sueldos.asignar_sueldos_aleatorios()
            elif opcion == 2:
                sueldos.clasificar_sueldos_()
            elif opcion == 3:
                sueldos.Ver_estadisticas()
            elif opcion == 4:
                sueldos.reporte_de_sueldos()
            elif opcion == 5:
                sueldos.salir_del_programa()
                print("saliste exitosamente.")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    menu()


