"""
Lógica de animación del proyecto.
"""
import matplotlib.animation as animation
from config import NUM_FRAMES, INTERVALO_MS, ESTELA_TAMANO
from physics import posicion_bola, posicion_mono, detectar_impacto, generar_trayectoria, calcular_angulo
from visualization import marcar_impacto


def crear_actualizador(ax, arreglo_tiempos, tiempo_impacto, estela_bola, punto_bola, punto_mono, texto_tiempo):
    """
    Crea la función de actualización para la animación.

    Args:
        ax: Axes de matplotlib
        arreglo_tiempos: Array de tiempos para la animación
        tiempo_impacto: Tiempo estimado de impacto
        estela_bola: Elemento gráfico de la estela
        punto_bola: Elemento gráfico de la bola
        punto_mono: Elemento gráfico del mono
        texto_tiempo: Texto para mostrar el tiempo

    Returns:
        Función de actualización para FuncAnimation
    """
    # Arrays precalculados para la estela
    angulo = calcular_angulo()
    tray_x, tray_y = generar_trayectoria(arreglo_tiempos, angulo)
    impacto_marcado = [False]  # closure para marcar impacto una vez

    def update(frame):
        t = arreglo_tiempos[frame]

        # Posiciones actuales
        xb, yb = posicion_bola(t, angulo)
        xm, ym = posicion_mono(t)

        # Actualizar estela (últimos N frames)
        inicio = max(0, frame - ESTELA_TAMANO)
        estela_bola.set_data(tray_x[inicio:frame], tray_y[inicio:frame])

        # Actualizar posiciones de los objetos
        punto_bola.set_data([xb], [yb])
        punto_mono.set_data([xm], [ym])

        # Actualizar texto de tiempo
        texto_tiempo.set_text(f"t = {t:.3f} s")

        # Detectar y marcar impacto
        if not impacto_marcado[0] and detectar_impacto(t, tiempo_impacto):
            marcar_impacto(ax, xb, ym)
            impacto_marcado[0] = True

        return estela_bola, punto_bola, punto_mono, texto_tiempo

    return update


def crear_animacion(fig, update_func):
    """
    Crea la animación de matplotlib.

    Args:
        fig: Figura de matplotlib
        update_func: Función de actualización

    Returns:
        Objeto Animation
    """
    return animation.FuncAnimation(
        fig,
        update_func,
        frames=NUM_FRAMES,
        interval=INTERVALO_MS,
        blit=False,
        repeat=False
    )