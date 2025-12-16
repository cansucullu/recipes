"""
Python code snippet to draw vectors using Matplotblib
"""
import numpy as np
import matplotlib.pyplot as plt

LIMIT = 7
COLOR1 = "#57606f"  # Axis lines color
COLOR2 = "#ececec"  # Grid lines color

def draw_vector(vectors, texts=None, savefig=False,
                name="vectors-example"):
    """
    Draw vectors.

    Parameters
    ----------
    vectors : list of list of int
        A list of vectors in the following format
        [vector_1, vector_2, ...], where vector_i is
        [x_start, y_start, x_end, y_end]
    texts : list of str
        A list of strings which are used as endpoint labels in the x-y
        axes. The order is top, bottom, left, right. Default is
        ["North", "South", "West", "East"]
    savefig : bool
        Boolean flag to save the fig, default is False
    name : str
        Name of the file when saved. Redundant if savefig=False.

    Returns
    -------
    None
    """
    texts = texts or []
    if len(texts) == 0:
        texts = ["North", "South", "West", "East"]

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    #  Shift spines (coordinate lines) to center and do styling
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_color(COLOR1)
    ax.spines["bottom"].set_color(COLOR1)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    arrowprops = {
        "arrowstyle":"<|-|>",
        "color":COLOR1,
        "shrinkA":0,
        "shrinkB":0
    }

    for a, b in [(LIMIT, 0), (0, LIMIT)]:
        ax.annotate("", xy=(-a, -b), xycoords="data", xytext=(a, b),
                    textcoords="data", arrowprops=arrowprops)

    ax.set_xlim(-LIMIT, LIMIT)
    ax.set_ylim(-LIMIT, LIMIT)

    #  Set line ticks except the center point
    ticks = np.linspace(-LIMIT+1, LIMIT-1, 2*LIMIT-1)
    ticklabels = [" " if i in [0] else "{:g}".format(i) for i in ticks]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(ticklabels, rotation=0, color=COLOR1)
    ax.set_yticklabels(ticklabels, rotation=0, color=COLOR1)
    ax.tick_params(axis='both', colors=COLOR1)

    #  Set grid lines
    ax.set_axisbelow(True)
    ax.grid(color=COLOR2, linestyle="dashed")

    #  Name coordinate system ends
    ax.text(0, LIMIT+1, texts[0], ha="center", va="center",
            color="#8e44ad", weight="bold")
    ax.text(0, -(LIMIT+1), texts[1], ha="center", va="center",
            color="#e74c3c")
    ax.text(LIMIT+1, 0, texts[2], ha="center", va="center",
            color="#f1c40f")
    ax.text(-(LIMIT+1), 0, texts[3], ha="center", va="center",
            color="#f1c40f")

    #  Draw vectors using matplotlib's quiver objects
    vectors = np.array(vectors)
    x_start, y_start, x_end, y_end = zip(*vectors)
    ax.quiver(x_start, y_start, x_end, y_end, angles="xy",
              scale_units="xy", scale=1, width=0.01,
              color=["#1e3799", "#e55039", "#218c74"], zorder=10)

    if savefig:
        plt.savefig("{}.png".format(name), dpi=300)

    plt.draw()
    plt.show()
    plt.gcf().clear()


if __name__ == '__main__':
    input_vectors = [
        [0, 0, 3, 4],
        [2, -3, 3, -1],
        [-2, 1, -1, 4],
    ]
    draw_vector(vectors=input_vectors, savefig=True)
