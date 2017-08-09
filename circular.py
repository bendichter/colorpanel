import matplotlib.pyplot as plt
import numpy as np

from colorpanel.utils import use_subplot_spec


def plot_clock(ax):
    ax.set_yticklabels([])
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_xticks([0, np.pi/2, np.pi, np.pi * 3/2])
    ax.set_xticklabels([12, 3, 6, 9])
    return ax


def plot_clocks(cmap='day/night', subplot_spec=None, fig=None, N=256):

    if fig is None:
        fig = plt.gcf()

    gs = use_subplot_spec(1, 2, subplot_spec=subplot_spec, fig=fig,
                          gs_out=True)

    data = np.linspace(0, 1, N)[np.newaxis, :]
    theta = np.linspace(0, 2 * np.pi, N)

    axs = []
    ax = fig.add_subplot(gs[0], polar=True)
    ax.pcolormesh(theta, [0, 1], data, cmap=cmap, vmin=0, vmax=2)
    ax = plot_clock(ax)
    ax.set_title('AM')
    axs.append(ax)

    ax = fig.add_subplot(122, polar=True)
    ax.pcolormesh(theta, [0, 1], data + 1, cmap=cmap, vmin=0, vmax=2)
    ax = plot_clock(ax)
    ax.set_title('PM')
    axs.append(ax)

    return fig