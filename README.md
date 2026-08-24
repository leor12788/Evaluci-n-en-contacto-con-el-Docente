# Evaluci-n-en-contacto-con-el-Docente
Integrante
Leonel Fernando Ortega Tapia (proyecto individual)
Fecha
Agosto 2026
Objetivo del sistema

Ofrecer una forma más accesible y entretenida de practicar vocabulario mediante el clásico juego del Ahorcado, mejorando la experiencia de la consola con colores y un dibujo progresivo del ahorcado, de modo que jugar y aprender nuevas palabras sea más claro e intuitivo para cualquier persona.

Descripción de funcionalidades
Selección aleatoria de palabra: el sistema elige una palabra al azar de una lista predefinida (elegir_palabra()).
Palabra oculta: la palabra se muestra al usuario como una serie de guiones bajos, uno por letra (crear_palabra_oculta()).
Validación de letras: se verifica que lo ingresado sea una sola letra del alfabeto (letra_valida()) y que no haya sido usada antes (letra_ya_usada()).
Actualización de la palabra oculta: al acertar una letra, se revelan todas sus posiciones en la palabra (actualizar_palabra_oculta()).
Control de intentos: el jugador dispone de 6 intentos; cada letra fallida resta un intento y agrega una parte al dibujo del ahorcado.
Dibujo progresivo del ahorcado: un diccionario (DIBUJOS_AHORCADO) guarda el dibujo en arte ASCII para cada cantidad de fallos (0 a 6); mostrar_dibujo() busca y muestra el que corresponde en cada turno.
Detección de fin de partida: el sistema detecta automáticamente si el jugador ganó (palabra completa) o perdió (0 intentos restantes) y muestra el resultado.
Colores en consola: mejora agregada en este proyecto integrador — códigos ANSI (caracteres especiales dentro de print()) resaltan aciertos en verde, errores en rojo y el dibujo en amarillo, sin usar ninguna librería nueva.
Marcador de partidas: contador de partidas ganadas y perdidas durante la sesión, con la opción de volver a jugar sin cerrar el programa.
Cronograma de actividades

El proyecto se planificó a lo largo de las 8 semanas del curso, siguiendo el orden de las 4 unidades de la asignatura. Cada semana se relacionó con un tema específico del syllabus y con una actividad concreta dentro del desarrollo del Ahorcado:

Semana	Unidad	Tema de la asignatura	Actividad realizada en el proyecto
1	Unidad 1	Tema 1: Los Problemas	Se identificó el problema a resolver (hacer más accesible el aprendizaje de vocabulario) y se seleccionó el juego del Ahorcado como programa a desarrollar, aplicando los pasos de resolución de problemas mediante computadoras.
2	Unidad 1	Tema 2: Introducción al Entorno de Desarrollo	Se configuró el entorno de desarrollo (Python y VS Code) y se investigaron tipos de diagramas de funcionalidad y de arquitectura, eligiendo el diagrama de flujo y la arquitectura en capas para el proyecto.
3	Unidad 2	Tema 1: Manejo de Datos	Se definieron las variables y tipos de datos del juego: la palabra secreta, la palabra oculta (lista), las letras usadas (lista) y los intentos disponibles (entero).
4	Unidad 2	Tema 2: Algoritmos y Diagramas de Flujo	Se diseñaron los algoritmos y los diagramas de flujo de cada funcionalidad (elegir palabra, validar letra, actualizar palabra oculta, dibujar el ahorcado) antes de programarlos, y se configuró el repositorio en GitHub.
5	Unidad 3	Tema 1: Condicionales	Se implementaron las validaciones del juego con estructuras condicionales (letra válida, letra repetida, letra correcta o incorrecta) usando operadores relacionales y lógicos.
6	Unidad 3	Tema 2: Bucles	Se usaron bucles (for y while) para recorrer la palabra al construir la palabra oculta y para buscar letras dentro de la lista de letras ya usadas.
7	Unidad 4	Tema 1: Estructura de Datos	Se aplicaron listas para representar la palabra oculta y las letras usadas, como estructuras de datos base del sistema.
8	Unidad 4	Tema 2: Funciones	Se organizó todo el juego en funciones independientes (elegir_palabra, crear_palabra_oculta, letra_valida, mostrar_dibujo, etc.), se agregaron los colores de consola y el diccionario de dibujos, y se preparó la entrega final: repositorio en GitHub, documento del proyecto y presentación.
Estructura del repositorio
ahorcado.py          # código completo del juego (funciones de lógica + funciones de presentación)
diagramas/            # diagramas de arquitectura y de cada funcionalidad
Cómo ejecutar el juego

Solo requiere Python 3 (sin librerías adicionales).

python ahorcado.py

Se juega directamente en la consola: escribe una letra y presiona Enter.

Diagramas

En la carpeta diagramas/ se encuentra la leyenda de símbolos (00_leyenda) y un diagrama por cada funcionalidad principal del sistema: arquitectura general, main(), jugar_partida(), validaciones (letra_valida, letra_ya_usada), actualizar_palabra_oculta() y mostrar_dibujo().
