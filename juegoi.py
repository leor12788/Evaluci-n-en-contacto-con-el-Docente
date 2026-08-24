# Ahorcado - Proyecto Integrador (Logica de Programacion)
# Version de consola. Usa unicamente lo visto en las 4 unidades del curso:
# variables, tipos de datos, condicionales, bucles, listas, diccionarios y funciones.
# La "mejora visual" se logra con codigos de color ANSI (caracteres especiales dentro
# de un print normal) y un diccionario que guarda el dibujo del ahorcado en cada etapa,
# sin usar tkinter, clases ni interfaces graficas.
 
import random
 
# ---------- colores de consola (solo texto, no es una libreria nueva) ----------
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
CIAN = "\033[96m"
NEGRITA = "\033[1m"
FIN = "\033[0m"
 
# lista de palabras posibles
PALABRAS = [
    "python", "programacion", "algoritmo", "variable", "funcion",
    "computadora", "desarrollo", "software", "diagrama", "logica",
]
 
INTENTOS_INICIALES = 6
 
# diccionario: a cada cantidad de intentos fallidos (0 a 6) le corresponde
# un dibujo del ahorcado hecho con texto (arte ASCII)
DIBUJOS_AHORCADO = {
    0: """
   +---+
   |   |
       |
       |
       |
       |
  =========""",
    1: """
   +---+
   |   |
   O   |
       |
       |
       |
  =========""",
    2: """
   +---+
   |   |
   O   |
   |   |
       |
       |
  =========""",
    3: """
   +---+
   |   |
   O   |
  /|   |
       |
       |
  =========""",
    4: """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
  =========""",
    5: """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
  =========""",
    6: """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
  =========""",
}
 
# ---------- funciones de logica del juego (identicas a los Pasos 1 y 2) ----------
 
def elegir_palabra():
    # elige una palabra al azar de la lista
    indice = random.randint(0, len(PALABRAS) - 1)
    return PALABRAS[indice]
 
 
def crear_palabra_oculta(palabra):
    # arma la lista de guiones, uno por cada letra
    palabra_oculta = []
    for i in range(len(palabra)):
        palabra_oculta.append("_")
    return palabra_oculta
 
 
def letra_valida(letra):
    # valida: un solo caracter y alfabetico
    if len(letra) == 1 and letra.isalpha():
        return True
    else:
        return False
 
 
def letra_ya_usada(letra, letras_usadas):
    # recorre la lista de letras usadas buscando coincidencia
    indice = 0
    while indice < len(letras_usadas):
        if letras_usadas[indice] == letra:
            return True
        indice = indice + 1
    return False
 
 
def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    # revela las posiciones donde la palabra tiene esa letra
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
    return palabra_oculta
 
 
def palabra_completa(palabra_oculta):
    return "_" not in palabra_oculta
 
 
# ---------- funciones de presentacion (solo print, sin interfaz grafica) ----------
 
def mostrar_titulo():
    print(CIAN + NEGRITA + "\n===================================")
    print("           EL AHORCADO")
    print("===================================" + FIN)
 
 
def mostrar_instrucciones():
    print("Reglas del juego:")
    print("- Hay una palabra oculta, letra por letra.")
    print("- En cada turno ingresas una letra.")
    print("- Tienes 6 intentos fallidos antes de perder.")
    print()
 
 
def mostrar_dibujo(intentos_fallidos):
    # busca en el diccionario el dibujo que corresponde a esta cantidad de fallos
    print(AMARILLO + DIBUJOS_AHORCADO[intentos_fallidos] + FIN)
 
 
def mostrar_estado(palabra_oculta, letras_usadas, intentos):
    print(NEGRITA + "\nPalabra: " + FIN + " ".join(palabra_oculta))
    print("Letras usadas: " + ", ".join(letras_usadas))
    print("Intentos restantes: " + str(intentos))
 
 
# ---------- flujo de una partida ----------
 
def jugar_partida():
    palabra = elegir_palabra()
    palabra_oculta = crear_palabra_oculta(palabra)
    letras_usadas = []
    intentos = INTENTOS_INICIALES
    intentos_fallidos = 0
 
    while intentos > 0 and palabra_completa(palabra_oculta) == False:
        mostrar_dibujo(intentos_fallidos)
        mostrar_estado(palabra_oculta, letras_usadas, intentos)
 
        letra = input("\nIngresa una letra: ").lower()
 
        if letra_valida(letra) == False:
            print(ROJO + "Ingresa una sola letra valida." + FIN)
            continue
 
        if letra_ya_usada(letra, letras_usadas) == True:
            print(ROJO + "Ya usaste esa letra." + FIN)
            continue
 
        letras_usadas.append(letra)
 
        if letra in palabra:
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            print(VERDE + "Bien! Esa letra esta en la palabra." + FIN)
        else:
            intentos -= 1
            intentos_fallidos += 1
            print(ROJO + "Fallaste..." + FIN)
 
    mostrar_dibujo(intentos_fallidos)
 
    if palabra_completa(palabra_oculta):
        print(VERDE + NEGRITA + "\nGanaste! La palabra era: " + palabra + FIN)
        return True
    else:
        print(ROJO + NEGRITA + "\nPerdiste. La palabra era: " + palabra + FIN)
        return False
 
 
# ---------- programa principal ----------
 
def main():
    mostrar_titulo()
    mostrar_instrucciones()
    input("Presiona ENTER para comenzar...")
 
    partidas_ganadas = 0
    partidas_perdidas = 0
    jugar_de_nuevo = "s"
 
    while jugar_de_nuevo == "s":
        resultado = jugar_partida()
 
        if resultado == True:
            partidas_ganadas += 1
        else:
            partidas_perdidas += 1
 
        print(NEGRITA + "\nMarcador -> Ganadas: " + str(partidas_ganadas) +
              "   Perdidas: " + str(partidas_perdidas) + FIN)
 
        jugar_de_nuevo = input("\nJugar de nuevo? (s/n): ").lower()
 
    print(CIAN + "\nGracias por jugar!" + FIN)
 
 
if __name__ == "__main__":
    main()