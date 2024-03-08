import math


def calculate_volts(amps=None, ohms=None, watts=None):

    if amps and ohms:
        voltage = amps * ohms

    if amps and watts:
        voltage = watts / ohms

    if watts and ohms:
        voltage = math.sqrt(watts * ohms)

    return voltage
