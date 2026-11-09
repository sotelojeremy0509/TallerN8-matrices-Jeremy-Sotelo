
ventas = [
    [12, 15, 10, 18],
    [8, 14, 16, 12],
    [20, 18, 15, 22]
]

def analizar_ventas():
    print("\n========== MATRIZ DE VENTAS ==========")

    for i in range(len(ventas)):
        print(f"\nVendedor {i + 1}:")
        for j in range(len(ventas[i])):
            print(f"Semana {j + 1}: {ventas[i][j]} millones")

   
    print("\n========== TOTAL POR VENDEDOR ==========")

    totales_vendedores = []

    for i in range(len(ventas)):
        total = 0
        for j in range(len(ventas[i])):
            total += ventas[i][j]

        totales_vendedores.append(total)
        print(f"Vendedor {i + 1}: {total} millones")

    # Total de ventas por semana
    print("\n========== TOTAL POR SEMANA ==========")

    totales_semanas = []

    for j in range(len(ventas[0])):
        total = 0
        for i in range(len(ventas)):
            total += ventas[i][j]

        totales_semanas.append(total)
        print(f"Semana {j + 1}: {total} millones")

   
    mayor_vendedor = max(totales_vendedores)
    posicion_vendedor = totales_vendedores.index(mayor_vendedor)

    print("\n========== MAYORES VENTAS ==========")
    print(f"Vendedor con mayores ventas: {posicion_vendedor + 1}")
    print(f"Total: {mayor_vendedor} millones")

  
    mayor_semana = max(totales_semanas)
    posicion_semana = totales_semanas.index(mayor_semana)

    print(f"Semana con mayores ventas: {posicion_semana + 1}")
    print(f"Total: {mayor_semana} millones")

    suma_total = 0
    cantidad = 0

    for fila in ventas:
        for valor in fila:
            suma_total += valor
            cantidad += 1

    promedio = suma_total / cantidad

    print("\n========== PROMEDIO GENERAL ==========")
    print(f"Promedio: {promedio:.2f} millones")



analizar_ventas()


print("\n========== MODIFICAR VENTA ==========")

vendedor = int(input("Ingrese el vendedor (1-3): "))
semana = int(input("Ingrese la semana (1-4): "))
nuevo_valor = float(input("Ingrese el nuevo valor: "))

if 1 <= vendedor <= 3 and 1 <= semana <= 4 and nuevo_valor >= 0:
    ventas[vendedor - 1][semana - 1] = nuevo_valor

    print("\nVenta modificada correctamente.")
    print("Resultados actualizados:")

    analizar_ventas()
else:
    print("Datos incorrectos. No se modificó la matriz.")
