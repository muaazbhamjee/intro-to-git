"""Starter tests — expand these as an exercise."""

import pytest
from src.utils import reynolds_number


def test_reynolds_number_basic():
    """Test Reynolds number with known values."""
    Re = reynolds_number(rho=1.225, u=10.0, L=0.1, mu=1.8e-5)
    assert Re == pytest.approx(68056, rel=1e-2)


def test_reynolds_number_zero_viscosity():
    """Viscosity must be positive."""
    with pytest.raises(ValueError):
        reynolds_number(rho=1.0, u=1.0, L=1.0, mu=0.0)


# TODO: Add tests for strouhal_number and drag_coefficient.
# TODO: Add tests for mesh.uniform_grid (hint: find the bug!).
# TODO: Add tests for mesh.stretched_grid.
