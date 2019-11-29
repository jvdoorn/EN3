from math import sqrt


def calculate_natural_frequency(L, R, C):
    """
    Calculates the natural frequency of an LRC circuit.
    :param L: inductance of the coil (H)
    :param R: resistance of the resistor (R)
    :param C: capacity of the capacitor (C)
    :return: the natural frequency (Hz)
    """
    return sqrt((1 / (L * C)) - (R / (2 * L)) ** 2)
