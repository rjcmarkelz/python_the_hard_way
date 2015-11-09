# following tutorial on spring ODE
from scipy.integrate import odeint
import numpy as np
from matplotlib.pylab import *
import matplotlib.pyplot as plt


def MassSpring(state, t):
    x = state[0] 
    xd = state[1]

    #constants
    k = 2.5 
    m = 1.5
    g = 9.8

    #accel
    xdd = ((-k*x)/m) + g

    #return state derivatives
    return [xd, xdd]

state0 = [0.0, 0.0] #intial state
t = np.arange(.0, 10.0, 0.1) # timestep


state = odeint(MassSpring, state0, t)

plot(t, state)
xlabel('TIME (sec)')
ylabel('STATES')
title('Mass-Spring System')
legend(('$x$ (m)', '$\dot{x}$ (m/sec)'))
show()