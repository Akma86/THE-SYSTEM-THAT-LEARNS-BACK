"""
Matplotlib and Seaborn plotting helpers for cyberpunk telemetry.
"""
import matplotlib.pyplot as plt


def apply_cyber_plot_style(fig, ax, bg_color="#040914"):
    """Applies a crisp dark cyberpunk theme to matplotlib figures and axes."""
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    ax.tick_params(colors="#94A3B8", labelsize=9)
    for spine in ax.spines.values():
        spine.set_color("#1E293B")
        spine.set_linewidth(1.2)
    ax.grid(color="#1E293B", linestyle="--", linewidth=0.8, alpha=0.6)
    return fig, ax
