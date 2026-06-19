"""
Punto de entrada principal del proyecto Shoot the Monkey.
"""
import numpy as np

from config import (
    VELOCIDAD_INICIAL,
    POSICION_MONO_X,
    POSICION_MONO_Y,
    ALTURA_LANZAMIENTO,
    GRAVEDAD
)
from physics import (
    calcular_angulo,
    calcular_tiempo_impacto,
    calcular_tiempo_total,
    generar_array_tiempos,
    generar_trayectoria,
    generar_caida_mono
)
from visualization import (
    crear_figura,
    configurar_ejes,
    dibujar_trayectoria,
    dibujar_linea_apuntado,
    crear_elementos_animados,
    crear_texto_tiempo,
    configurar_leyenda
)
from animation import crear_actualizador, crear_animacion


def main():
    # Cálculos físicos
    angulo = calcular_angulo()
    print(f"Ángulo de disparo: {np.degrees(angulo):.2f}°")

    tiempo_impacto = calcular_tiempo_impacto(angulo)
    print(f"Tiempo de impacto: {tiempo_impacto:.3f} s")

    tiempo_total = calcular_tiempo_total(tiempo_impacto)
    arreglo_tiempos = generar_array_tiempos(tiempo_total)

    # Generación de trayectorias
    tray_x, tray_y = generar_trayectoria(arreglo_tiempos, angulo)

    # Crear visualización
    fig, ax = crear_figura()
    configurar_ejes(ax)
    dibujar_trayectoria(ax, tray_x, tray_y)
    dibujar_linea_apuntado(ax)

    # Elementos animados
    estela_bola, punto_bola, punto_mono = crear_elementos_animados(ax)
    texto_tiempo = crear_texto_tiempo(ax)
    configurar_leyenda(ax)

    # Crear animación
    update_func = crear_actualizador(
        ax, arreglo_tiempos, tiempo_impacto,
        estela_bola, punto_bola, punto_mono, texto_tiempo
    )
    ani = crear_animacion(fig, update_func)

    # Mostrar
    import matplotlib.pyplot as plt
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()