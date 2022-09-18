import scipy as sp


def create_axis(lamp_indicies, lamp_spec_vals, axis_size):
    """
    Linearly fit between values and indicies. Returns an interpolated axis.

    Args:
        lamp_indicies: An array of index positions of lamp peaks IN THE SPECTRAL DATA
        lamp_spec_vals: An array of the known spectral values of lamp peaks.
    Returns: 
        An array containing the calibrated wavelength positions for the CCD
    """
    m, c, r, p, se = sp.stats.linregress(lamp_indicies, lamp_spec_vals)
    wavelength_ax = []
    for i in range(axis_size):
        wavelength_ax.append(m*(i+1) + c)

    return wavelength_ax
