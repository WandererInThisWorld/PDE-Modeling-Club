import numpy as np
import matplotlib.pyplot as plt


# this the ideal scenario, without drag
g = 9.81
tf = 100
dt = 0.01

# initial position of the food projectile
x0 = 0
y0 = 0
z0 = 10

# initial velocity of the food projectile and angle thrown
vf0 = 10
phi = np.pi/3 # 45 degrees
theta = np.pi/4

# initial position of the dog 
a0 = 10
b0 = 10
c0 = 0

# start time
t = 0

# position and velocity of the food
xt = vf0*np.cos(phi)*np.cos(theta) * t + x0
yt = vf0*np.cos(phi)*np.sin(theta) * t + y0
zt = vf0*np.sin(phi) * t -g * (t**2)/2 + z0
vxt = vf0*np.cos(phi)*np.cos(theta)
vyt = vf0*np.cos(phi)*np.sin(theta)
vzt = vf0*np.sin(phi) - g*t

# position and velocity of the dog
ar = a0
br = b0
cr = c0

at = a0
bt = b0
ct = c0

vd = 1
tstar = vzt/g + np.sqrt(vzt**2 + 2*g*zt)/g + t
xtstar = vxt*(tstar - t) + xt
ytstar = vyt*(tstar - t) + yt
vat = np.sign(xtstar - at)*vd*np.sqrt(((xtstar - at)**2)/((xtstar - at)**2 + (ytstar - bt)**2))
vbt = np.sign(ytstar - bt)*vd*np.sqrt(((ytstar - bt)**2)/((xtstar - at)**2 + (ytstar - bt)**2))

# record of position of food projectile and dog
foodx = []
foody = []
foodz = []
dogx = []
dogy = []
dogz = []

while zt >= 0:
    # position and velocity of the food
    xt = vf0*np.cos(phi)*np.cos(theta) * t + x0
    yt = vf0*np.cos(phi)*np.sin(theta) * t + y0
    zt = vf0*np.sin(phi) * t -g * (t**2)/2 + z0
    vxt = vf0*np.cos(phi)*np.cos(theta)
    vyt = vf0*np.cos(phi)*np.sin(theta)
    vzt = vf0*np.sin(phi) - g*t

    # every 0.5 seconds, the dog goes another direction
    if ((t*50) - int(t*50)) <= dt/2:
        # new velocity of the dog
        tstar = vzt/g + np.sqrt(vzt**2 + 2*g*zt)/g + t
        xtstar = vxt*(tstar - t) + xt
        ytstar = vyt*(tstar - t) + yt
        vat = vd*(xtstar - at)/np.sqrt((xtstar - at)**2 + (ytstar - bt)**2)
        vbt = vd*(ytstar - bt)/np.sqrt((xtstar - at)**2 + (ytstar - bt)**2)

        ar = at
        br = bt
        cr = ct

        if ((at - xtstar)**2 + (bt - ytstar)**2) < 1:
            #print("close")
            vat = vat*((at - xtstar)**2 + (bt - ytstar)**2)
            vbt = vbt*((at - xtstar)**2 + (bt - ytstar)**2)
            ...

        print(xtstar, '\t', ytstar, '\t', tstar)
    
    # compute the position of the dog
    at = ar + vat*(t - np.floor(2*t)/2)
    bt = br + vbt*(t - np.floor(2*t)/2)

    t = t + dt

    # store the positions of the food and dog
    foodx.append(xt)
    foody.append(yt)
    foodz.append(zt)
    dogx.append(at)
    dogy.append(bt)
    dogz.append(ct)

print(foodx[-1], '\t', foody[-1], '\t', t)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

for i in range(len(foodx)):
    ax.plot(foodx[0:i], foody[0:i], foodz[0:i])
    ax.plot(foodx[i], foody[i], foodz[i], 'o')
    ax.plot([0, foodx[i]], [0, foody[i]], [0, foodz[i]])
    
    ax.plot(dogx[0:i], dogy[0:i], dogz[0:i])
    ax.plot(dogx[i], dogy[i], dogz[i], 'o')
    
    plt.draw()
    plt.pause(0.05)
    ax.cla()

np.random.seed(1)






# now add drag into the mixture

# initial position (and mass) of the food projectile
x0 = 0
y0 = 0
z0 = 10

m = 5
c = 10

# initial velocity of the food projectile and angle thrown
vf0 = 20
phi = np.pi/3 # 45 degrees
theta = np.pi/4

# initial position of the dog 
a0 = 25
b0 = 10
c0 = 0

# start time
t = 0

# position and velocity of the food
xt = (m/c)*vf0*np.cos(phi)*np.cos(theta)*(1-np.exp(-c*t/m)) + x0
yt = (m/c)*vf0*np.cos(phi)*np.sin(theta)*(1-np.exp(-c*t/m)) + y0
zt = (m/c)*(vf0*np.sin(phi) + m*g/c)*(1-np.exp(-c*t/m)) - m*g*t/c + z0
vxt = vf0*np.cos(phi)*np.cos(theta) * np.exp(-c*t/m)
vyt = vf0*np.cos(phi)*np.sin(theta) * np.exp(-c*t/m)
vzt = (vf0*np.sin(phi) + m*g/c) * np.exp(-c*t/m) - m*g/c

# position and velocity of the dog
ar = a0
br = b0
cr = c0

at = a0
bt = b0
ct = c0

vd = 1
tstar = vzt/g + np.sqrt(vzt**2 + 2*g*zt)/g + t
xtstar = vxt*(tstar - t) + xt
ytstar = vyt*(tstar - t) + yt
vat = np.sign(xtstar - at)*vd*np.sqrt(((xtstar - at)**2)/((xtstar - at)**2 + (ytstar - bt)**2))
vbt = np.sign(ytstar - bt)*vd*np.sqrt(((ytstar - bt)**2)/((xtstar - at)**2 + (ytstar - bt)**2))

# record of position of food projectile and dog
foodx = []
foody = []
foodz = []
dogx = []
dogy = []
dogz = []

while zt >= 0:
    # position and velocity of the food
    xt = (m/c)*vf0*np.cos(phi)*np.cos(theta)*(1-np.exp(-c*t/m)) + x0
    yt = (m/c)*vf0*np.cos(phi)*np.sin(theta)*(1-np.exp(-c*t/m)) + y0
    zt = (m/c)*(vf0*np.sin(phi) + m*g/c)*(1-np.exp(-c*t/m)) - m*g*t/c + z0
    vxt = vf0*np.cos(phi)*np.cos(theta) * np.exp(-c*t/m)
    vyt = vf0*np.cos(phi)*np.sin(theta) * np.exp(-c*t/m)
    vzt = (vf0*np.sin(phi) + m*g/c) * np.exp(-c*t/m) - m*g/c

    
    # every 0.5 seconds, the dog goes another direction
    if ((t*50) - int(t*50)) <= dt/2:
        # new velocity of the dog
        tstar = vzt/g + np.sqrt(vzt**2 + 2*g*zt)/g + t
        xtstar = vxt*(tstar - t) + xt
        ytstar = vyt*(tstar - t) + yt
        vat = vd*(xtstar - at)/np.sqrt((xtstar - at)**2 + (ytstar - bt)**2)
        vbt = vd*(ytstar - bt)/np.sqrt((xtstar - at)**2 + (ytstar - bt)**2)

        ar = at
        br = bt
        cr = ct

        if ((at - xtstar)**2 + (bt - ytstar)**2) < 1:
            #print("close")
            vat = vat*((at - xtstar)**2 + (bt - ytstar)**2)
            vbt = vbt*((at - xtstar)**2 + (bt - ytstar)**2)
            ...

        print(xtstar, '\t', ytstar, '\t', tstar)
    
    # compute the position of the dog
    at = ar + vat*(t - np.floor(2*t)/2)
    bt = br + vbt*(t - np.floor(2*t)/2)

    t = t + dt

    # store the positions of the food and dog
    foodx.append(xt)
    foody.append(yt)
    foodz.append(zt)
    dogx.append(at)
    dogy.append(bt)
    dogz.append(ct)

print(foodx[-1], '\t', foody[-1], '\t', t)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

for i in range(len(foodx)):
    ax.plot(foodx[0:i], foody[0:i], foodz[0:i])
    ax.plot(foodx[i], foody[i], foodz[i], 'o')
    ax.plot([0, foodx[i]], [0, foody[i]], [0, foodz[i]])
    
    ax.plot(dogx[0:i], dogy[0:i], dogz[0:i])
    ax.plot(dogx[i], dogy[i], dogz[i], 'o')
    
    plt.draw()
    plt.pause(0.05)
    ax.cla()




