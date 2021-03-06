from matplotlib_venn import venn2
import matplotlib.pyplot as plt


FONT_SIZE = 18
ALPHA = 0.7


def draw_venn_single(area1, area2, savefig=False, name="venn_single_example"):
    v = venn2(subsets=(area1, area2, 0.5), set_labels=('', '', ''))

    v.get_patch_by_id('10').set_alpha(ALPHA)
    v.get_patch_by_id('10').set_color('green')
    v.get_label_by_id('10').set_color('white')
    v.get_label_by_id('10').set_text('Product')
    v.get_label_by_id('10').set_fontsize(FONT_SIZE)
    v.get_label_by_id('10').set_fontweight('bold')

    v.get_patch_by_id('01').set_alpha(ALPHA)
    v.get_patch_by_id('01').set_color('red')
    v.get_label_by_id('01').set_text('Marketing')
    v.get_label_by_id('01').set_color('white')
    v.get_label_by_id('01').set_fontsize(FONT_SIZE)
    v.get_label_by_id('01').set_fontweight('bold')

    v.get_label_by_id('11').set_text('?')
    v.get_label_by_id('11').set_fontsize(FONT_SIZE)

    c1 = v.centers[0][0]
    c2 = v.centers[1][0]
    r1 = v.radii[0] / 2
    r2 = v.radii[1] / 2
    m = 0 if area1 == area2 else (-1 if area1 > area2 else 1)
    adjust = (c2-c1) * 0.02
    cp = c1 + r1 + (c2-c1-r1-r2) / 2 - adjust * m

    if savefig:
        plt.savefig("{name}.png".format(name=name), dpi=300)
    plt.show()


if __name__ == '__main__':
    draw_venn_single(area1=3, area2=3, savefig=True)
