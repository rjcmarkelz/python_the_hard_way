import numpy as np
from scipy import integrate
from matplotlib.pylab import *
import matplotlib.pyplot as plt

#diffusion example
def tank(t, y):
    F = 20.1
    CA_in = 2.5
    V = 100
    k = 0.15
    CA = y[0]
    #output must be column vector
    n = len(y)
    dydt = np.zeros((n,1))
    dydt[0] = F/V*(CA_in - CA) - k*CA**2
    return dydt


if __name__ == '__main__':

    r = integrate.ode(tank).set_integrator('vode', method = 'bdf')

    t_start = 0.0
    t_end = 10.0
    delta_t = 0.1

    num_steps = np.floor((t_end - t_start)/delta_t) + 1
    CA_t_zero = 0.5
    r.set_initial_value([CA_t_zero], t_start)

    t = np.zeros((num_steps, 1))
    CA = np.zeros((num_steps, 1))

    t[0] = t_start
    CA[0] = CA_t_zero

    k = 1

    while r.successful() and k < num_steps:
        r.integrate(r.t + delta_t)

        t[k] = r.t
        CA[k] = r.y[0]
        k += 1

    plot(t, CA)
    grid('on')
    xlabel('Time [minutes]')
    ylabel('Concentration [mol/L]')
    plt.show()


