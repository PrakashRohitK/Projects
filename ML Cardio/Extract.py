import numpy as np

def crae(diameters):
    return np.sqrt(np.sum([w_a ** 2 for w_a in diameters]) / len(diameters))

def crve(diameters):
    return np.sqrt(np.sum([w_v ** 2 for w_v in diameters]) / len(diameters))

def avr(crae, crve):
    return crae / crve
