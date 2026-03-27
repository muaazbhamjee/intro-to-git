"""CFD utility functions.

This module provides helper functions for common CFD calculations.
Use it to practise Git workflows: branch, edit, commit, push, PR.
"""

import math


def reynolds_number(rho: float, u: float, L: float, mu: float) -> float:
    """Calculate the Reynolds number.

    Parameters
    ----------
    rho : float
        Fluid density (kg/m^3).
    u : float
        Characteristic velocity (m/s).
    L : float
        Characteristic length (m).
    mu : float
        Dynamic viscosity (Pa.s).

    Returns
    -------
    float
        Reynolds number (dimensionless).
    """
    if mu <= 0:
        raise ValueError("Dynamic viscosity must be positive.")
    return rho * u * L / mu


def strouhal_number(f: float, D: float, U: float) -> float:
    """Calculate the Strouhal number for vortex shedding.

    Parameters
    ----------
    f : float
        Shedding frequency (Hz).
    D : float
        Cylinder diameter (m).
    U : float
        Free-stream velocity (m/s).

    Returns
    -------
    float
        Strouhal number (dimensionless).
    """
    if U <= 0:
        raise ValueError("Free-stream velocity must be positive.")
    return f * D / U


def drag_coefficient(F_d: float, rho: float, U: float, A: float) -> float:
    """Calculate the drag coefficient.

    Parameters
    ----------
    F_d : float
        Drag force (N).
    rho : float
        Fluid density (kg/m^3).
    U : float
        Free-stream velocity (m/s).
    A : float
        Reference area (m^2).

    Returns
    -------
    float
        Drag coefficient (dimensionless).
    """
    q = 0.5 * rho * U ** 2  # dynamic pressure
    if q * A == 0:
        raise ValueError("Dynamic pressure × area must be non-zero.")
    return F_d / (q * A)


# TODO: Add a function to calculate the Mach number.
#       Ma = U / a, where a = sqrt(gamma * R * T)


if __name__ == "__main__":
    Re = reynolds_number(rho=1.225, u=10.0, L=0.1, mu=1.8e-5)
    print(f"Reynolds number: {Re:.0f}")

    St = strouhal_number(f=50.0, D=0.1, U=10.0)
    print(f"Strouhal number: {St:.3f}")

    Cd = drag_coefficient(F_d=5.0, rho=1.225, U=10.0, A=0.01)
    print(f"Drag coefficient: {Cd:.3f}")
