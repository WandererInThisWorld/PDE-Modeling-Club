import numpy as np
import matplotlib.pyplot as plt


# this the ideal scenario, without drag
g = 9.81
tf = 10
dt = 0.01
x0 = 0
y0 = 0
z0 = 10
v0 = 50
phi = np.pi/3 # 45 degrees
theta = np.pi/6
t = np.array([i*dt for i in range(int(tf/dt))])
x = x0+v0*np.cos(phi)*np.cos(theta)*t
y = y0+v0*np.cos(phi)*np.sin(theta)*t
z = z0+v0*np.sin(phi)*t-0.5*g*(t**2)

idx = 0
neg_idx = []
while idx < len(z):
    if z[idx] < 0:
        neg_idx.append(idx)
    idx = idx + 1


new_z = np.delete(z, neg_idx)
new_y = np.delete(y, neg_idx)
new_x = np.delete(x, neg_idx)
new_t = np.delete(t, neg_idx)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

for i in range(len(new_x)):
    ax.plot(new_x, new_y, new_z)
    ax.plot(new_x[i], new_y[i], new_z[i], 'o')
    ax.plot([0, new_x[i]], [0, new_y[i]], [0, new_z[i]])
    plt.draw()
    plt.pause(0.05)
    ax.cla()

np.random.seed(1)
# now add drag into the mixture
t = np.array([i*dt for i in range(int(tf/dt))])
x = [x0]
y = [y0]
z = [z0]
vel = v0
vx0 = vel*np.cos(phi)*np.cos(theta)
vy0 = vel*np.cos(phi)*np.sin(theta)
vz0 = vel*np.sin(phi)
k = 1
for ti in t[1:]:
    vx = vx0*np.exp(-k*ti)
    vy = vy0*np.exp(-k*ti)
    vz = (vz0 + g/k)*np.exp(-k*ti) - g/k
    
    x.append(x[-1] + vx*dt)
    y.append(y[-1] + vy*dt)
    z.append(z[-1] + vz*dt)
    
    
x = np.array(x)
y = np.array(y)
z = np.array(z)

idx = 0
neg_idx = []
while idx < len(z):
    if z[idx] < 0:
        neg_idx.append(idx)
    idx = idx + 1


new_z = np.delete(z, neg_idx)
new_y = np.delete(y, neg_idx)
new_x = np.delete(x, neg_idx)
new_t = np.delete(t, neg_idx)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

for i in range(len(new_x)):
    ax.plot(new_x, new_y, new_z)
    ax.plot(new_x[i], new_y[i], new_z[i], 'o')
    ax.plot([0, new_x[i]], [0, new_y[i]], [0, new_z[i]])
    plt.draw()
    plt.pause(0.01)
    ax.cla()

