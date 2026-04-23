import os
os.system("cls")


IVA = 0.19
PRESUPUESTO_MAXIMO = 50000000
metros_cuadrados = 0
costo_metro_cuadrado = 0
cantidad_trabajadores = 0
pago_trabajador = 0

nombre = str(input("Ingrese el nombre del proyecto: "))
while True:
    try:
        while metros_cuadrados <= 0:
            metros_cuadrados = int(input("Ingrese los metros cuadrados a construir: "))
        while costo_metro_cuadrado <= 0:
            costo_metro_cuadrado = int(input("Ingrese el costro por metro cuadrado: "))
        while cantidad_trabajadores <= 0:
            cantidad_trabajadores = int(input("Ingrese la cantidad de trabajadores: "))
        while pago_trabajador <= 0:
            pago_trabajador = int(input("ingrese el pago por trabajador: "))

        costo_materiales = metros_cuadrados * costo_metro_cuadrado
        costo_mano_obra = cantidad_trabajadores * pago_trabajador
        costo_neto = costo_materiales + costo_mano_obra
        costo_IVA = costo_neto * IVA
        costo_neto_con_IVA = costo_IVA + costo_neto

        if costo_neto_con_IVA <= PRESUPUESTO_MAXIMO:
            estado = "Dentro del presupuesto"
        elif costo_neto_con_IVA >= (PRESUPUESTO_MAXIMO*1.10):
            estado= "Presupuesto ajustado"
        else:
            estado = "Fuera de presupuesto"    

        print("-------------RESUMEN------------")
        print(f"Nombre del proyecto: {nombre}")
        print(f"Costo total: {round(costo_neto_con_IVA,2)}")
        print(f"Estado del proyecto: {estado}")
        break
    except:
        print("ingrese los datos correctamente, intente nuevamente")
