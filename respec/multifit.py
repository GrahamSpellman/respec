import sys
import numpy as np
import scipy as sp
from lmfit import models


def peak_detect_rough(v, delta, x):
    """
    Transcribed from Eli Billauer because nobody writes readable code.
    https://gist.github.com/250860.git

    Returns two items: mximas and mnimas. Each is an array of touples containing the 
    location and values of mximas in the data vector v. If x is passed, the touples will
    be (x value, v value), if not, the x values are replaced with indicies. 

    Args:
        v: Input array
        delta: Value for value tolerance
        x: optional argument for position data associated with v.
    Returns:
        maximas: Array of touples containing value of maximas and their index positions. Indicies replaced with x-positions if passsed.
        minimas: Array of touples containing value of minimas and their index positions. Indicies replaced with x-positions if passsed.
    """
    mximas = []
    mnimas = []

    # exit cases
    if x is None:
        x = np.arange(len(v))

    v = np.asarray(v)

    if len(v) != len(x):
        sys.exit('Inputs must be of the same length')

    if not np.isscalar(delta):
        sys.exit('Delta must be a scalar')

    if delta <= 0:
        sys.exit('Delta must be positive')

    #declaring temporary values for peak detection
    mn, mx = np.Inf, -np.Inf
    mnpos, mxpos = np.NaN, np.NaN
    lookformx = True

    for i in np.arange(len(v)):
        v_val = v[i]
        if v_val > mx:
            mx = v_val
            mxpos = x[i]
        if v_val < mn:
            mn = v_val
            mnpos = x[i]
        
        if lookformx:
            if v_val < mx-delta:
                mximas.append((mxpos, mx))
                mn = v_val
                mnpos = x[i]
                lookformx = False
        else:
            if v_val > mn + delta:
                mnimas.append((mnpos, mn))
                mx = v_val
                mxpos = x[i]
                lookformx = True   

    return mximas, mnimas

def add_6035_lorenzian(prefix, center):
    """
    NOT IMPLIMENTED
    Wrapper around add_lorenzian with sensible defaults for the calibration lamp
    """
    return


def add_lorenzian(prefix, center, amplitude, sigma):
    """
    Adds an unevaluated lorenzian to an lmfit model.

    Adapted from: https://stackoverflow.com/questions/57278821/how-does-one-fit-multiple-independent-and-overlapping-lorentzian-peaks-in-a-set


    Args:
        prefix: naming prefix for lmfit parameters.
        center: initial positon of centerpoint parameter %\mu%
        amplitude: initial position of amplitude %A%
        sigma: initial position of sigma parameter %\sigma%
    Returns:
        peak: a reference to the generated lmfit lorenzian model
        params: array of Parameter objects for the model
    """
    peak = models.LorentzianModel(prefix=prefix)
    parameters = peak.make_params()
    parameters[prefix + 'center'].set(center)
    parameters[prefix + 'amplitude'].set(amplitude)
    parameters[prefix + 'sigma'].set(sigma, min=0)
    
    return peak, parameters


def make_multi_lorenz():
    return


