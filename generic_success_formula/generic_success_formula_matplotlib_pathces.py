"""
The code for creating an image of 3 circles with symbols in between.
The current version is a top-level code and does not use any functions.
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

fig = plt.figure(1, figsize=(6.4 * 1.6, 4.8), facecolor='gray')
print(fig.get_size_inches())
ax = fig.add_subplot(111)
fig.subplots_adjust(left=0.01, bottom=0.01, right=1-0.01, top=1-0.01)


#  Clean axes' spines and xy lines
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(
    axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False
)

#  Calculations for drawing real circles
#  Credits: https://stackoverflow.com/questions/9230389/why-is-matplotlib-plotting-my-circles-as-ovals
x0, y0 = ax.transAxes.transform((0, 0))  # lower left in pixels
x1, y1 = ax.transAxes.transform((1, 1))  # upper right in pixes
dx = x1 - x0
dy = y1 - y0
maxd = max(dx, dy)
width = maxd / dx
height = maxd / dy

# Location and size settings for circles
X1 = 0.2  # X is for x axis location of center
X2 = 0.5
X3 = 0.8
S1 = 0.2  # S is for scale
S2 = 0.2
S3 = 0.2
C1 = "#4daf4a"
C2 = "#e41a1c"
C3 = "#377eb8"

ax.text(X1, 0.5, "Good\nProduct", fontsize=18, color=C1, ha="center", va="center", style="normal", weight=600)
ax.add_artist(Ellipse((X1, 0.5), width * S1, height * S1, edgecolor=C1+"FF", facecolor="white"))

ax.text(np.mean([X2, X1]), 0.5, "$\\times$", size=18 * 1.66, rotation=0., color="#22313F", ha="center", va="center", )

ax.text(X2, 0.5, "Good\nMarketing", size=18, color=C2, ha="center", va="center", style="normal", weight=600)
ax.add_artist(Ellipse((X2, 0.5), width * S2, height * S2, edgecolor=C2+"FF", facecolor="white"))

ax.text(np.mean([X3, X2]), 0.5, "$=$", size=18 * 1.66, rotation=0., color="#22313F", ha="center", va="center", )

ax.text(X3, 0.5, "Success", size=18, color=C3, ha="center", va="center", style="normal", weight=600)
ax.add_artist(Ellipse((X3, 0.5), width * S3, height * S3, edgecolor=C3+"FF", facecolor="white"))

fig.savefig("generic-success-formula-rgb.png", dpi=300)
plt.draw()
plt.show()
