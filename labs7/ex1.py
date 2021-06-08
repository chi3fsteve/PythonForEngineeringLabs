import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def ode_FE(f, X_0, dt, T):
    steps = int(round(float(T)/dt))
    x = np.zeros(steps + 1)
    t = np.linspace(0, steps * dt, len(x))
    x[0] = X_0
    for n in range(steps):
        x[n+1] = x[n] + dt*f(x[n])
    return x, t

X = np.linspace(-10, 20, 20)
Y = np.linspace(-10, 20, 20)
X, Y = np.meshgrid(X, Y)
dxdt = (1.3**X)
dt = 1 * np.ones(X.shape)
dx = dxdt * dt
x, t = ode_FE()


f1 = plt.figure(1)
plt.streamplot(X, Y, dt, dx)
f2 = plt.figure(2)
plt.quiver(X, Y, dt, dx, headwidth=2.0, angles='xy', scale=25.)
# plt.show()

# f(X) = start(1+rate)^time
time = 240
start = 10
rate = 105**(1/time)-1
after20days = start*(1+rate)**(20*24)
print("After 20 days there will be {}".format(after20days.__round__()))

f3 = plt.figure(3)
fx = np.linspace(0, 200, 1000)
fy = start*(1+rate)**fx
plt.plot(fx,fy)
plt.yscale('log')
plt.show()