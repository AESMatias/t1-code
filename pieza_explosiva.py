class PiezaExplosiva:
    def __init__(self, alcance: int, tipo: str, posicion: list) -> None:
        self.alcance = alcance
        self.tipo = tipo
        self.posicion = posicion

    def __str__(self) -> str:
        fila, columna = self.posicion
        texto = f"Soy la pieza {self.tipo}{self.alcance}\n"
        texto += f"\tEstoy en la fila {fila} y columna {columna}\n"
        return texto

    def verificar_alcance(self, fila: int, columna: int) -> bool:
        is_attainable = False
        fila_pieza, columna_pieza = self.posicion  # Coord of the actual piece

        # La variable maxima_posicion toma el valor de la posicion mas alejada
        # del tablero, lo que permite saber la distancia mas lejana que se debe
        # considerar para verificar si la pieza puede alcanzar la celda,
        # esto es util para ingresarlo en la funcion range de mas abajo,
        # y abarcar genericamente todos los casos posibles segun el contexto del problema.
        maxima_posicion = max(fila_pieza, columna_pieza, fila, columna)
        if self.tipo == 'V' and columna_pieza == columna:
            return True
        elif self.tipo == 'H' and fila == fila_pieza:
            return True
        elif self.tipo == 'R':
            # Se puede prescindir del *10, pero es mas seguro asi
            for i in range(maxima_posicion*10):
                if columna_pieza == columna:
                    is_attainable = True
                if fila == fila_pieza:
                    is_attainable = True
                elif fila_pieza == fila-i and columna_pieza == columna+i:
                    is_attainable = True
                elif fila_pieza == fila-i and columna_pieza == columna-i:
                    is_attainable = True
                elif fila_pieza == fila+i and columna_pieza == columna+i:
                    is_attainable = True
                elif fila_pieza == fila+i and columna_pieza == columna-i:
                    is_attainable = True
        return is_attainable


if __name__ == "__main__":
    """
    Ejemplos:

    Dado el siguiente tablero
    [
        ["--", "V2", "PP", "--", "H2"],
        ["H3", "--", "--", "PP", "R11"]
    ]

    """
    # # Ejemplo 1 - Pieza R11
    # pieza_1 = PiezaExplosiva(11, "R", [1, 4])
    # print(str(pieza_1))

    # # Ejemplo 2 - Pieza V2
    # pieza_2 = PiezaExplosiva(2, "V", [0, 1])
    # print(str(pieza_2))
