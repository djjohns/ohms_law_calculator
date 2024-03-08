import math


def calculate_amps(volts=None, watts=None, ohms=None):

    if volts and ohms:
        amps = volts / ohms

    if volts and watts:
        amps = watts / volts

    if ohms and watts:
        amps = math.sqrt(watts / ohms)

    return amps
