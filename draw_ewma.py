#!/usr/bin/env python

import matplotlib.pyplot as libplot

alpha = 0.9

def ewma(xprev, sprev, dt, alpha, t):
    xnext = alpha * dt + (1 - alpha) * xprev
    snext = (t * sprev) / (t + 1) + (dt - xnext) / t
    return [xnext, snext]

indata = 
