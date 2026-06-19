"""
Configuración de visualización y gráficos.
"""
import matplotlib.pyplot as plt
from config import (
    COLOR_FONDO,
    COLOR_EJE,
    COLOR_TEXTO,
    COLOR_TRAYECTORIA,
    COLOR_LINEA_APUNTADO,
    COLOR_BOLA,
    COLOR_MONO,
    COLOR_IMPACTO,
    POSICION_MONO_X,
    POSICION_MONO_Y,
    ALTURA_LANZAMIENTO
)


def crear_figura():
    """Crea y configura la figura de matplotlib."""
    fig, ax = plt.subplots(figsize=(10, 6))
    return fig, ax


def configurar_ejes(ax):
    """Configura los ejes con el estilo del proyecto."""
    # Colores de fondo
    fig = ax.figure
    fig.patch.set_facecolor(COLOR_FONDO)
    ax.set_facecolor(COLOR_FONDO)

    # Límites
    ax.set_xlim(-0.3, POSICION_MONO_X + 1)
    ax.set_ylim(-0.5, POSICION_MONO_Y + 1.5)

    # Etiquetas
    ax.set_xlabel("Distancia horizontal (m)", color=COLOR_TEXTO)
    ax.set_ylabel("Altura (m)", color=COLOR_TEXTO)
    ax.tick_params(colors=COLOR_TEXTO)

    # Bordes
    for spine in ax.spines.values():
        spine.set_edgecolor(COLOR_EJE)

    # Título
    ax.set_title("Shoot the Monkey — independencia de componentes",
                 color=COLOR_TEXTO, pad=12)


def dibujar_trayectoria(ax, tray_x, tray_y):
    """Dibuja la línea de trayectoria de la bola."""
    ax.plot(tray_x, tray_y, color=COLOR_TRAYECTORIA, linewidth=1, linestyle="--")


def dibujar_linea_apuntado(ax):
    """Dibuja la línea de disparo inicial."""
    ax.plot([0, POSICION_MONO_X], [ALTURA_LANZAMIENTO, POSICION_MONO_Y],
            color=COLOR_LINEA_APUNTADO, linewidth=1, linestyle=":",
            label="línea de apontado")


def crear_elementos_animados(ax):
    """Crea los elementos que serán animados."""
    estela_bola, = ax.plot([], [], color=COLOR_BOLA, linewidth=1.5, alpha=0.5)
    punto_bola, = ax.plot([], [], "o", color=COLOR_BOLA, markersize=8, label="Bola")
    punto_mono, = ax.plot([], [], "s", color=COLOR_MONO, markersize=12, label="Mono")

    return estela_bola, punto_bola, punto_mono


def crear_texto_tiempo(ax):
    """Crea el texto que mostrará el tiempo."""
    return ax.text(0.02, 0.95, "", transform=ax.transAxes,
                   color=COLOR_TEXTO, fontsize=10, va="top")


def configurar_leyenda(ax):
    """Configura la leyenda del gráfico."""
    ax.legend(loc="upper right", facecolor="#1a1a2e",
              labelcolor=COLOR_TEXTO, edgecolor=COLOR_EJE)


def marcar_impacto(ax, x, y):
    """Marca el punto de impacto en el gráfico."""
    ax.plot(x, y, "*", color=COLOR_IMPACTO, markersize=22, zorder=5)
    ax.text(x + 0.1, y + 0.2, "¡IMPACTO!", color=COLOR_IMPACTO,
            fontsize=12, fontweight="bold")