import sys  # Se importa el modulo sys obtener los argumentos por consola, pero,
# en estricto rigor, no se utilizan las librerías prohibidas.
import os.path
from imprimir_tablero import imprimir_tablero
from tablero import Tablero

if __name__ == "__main__":
    # Intente hacer "python3 main.py hola mundo"
    argumentos_por_consola = sys.argv
    if len(argumentos_por_consola) != 3:  # Comprueba que los argumentos sean exactamente 2
        print('')
        print('Cantidad de argumentos inválida, debe introducir 2\n')
        sys.exit()
    nombre_usuario = str(argumentos_por_consola[1])
    nombre_tablero = str(argumentos_por_consola[2])
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"

    # No he verificado explícitamente que el usuario pueda
    # contener tildes u otros carcateres especiales
    # válidos en el idioma español, porque el enunciado
    # no lo especifica, sólo indica que el usuario debe
    # tener letras del alfabeto.
    def Verificar_nombre_usuario(nombre_usuario: str) -> bool:
        if len(nombre_usuario) >= 4:
            for i in range(len(nombre_usuario)):
                if nombre_usuario[i].lower() not in alfabeto:
                    return False
            return True
        else:
            return False

    def Verificar_nombre_tablero(nombre_tablero: str) -> (bool, list):
        tablero_actual = []
        with open("tableros.txt", "r") as tableros:
            for tablero in tableros:
                tablero = tablero.split(',')
                if tablero[0] == nombre_tablero:
                    nombre_tablero = str(tablero[0])
                    for idx, element in enumerate(tablero):
                        if idx >= 3:
                            if '\n' in element:
                                element = element.replace('\n', '')
                                tablero[-1] = element
                                tablero_actual = tablero
                    return True, tablero
            return False, tablero_actual

    usuario_validado = Verificar_nombre_usuario(nombre_usuario)
    (tablero_validado, tablero_actual) = Verificar_nombre_tablero(
        nombre_tablero)

    def funcion_principal(usuario_validado: bool,
                          tablero_validado: bool, tablero_actual: list) -> None:
        # Verificar validez del usuario
        if usuario_validado == False:
            print('Usuario invalido')
        # Verificar validez del tablero
        if tablero_validado == False:
            print('Tablero invalido')
        if usuario_validado == False or tablero_validado == False:
            exit()
        elif usuario_validado == True and tablero_validado == True:
            try:
                print('')
                print('================================')
                print(f"Hola {nombre_usuario}!\n")
                print('*** Menú de Acciones ***\n')
                print('[1] Mostrar tablero')
                print('[2] Limpiar tablero')
                print('[3] Solucionar tablero')
                print('[4] Salir del programa')
                print('================================')
                print('')
                print('Indique su opción (1, 2, 3 o 4):')
                input_usuario = input("Opcion:")

                try:
                    input_usuario = int(input_usuario)
                except ValueError:
                    print('Ha introducido una opción inválida\n')
                    print('Por favor, vuelva a intentarlo\n')
                    exit()
                try:
                    if input_usuario not in [1, 2, 3, 4] or input_usuario == '':
                        print('Ha introducido una opción inválida\n')
                        print('Por favor, vuelva a intentarlo\n')
                        exit()
                    elif input_usuario == 1:
                        imprimir_tablero(tablero_actual[3:])
                        print('')
                        funcion_principal(usuario_validado,
                                          tablero_validado, tablero_actual)
                    elif input_usuario == 2:
                        print('')
                        print('El tablero: \n')
                        print(tablero_actual[3:], '\n')

                        print('Ha sido limpiado, el nuevo tablero es: \n')
                        tablero_actual_copia = tablero_actual
                        with open("tableros.txt", "r") as tableros:
                            for tablero in tableros:
                                if nombre_tablero in tablero:
                                    # print(tablero_actual[3:])
                                    for idx, element in enumerate(tablero_actual):
                                        if element == 'PP':
                                            tablero_actual_copia[idx] = '--'
                                    print(tablero_actual_copia[3:])
                                    tablero = tablero_actual_copia
                                    tablero_actual = tablero
                                    funcion_principal(usuario_validado,
                                                      tablero_validado, tablero_actual)
                    elif input_usuario == 3:
                        # Llama correctamente al metodo solucionar_tablero
                        # pero éste no está implementado.
                        print('Funcion no implementada por el momento\n')
                        Tablero.solucionar(tablero_actual)
                        funcion_principal(usuario_validado,
                                          tablero_validado, tablero_actual)
                    elif input_usuario == 4:
                        print('Gracias por usar el programa\n')
                        exit()
                    else:
                        print('')
                        print('Ha introducido una opción inválida\n')
                        print('Por favor, vuelva a intentarloo\n')
                        exit()
                except ValueError:
                    print('Ha introducido una opción inválida\n')
                    print('Por favor, vuelva a intentarlooo\n')
                    exit()
            except KeyboardInterrupt:
                print('')
                print('')
                print('Gracias por usar el programa\n')
                exit()

    funcion_principal(usuario_validado, tablero_validado, tablero_actual)
