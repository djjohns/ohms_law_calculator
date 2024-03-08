def calculate_watts(volts=None, amps=None, ohms=None):

    if volts and ohms:
        watts = (volts**2) / ohms

    if amps and ohms:
        watts = (amps**2) * ohms

    if volts and amps:
        watts = volts * amps

    return watts
