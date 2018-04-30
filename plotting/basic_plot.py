"""
- create OO subplots in fig
- line, scatter, hist, and loglog
- modify axes, 
- clear axis and restart

OO syntax: https://python4mpia.github.io/plotting/advanced.html

examples: https://matplotlib.org/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py

ref: https://matplotlib.org/gallery/subplots_axes_and_figures/subplot_toolbar.html#
sphx-glr-gallery-subplots-axes-and-figures-subplot-toolbar-py

"""
import numpy as np
import matplotlib.pyplot as plt
#these two lines set the style for matplotlib
import seaborn as sns
sns.set(style="dark")

x = np.linspace(.01, 10, 100)

#plot content:
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
fig.suptitle('plot title here')

ax1.plot(x,x**2)
ax2.scatter(x,x**3, s=10)
ax3.hist(x**4, 40)
ax4.loglog(x, x**5)

# add labels, etc
ax1.set_xlim(1,4)
ax2.set_xlabel('plot 2')
ax3.set_ylabel('some data')
ax4.set_xlabel(r'expr $\gamma_i > \beta_i$')

ax2.cla()
ax2.scatter(x, x**6, s=1)


# fix overlap/crowding:
fig.tight_layout()
# fig.tight_layout(rect=[0, 0.03, 1, 0.95])

