import math


def calculate_volts(
    amps: float = None, ohms: float = None, watts: float = None
) -> float:
    if amps and ohms:
        if not all(isinstance(arg, (int, float)) for arg in (amps, ohms)):
            raise TypeError("All arguments must be numbers")
        volts = amps * ohms

    if amps and watts:
        if not all(isinstance(arg, (int, float)) for arg in (amps, watts)):
            raise TypeError("All arguments must be numbers")
        volts = watts / amps

    if watts and ohms:
        if not all(isinstance(arg, (int, float)) for arg in (watts, ohms)):
            raise TypeError("All arguments must be numbers")
        volts = math.sqrt(watts * ohms)

    return volts
