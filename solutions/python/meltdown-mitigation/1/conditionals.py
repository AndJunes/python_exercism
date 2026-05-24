"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):

    ##Verify criticality is balanced.
    
    return (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""

    generated_power = voltage * current
    percentage_power = (
        generated_power / theoretical_max_power
    ) * 100

    if percentage_power >= 80:
        return "green"

    if percentage_power >= 60:
        return "orange"

    if percentage_power >= 30:
        return "red"

    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    #Assess and return status code for the reactor.

    if (temperature * neutrons_produced_per_second) < (threshold * 0.9):
        return "LOW"
    elif (threshold * 0.9) <= (temperature * neutrons_produced_per_second) <= (threshold * 1.1):
        return "NORMAL"
    else:
        return "DANGER"

