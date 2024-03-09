def calculate_ohms(
    watts: float = None, volts: float = None, amps: float = None
) -> float:

    if volts and amps:
        resistance = volts / amps

    if volts and watts:
        resistance = (volts**2) / amps

    if amps and watts:
        resistance = watts / (amps**2)

    return resistance
