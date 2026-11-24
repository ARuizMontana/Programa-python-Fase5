# ==============================================================================
# Nombre del Estudiante: Anderson Fabian Ruiz Montaña
# Grupo: 213022A_132
# Programa: Ingeniería de Telecomunicaciones
# Curso: Fundamentos de Programación - Fase 5 (Evaluación Final POA)
# Código Fuente: Autoría Propia
# ==============================================================================

# Matriz de inventario con 5 artículos:
# [Código del artículo, Nombre del artículo, Stock actual, Stock mínimo requerido]
inventario = [
    ["A01", "Cable UTP Cat 6A", 15, 25],
    ["A02", "Conector RJ45", 120, 100],
    ["A03", "Patch Panel", 4, 10],
    ["A04", "Cinta aislante", 30, 30],
    ["A05", "Amarres plasticos", 18, 50]
]


def calcular_cantidad_pedir(stock_actual, stock_minimo):
    # Si el stock actual es menor que el mínimo requerido, calculamos la diferencia
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        # Si el stock actual es mayor o igual al mínimo, no se necesita pedir nada
        cantidad_a_pedir = 0

    return cantidad_a_pedir


print("--- REPORTE DE REABASTECIMIENTO DE INVENTARIO ---")

# Recorremos cada fila (cada artículo) de la matriz
for fila in inventario:
    nombre_articulo = fila[1]
    stock_actual = fila[2]
    stock_minimo = fila[3]

    # Llamamos a la función para obtener la cantidad exacta a pedir
    cantidad_a_pedir = calcular_cantidad_pedir(stock_actual, stock_minimo)

    # Mostramos el nombre del artículo y la cantidad a solicitar
    print("Artículo:", nombre_articulo, "| Cantidad a pedir:", cantidad_a_pedir)