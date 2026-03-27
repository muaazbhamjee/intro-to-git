"""Mesh generation utilities.

Simple structured mesh helpers for 2D domains.
NOTE: There is a deliberate bug in this file — can you find it?
"""

import math


def uniform_grid(x_min: float, x_max: float, n_cells: int) -> list[float]:
    """Generate a uniform 1D grid.

    Parameters
    ----------
    x_min : float
        Left boundary coordinate.
    x_max : float
        Right boundary coordinate.
    n_cells : int
        Number of cells.

    Returns
    -------
    list[float]
        Cell centre coordinates.
    """
    if n_cells <= 0:
        raise ValueError("Number of cells must be positive.")

    dx = (x_max - x_min) / n_cells
    # BUG: should start at x_min + 0.5 * dx, not x_min
    return [x_min + i * dx for i in range(n_cells)]


def stretched_grid(
    x_min: float, x_max: float, n_cells: int, ratio: float = 1.1
) -> list[float]:
    """Generate a geometrically stretched 1D grid.

    Useful for boundary layers where cells near x_min should be smaller.

    Parameters
    ----------
    x_min : float
        Left boundary coordinate.
    x_max : float
        Right boundary coordinate.
    n_cells : int
        Number of cells.
    ratio : float
        Growth ratio between successive cells (default 1.1).

    Returns
    -------
    list[float]
        Cell-edge coordinates (n_cells + 1 values).
    """
    if n_cells <= 0:
        raise ValueError("Number of cells must be positive.")
    if ratio <= 0:
        raise ValueError("Growth ratio must be positive.")

    # First cell size from geometric series sum
    total_length = x_max - x_min
    if abs(ratio - 1.0) < 1e-12:
        dx0 = total_length / n_cells
    else:
        dx0 = total_length * (1 - ratio) / (1 - ratio ** n_cells)

    edges = [x_min]
    dx = dx0
    for _ in range(n_cells):
        edges.append(edges[-1] + dx)
        dx *= ratio

    return edges


def y_plus(u_tau: float, y: float, nu: float) -> float:
    """Calculate y+ (dimensionless wall distance).

    Parameters
    ----------
    u_tau : float
        Friction velocity (m/s).
    y : float
        Distance from wall (m).
    nu : float
        Kinematic viscosity (m^2/s).

    Returns
    -------
    float
        y+ value.
    """
    if nu <= 0:
        raise ValueError("Kinematic viscosity must be positive.")
    return u_tau * y / nu


if __name__ == "__main__":
    # Test uniform grid
    centres = uniform_grid(0.0, 1.0, 5)
    print(f"Uniform cell centres: {centres}")
    print(f"  Expected first centre near 0.1, got {centres[0]}")

    # Test stretched grid
    edges = stretched_grid(0.0, 1.0, 10, ratio=1.2)
    print(f"\nStretched grid edges ({len(edges)} points):")
    for i, x in enumerate(edges):
        print(f"  Edge {i}: x = {x:.4f}")
