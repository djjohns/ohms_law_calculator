import math


def calculate_amps(
    volts: float = None, watts: float = None, ohms: float = None
) -> float:

    if volts and ohms:
        amps = volts / ohms

    if volts and watts:
        amps = watts / volts

    if ohms and watts:
        amps = math.sqrt(watts / ohms)

    return amps
