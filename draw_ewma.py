#!/usr/bin/env python

import matplotlib.pyplot as libplot
import random

random.seed()

alpha = 0.9

def ewma(xprev, sprev, dt, alpha, t):
    xnext = alpha * dt + (1 - alpha) * xprev
    #snext = (t * sprev) / (t + 1) + (dt - xnext) ** 2 / (t + 1)
    #snext = sprev + xnext ** 2 - xprev ** 2 + (xnext ** 2 - sprev - xprev ** 2) / (t + 1)
    C = 2 * alpha ** 2 / (1 + alpha)
    snext = alpha * sprev + (1 - alpha) * (dt - xnext) / C
    
    
    return [xnext, snext]

t = [i+1 for i in range(150)]
#indata = [random.gauss(0, 0.001) for i in range(len(t))]
indata = [random.gauss(0, 2) for i in range(len(t))]
mu = [indata[0]]
sigma = [indata[0] ** 2]

for i in range(len(t)):
  [x, s] = ewma(mu[-1], sigma[-1], indata[i], 0.4, i+1)
  mu.append(x)
  sigma.append(s)

sigma_est = [alpha / (2 - alpha) * (w) for w in sigma]

libplot.figure()
libplot.plot(t, indata, ":")
libplot.plot(t, mu[1:])
#libplot.plot(t, sigma_est[1:])
libplot.legend(["Input", "Mu"])#, "Sigma"])

libplot.show()
