from pieza_explosiva import PiezaExplosiva
import os


class Tablero:
    def __init__(self, tablero: list) -> None:
        # filas         #columnas
        self.dimensiones = [len(tablero), len(tablero[0])]
        self.tablero = tablero

    @property
    def desglose(self) -> list:
        list_to_return = []
        explosive_piece = 0
        pawns = 0
        empty = 0
        for row in self.tablero:
            for col in row:
                if col == '--':
                    empty += 1
                elif col == 'PP':
                    pawns += 1
                else:
                    explosive_piece += 1
        list_to_return.append(int(explosive_piece))
        list_to_return.append(int(pawns))
        list_to_return.append(int(empty))
        return list_to_return

    @property
    def peones_invalidos(self) -> int:
        pawns = []
        counter_outside = 0
        invalid_pawns = 0
        for row in self.tablero:
            for idx, cell in enumerate(row):
                if cell == 'PP':
                    pawns.append((counter_outside, idx))
            counter_outside += 1
        for pawn in pawns:
            neighbours = 0
            y, x = pawn  # Coords of the actual pawn
            try:
                if self.tablero[y][x-1] == 'PP' and x != 0:
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.tablero[y][x+1] == 'PP':
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.tablero[y-1][x] == 'PP' and y != 0:
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.tablero[y+1][x] == 'PP':
                    neighbours += 1
            except IndexError:
                pass
            if neighbours > 1:
                invalid_pawns += 1
        return int(invalid_pawns)

    @property
    def piezas_explosivas_invalidas(self) -> int:
        invalidas = 0
        piezas_explosivas = []  # Lista de tuplas (fila, columna, tipo)
        for idx_fila, fila in enumerate(self.tablero):
            for idx_col, col in enumerate(fila):
                if col != '--' and col != 'PP':
                    piezas_explosivas.append((idx_fila, idx_col, str(col)))
        for pieza in piezas_explosivas:
            fila_pieza, col_pieza, tipo = pieza  # fila, columna, tipo
            dimension_horizontal = self.dimensiones[1]
            dimension_vertical = self.dimensiones[0]
            max_dimension = max(dimension_horizontal, dimension_vertical)

            if tipo[0] == 'V':
                contador_alcances = 1  # Empieza en 1 contando su misma casilla
                for i in range(1, max_dimension):  # Alcance
                    try:
                        if self.tablero[fila_pieza-i][col_pieza] != 'Null' \
                                and fila_pieza-i >= 0:
                            contador_alcances += 1
                        else:
                            break  # Si no es -- o PP, no puede seguir
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                for i in range(1, max_dimension):  # Alcance
                    try:
                        if self.tablero[fila_pieza+i][col_pieza] != 'Null':
                            contador_alcances += 1
                        else:
                            break  # Si no es -- o PP, no puede seguir
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                if int(tipo[1:]) > contador_alcances:
                    invalidas += 1

            if tipo[0] == 'H':
                contador_alcances = 1  # Empieza en 1 contando su misma casilla
                for i in range(1, max_dimension):  # Alcance
                    try:
                        if self.tablero[fila_pieza][col_pieza-i] != 'Null' \
                                and col_pieza-i >= 0:
                            contador_alcances += 1
                        else:
                            break  # Si no es -- o PP, no puede seguir
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                for i in range(1, max_dimension):  # Alcance
                    try:
                        if self.tablero[fila_pieza][col_pieza+i] != 'Null':
                            contador_alcances += 1
                        else:
                            break  # Si no es -- o PP, no puede seguir
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                if int(tipo[1:]) > contador_alcances:
                    invalidas += 1

            elif tipo[0] == 'R':
                contador_alcances = 1  # Empieza en 1 contando su misma casilla
# CASO H
                for i in range(1, max_dimension):  # Alcance
                    try:
                        if self.tablero[fila_pieza][col_pieza-i] != 'Null' \
                                and col_pieza-i >= 0:
                            contador_alcances += 1
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                for i in range(1, max_dimension):  # Alcance
                    try:
                        if self.tablero[fila_pieza][col_pieza+i] != 'Null':
                            contador_alcances += 1
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
# CASO V
                for i in range(1, max_dimension):  # Alcance
                    try:
                        if self.tablero[fila_pieza-i][col_pieza] != 'Null' \
                                and fila_pieza-i >= 0:
                            contador_alcances += 1
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                for i in range(1, max_dimension):  # Alcance
                    try:
                        if self.tablero[fila_pieza+i][col_pieza] != 'Null':
                            contador_alcances += 1
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
# CASO R
                for i in range(1, max_dimension):
                    try:
                        if self.tablero[fila_pieza+i][col_pieza-i] != 'Null' \
                                and col_pieza-i >= 0:
                            contador_alcances += 1
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                for i in range(1, max_dimension):
                    try:
                        if self.tablero[fila_pieza+i][col_pieza+i] != 'Null':
                            contador_alcances += 1
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                for i in range(1, max_dimension):
                    try:
                        if self.tablero[fila_pieza-i][col_pieza-i] != 'Null' \
                                and fila_pieza-i >= 0 and col_pieza-i >= 0:
                            contador_alcances += 1
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                for i in range(1, max_dimension):
                    try:
                        if self.tablero[fila_pieza-i][col_pieza+i] != 'Null' \
                                and fila_pieza-i >= 0:
                            contador_alcances += 1
                    except IndexError:
                        pass  # Exception error indica que finaliza el tablero
                if int(tipo[1:]) > contador_alcances:
                    invalidas += 1
        return int(invalidas)

    @property
    def tablero_transformado(self) -> list:
        dimension_fila, dimension_col = [
            self.dimensiones[0], self.dimensiones[1]]
        tablero = self.tablero
        for fila in range(dimension_fila):
            for col in range(dimension_col):
                pieza = tablero[fila][col]
                posicion = [fila, col]
                if pieza != "--" and pieza != "PP":
                    pieza = PiezaExplosiva(
                        int(pieza[1:]), str(pieza[0]), posicion)
                    # Cambia la pieza en str por la pieza instanciada
                    tablero[fila][col] = pieza
        return tablero

    def celdas_afectadas(self, fila: int, columna: int) -> int:
        pieza_explosiva = fila, columna  # Posicion de la pieza explosiva
        dimension_vertical = self.dimensiones[0]
        dimension_horizontal = self.dimensiones[1]
        max_dimension = max(dimension_horizontal, dimension_vertical)
# Caso de tipo V
        if 'V' in self.tablero[fila][columna]:
            celdas_afectadas = 1  # Empieza en 1 contando su misma casilla
            distancia_vertical_abajo = abs(dimension_vertical-fila)
            for i in range(1, fila+1):
                try:
                    if self.tablero[fila-i][columna] != 'PP' and fila-i >= 0:
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero
            for i in range(1, distancia_vertical_abajo+1):
                try:
                    if self.tablero[fila+i][columna] != 'PP':
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero
            return celdas_afectadas
# Caso de tipo H
        elif 'H' in self.tablero[fila][columna]:
            celdas_afectadas = 1  # Empieza en 1 contando su misma casilla
            distancia_horizontal_der = abs(dimension_horizontal-columna)
            for i in range(1, columna+1):
                try:
                    if self.tablero[fila][columna-i] != 'PP' and columna-i >= 0:
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero
            for i in range(1, distancia_horizontal_der+1):
                try:
                    if self.tablero[fila][columna+i] != 'PP':
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero
            return celdas_afectadas
# Caso de tipo R
        elif 'R' in self.tablero[fila][columna]:
            celdas_afectadas = 1  # Empieza en 1 contando su misma casilla
# Codigo para contar casillas oblicuas de R
            for i in range(1, max_dimension):
                try:
                    if self.tablero[fila+i][columna-i] != 'PP' and columna-i >= 0:
                        celdas_afectadas += 1
                    else:
                        break  # Fin del tablero o hay un peon
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero
            for i in range(1, max_dimension):
                try:
                    if self.tablero[fila+i][columna+i] != 'PP':
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero
            for i in range(1, max_dimension):
                try:
                    if self.tablero[fila-i][columna-i] != 'PP' and fila-i >= 0 \
                            and columna-i >= 0:
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero

            for i in range(1, max_dimension):
                try:
                    if self.tablero[fila-i][columna+i] != 'PP' and fila-i >= 0:
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero

# Codigo para contar las casillas horizontales de R
            distancia_horizontal_der = abs(dimension_horizontal-columna)
            for i in range(1, max_dimension):
                try:
                    if self.tablero[fila][columna-i] != 'PP' and columna-i >= 0:
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero
            for i in range(1, max_dimension):
                try:
                    if self.tablero[fila][columna+i] != 'PP':
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero

# Codigo para contar las casillas verticales de R
            distancia_vertical_abajo = abs(dimension_vertical-fila)
            for i in range(1, max_dimension):
                try:
                    if self.tablero[fila-i][columna] != 'PP' and fila-i >= 0:
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero
            for i in range(1, max_dimension):
                try:
                    if self.tablero[fila+i][columna] != 'PP':
                        celdas_afectadas += 1
                    else:
                        break
                except IndexError:
                    pass  # Exception error indica que finaliza el tablero

            return celdas_afectadas
        else:
            return -1

    def limpiar(self) -> None:
        for row in (self.tablero):
            for idx, col in enumerate(row):
                if col == 'PP':
                    row[idx] = '--'
        return None

    def __str__(self):
        return str(self.tablero)

    def reemplazar(self, nombre_nuevo_tablero: str) -> bool:
        was_replaced = False
        with open('tableros.txt', 'r') as f:
            for line in f.readlines():
                if nombre_nuevo_tablero in str(line):
                    line = line.split(',')
                    self.dimensiones = [int(line[1]),
                                        int(line[2])]
                    nuevo_tablero = [line[i:i+self.dimensiones[1]]
                                     for i in range(3, len(line), self.dimensiones[1])]
                    for row in nuevo_tablero:
                        for idx, col in enumerate(row):
                            row[idx] = col.strip()
                    self.tablero = nuevo_tablero
                    was_replaced = True
                    return was_replaced
        return was_replaced

    def solucionar(self) -> list:
        return []
