#%%
"""
Does ordinary least squares work with heavy-tailed error distributions?
Under what conditions?
"""
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='dark')
from sklearn import linear_model

# t_param <=1 results in 
t_param = 1.1
L = 100
Nmin = 10
Nmax = 1e5 #100000
# linear coefficients
a = 5
b = 5

e_norm = stats.norm()
e_t = stats.t(df=t_param)

x = np.random.uniform(-10, 10, Nmax)
fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)
fig.suptitle('pdf samples at Nmax density')

axs[0].scatter(x, e_norm.pdf(x), s=3)
axs[1].scatter(x, e_t.pdf(x), s=3)
axs[0].set_xlabel(r'normal $f(x)$')
axs[1].set_xlabel(r't-distr $f(x)$')


print('building linear model, testing for convergence')
nvec = np.linspace(Nmin, Nmax, L).astype(int)
regr = linear_model.LinearRegression()

#parameter fit vectors
Y_gauss_a = []
Y_gauss_b = []
Y_t_a = []
Y_t_b = []

# FIT SLOPE, INTERCEPT USING OLS
for n in nvec:
    x = np.linspace(-5, 5, n)
    Y_gauss = a*x + b + e_norm.rvs(n)
    regr.fit(x.reshape(-1, 1), Y_gauss.reshape(-1, 1))

    Y_gauss_a.append(regr.coef_[0, 0])
    Y_gauss_b.append(regr.intercept_[0])

    Y2 = a*x + b + e_t.rvs(n)
    regr.fit(x.reshape(-1, 1), Y2.reshape(-1, 1))
    Y_t_a.append(regr.coef_[0,0])
    Y_t_b.append(regr.intercept_[0])

# PLOTTING OLS FIT VALUES VS N
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax0.cla(); ax1.cla(); ax2.cla(); ax3.cla()
ax0.scatter(nvec, Y_gauss_a, s=5)
ax1.scatter(nvec, Y_gauss_b, s=5)
ax2.scatter(nvec, Y_t_a, s=5)
ax3.scatter(nvec, Y_t_b, s=5)

# LABELS

fig.suptitle('$y = ax + b$ parameter fits with normal, t-distr noise for N samples')
ax0.set_title('a (norm)')
ax1.set_title('b (norm)')
ax2.set_title('a (t-distr)')
ax3.set_title('b (t-distr)')

ax3.set_xlabel('n samples')
ax0.set_ylabel('parameter estimate')
fig.tight_layout(rect=[0, 0, 1, .94])
