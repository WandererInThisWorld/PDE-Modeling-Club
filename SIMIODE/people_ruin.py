import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# x is prey
# y is predator

alpha = 1#0.6
beta = 0.11#0.4
delta = 0.1#0.2
gamma = 5#0.7


dt = 0.001

def lotvolt(t, x, y):
    global beta
    if t > 150:
        beta = 0.4 + 9.9/(1 + np.exp(-(t-150-10)))
    return alpha*x - beta*x*y, delta*x*y - gamma*y   

def lotvolt2(t, x):
    return lotvolt(t, x[0], x[1])

def ode45(function, time_interval, starting_point):
    x_list = [starting_point[0]]
    y_list = [starting_point[1]]

    # h = dt

    for t in range(int((time_interval[1] - time_interval[0])/dt)):
        x_rec = x_list[-1]
        y_rec = y_list[-1]

        #k1 = function(x_rec, y_rec)
        #k2 = function(x_rec + h*k1[0]/2, y_rec + h*k1[1]/2)
        #k3 = function(x_rec + h*k2[0]/2, y_rec + h*k2[1]/2)
        #k4 = function(x_rec + h*k3[0], y_rec + h*k3[1])
        #x_list.append(x_rec + h*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]))
        #y_list.append(x_rec + h*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]))

        x_list.append(x_rec + function(t + time_interval[0], x_rec, y_rec)[0] * dt)
        y_list.append(y_rec + function(t + time_interval[0], x_rec, y_rec)[1] * dt)
    
    return x_list[:-1], y_list[:-1]

def main():
    start_time = 100
    end_time = 300
    #time_interval = [t/dt for t in range(int((end_time - start_time)/dt))]
    #x, y = ode45(lotvolt, (start_time, end_time), (15, 8))
    results = solve_ivp(lotvolt2, (start_time, end_time), np.array([50, 10]))
    t = results.t
    y = results.y
    #plt.plot(time_interval, x)
    #plt.plot(time_interval, y)
    plt.plot(t, y[0])
    plt.plot(t, y[1])
    #plt.plot(y[0], y[1])
    plt.show()


main()

