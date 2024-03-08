def calculate_ohms(watts=None, volts=None, amps=None):

    if volts and amps:
        resistance = volts / amps

    if volts and watts:
        resistance = (volts**2) / amps

    if amps and watts:
        resistance = watts / (amps**2)

    return resistance
