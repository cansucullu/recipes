"""
Draws Venn Diagrams with 2 sets and an intersection
"""

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

FONT_SIZE = 18
ALPHA = 0.7
COLOR1 = (0, 0, 1)
COLOR2 = (1, 0, 0)

def blend_colors(color1, color2, alpha=0.5):
    """
    Blends 2 colors by estimating the weighted averages for each RGB
    channel

    Parameters
    ----------
    color1 : tuple of float
        Color 1 in (R, G, B) where elements are between 0 and 1.
    color2 : tuple of float
        Color 2 in (R, G, B) where elements are between 0 and 1.
    alpha : float
        Relative weight of the first color, between 0 and 1. Default is
        0.5, i.e. equal weight.

    Returns
    -------
    tuple of int
        Blended color in (R, G, B).
    """
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r_blend = r1 * (1 - alpha) + r2 * alpha
    g_blend = g1 * (1 - alpha) + g2 * alpha
    b_blend = b1 * (1 - alpha) + b2 * alpha
    return (r_blend, g_blend, b_blend)


def draw_venn_single(area1, area2, savefig=False,
                     name="venn_single_example"):
    """
    Draw vectors.

    Parameters
    ----------
    area1 : int
        Releative area of the first set (set on the left)
    area2 : int
        Releative area of the second set (set on the right)
    savefig : bool
        Boolean flag to save the fig, default is False
    name : str
        Name of the file when saved. Redundant if savefig=False.
        Default is venn_single_example.

    Returns
    -------
    None
    """
    v = venn2(subsets=(area1, area2, 0.5), set_labels=('', '', ''))

    v.get_patch_by_id('10').set_alpha(ALPHA)
    v.get_patch_by_id('10').set_color(COLOR1)
    v.get_label_by_id('10').set_color('white')
    v.get_label_by_id('10').set_text('Product')
    v.get_label_by_id('10').set_fontsize(FONT_SIZE)
    v.get_label_by_id('10').set_fontweight('bold')

    v.get_patch_by_id('01').set_alpha(ALPHA)
    v.get_patch_by_id('01').set_color(COLOR2)
    v.get_label_by_id('01').set_text('Marketing')
    v.get_label_by_id('01').set_color('white')
    v.get_label_by_id('01').set_fontsize(FONT_SIZE)
    v.get_label_by_id('01').set_fontweight('bold')

    v.get_patch_by_id('11').set_color(blend_colors(COLOR1, COLOR2))
    v.get_label_by_id('11').set_text('?')
    v.get_label_by_id('11').set_fontsize(FONT_SIZE)

    c1 = v.centers[0].asarray()[0]
    c2 = v.centers[1].asarray()[0]
    r1 = v.radii[0] / 2
    r2 = v.radii[1] / 2
    m = 0 if area1 == area2 else (-1 if area1 > area2 else 1)
    adjust = (c2-c1) * 0.02
    cp = c1 + r1 + (c2-c1-r1-r2) / 2 - adjust * m

    if savefig:
        plt.savefig(f"{name}.png", dpi=300)
    plt.show()


if __name__ == '__main__':
    draw_venn_single(area1=3, area2=3, savefig=True)
