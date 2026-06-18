"""
Configuración y parámetros del experimento.
"""

# Parámetros físicos
VELOCIDAD_INICIAL = 13.0          # velocidad inicial de la bola (m/s)
POSICION_MONO_X = 6.9             # posición horizontal del mono (m)
POSICION_MONO_Y = 4.0             # altura inicial del mono (m)
ALTURA_LANZAMIENTO = 0.0          # altura del cañón (m)
GRAVEDAD = 9.8                    # gravedad (m/s²)

# Parámetros de animación
TIEMPO_EXTRA = 1.15               # factor de tiempo extra para ver el final
NUM_FRAMES = 300                  # número de frames para la animación
INTERVALO_MS = 20                 # milisegundos entre frames
ESTELA_TAMANO = 20                # número de frames para la estela

# Colores (formato hex)
COLOR_FONDO = "#0f0f1a"
COLOR_EJE = "#444"
COLOR_TEXTO = "white"
COLOR_TRAYECTORIA = "#ffffff20"
COLOR_LINEA_APUNTADO = "#ff6b6b40"
COLOR_BOLA = "#4ecdc4"
COLOR_MONO = "#ffd93d"
COLOR_IMPACTO = "#ff6b6b"