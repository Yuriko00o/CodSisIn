def draw_snake(body_parts):
    if not body_parts or not all(isinstance(part, int) and part > 0 for part in body_parts):
        return []

    # Calcular el ancho total de la serpiente
    width = max(body_parts)

    # Calcular el alto total de la serpiente (número de filas)
    height = len(body_parts)

    # Inicializar la matriz con espacios vacíos
    grid = [[' ' for _ in range(width)] for _ in range(height)]

    for i, length in enumerate(body_parts):
        if i % 2 == 0:  # Parte par (izquierda a derecha, la cabeza de la serpiente hacia la izquierda)
            # La cabeza está en la parte más a la izquierda de la primera sección
            if i == 0:
                grid[i][0] = 'H'
                for j in range(1, length):
                    grid[i][j] = 'x'
            else:
                for j in range(length):
                    grid[i][j] = 'x'
        else:  # Parte impar (derecha a izquierda)
            for j in range(length):
                grid[i][width - 1 - j] = 'x'

    # Colocar la cola
    if len(body_parts) % 2 == 1:  # Última parte fue de izquierda a derecha
        grid[height - 1][body_parts[-1] - 1] = 'T'
    else:  # Última parte fue de derecha a izquierda
        grid[height - 1][width - body_parts[-1]] = 'T'

    return grid

def print_snake(snake_grid):
    for row in snake_grid:
        print("".join(row))

#Serpiente simple
body_parts1 = [3, 2, 4]
snake1 = draw_snake(body_parts1)
if snake1:
    print("Serpiente 1:")
    print_snake(snake1)
    print("-" * 20)
