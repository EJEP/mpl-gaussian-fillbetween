import numpy as np
from matplotlib import pyplot as plt

def do_gaussian_fill(x, y, ax, sig, n_sig, m_steps, color='C0'):
    """Fill the region around a curve with Gaussian shading.

    Parameters
    ----------
    x : array or array-like
        x data to plot
    y : array or array-like
        y data to plot
    ax : matplotlib axis object
        Axis on which to plot the data
    sig : scalar or array
        Standard deviation of y data.
    n_sig : float
        Number of standard deviations away from `y` data to shade
    m_steps : int
        Number of steps to use for shading
    color : matplotlib color
    """

    for i in range(0, m_steps):
        bottom = y + ((i * n_sig * sig) / m_steps)
        top = y + (((i + 1) * n_sig * sig) / m_steps)

        bottom_2= y - ((i * n_sig * sig) / m_steps)
        top_2 = y - (((i + 1) * n_sig * sig) / m_steps)

        mid = (top + bottom) / 2
        dist = (((2*i) +1) * n_sig) / (2 * m_steps)

        alpha = np.exp(-1 * dist * dist / 2)

        ax.fill_between(x, top, bottom, alpha=alpha, color=color, linewidth=0)
        ax.fill_between(x, top_2, bottom_2, alpha=alpha, color=color,
                        linewidth=0)

