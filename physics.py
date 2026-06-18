"""
Cálculos físicos del movimiento de proyectiles.
"""
import numpy as np
from config import (
    VELOCIDAD_INICIAL,
    POSICION_MONO_X,
    POSICION_MONO_Y,
    ALTURA_LANZAMIENTO,
    GRAVEDAD,
    TIEMPO_EXTRA,
    NUM_FRAMES
)


def calcular_angulo():
    """Calcula el ángulo de disparo hacia el mono."""
    return np.arctan2(POSICION_MONO_Y - ALTURA_LANZAMIENTO, POSICION_MONO_X)


def calcular_tiempo_impacto(angulo):
    """Calcula el tiempo hasta el impacto."""
    return POSICION_MONO_X / (VELOCIDAD_INICIAL * np.cos(angulo))


def calcular_tiempo_total(tiempo_impacto):
    """Calcula el tiempo total de la animación."""
    return tiempo_impacto * TIEMPO_EXTRA


def generar_array_tiempos(tiempo_total):
    """Genera el array de tiempos para la animación."""
    return np.linspace(0, tiempo_total, NUM_FRAMES)


def posicion_bola(t, angulo):
    """Calcula la posición de la bola en un tiempo t."""
    x = VELOCIDAD_INICIAL * np.cos(angulo) * t
    y = ALTURA_LANZAMIENTO + VELOCIDAD_INICIAL * np.sin(angulo) * t - 0.5 * GRAVEDAD * t**2
    return x, y


def posicion_mono(t):
    """Calcula la posición del mono (caída libre) en un tiempo t."""
    x = POSICION_MONO_X  # el mono no se mueve horizontalmente
    y = POSICION_MONO_Y - 0.5 * GRAVEDAD * t**2
    return x, y


def generar_trayectoria(arreglo_tiempos, angulo):
    """Genera las posiciones completas de la bola."""
    x = VELOCIDAD_INICIAL * np.cos(angulo) * arreglo_tiempos
    y = ALTURA_LANZAMIENTO + VELOCIDAD_INICIAL * np.sin(angulo) * arreglo_tiempos - 0.5 * GRAVEDAD * arreglo_tiempos**2
    return x, y


def generar_caida_mono(arreglo_tiempos):
    """Genera las posiciones del mono en caída libre."""
    x = np.full_like(arreglo_tiempos, POSICION_MONO_X)
    y = POSICION_MONO_Y - 0.5 * GRAVEDAD * arreglo_tiempos**2
    return x, y


def detectar_impacto(t, tiempo_impacto, umbral=0.98):
    """Detecta si ha ocurrido el impacto."""
    return t >= tiempo_impacto * umbral