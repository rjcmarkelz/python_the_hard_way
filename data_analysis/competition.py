# outline of competition model
from scipy.integrate import odeint
import numpy as np
from matplotlib.pylab import *
import matplotlib.pyplot as plt

def competition(t, state, parameters):
	# array
	

	#constants 
	k = 0.11
	m = 0.01
	g = 0.1
	n = 1
	C = 0.99
	q = 2

	#state derivatives
	dw1 = (w1^q/(w1^q + C*w2^q))*(k*(w1+w2)/(1 + g*(w1+w2)^n)) - m*w1
	dw2 = (C*(w2^q/(w1^q + C*w2^q)))*(k*(w1+w2)/(1 + g*(w1+w2)^n)) - m*w2

	return [dw1, dw2]

state0 = [0.20, 0.20] #initial state
t = np.arange(.0, 10.0, 0.1) # timestep


state = odeint(competition, state0, t)

plot(t, state)
xlabel('TIME (sec)')
ylabel('STATES')
title('2 Plant System')
legend((''))
show()