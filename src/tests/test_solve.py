import pytest
from solve import maximize_diamonds, compute_qualities
from models.blueprint import Blueprint

# Manually constructed Blueprints matching example
bps = [
    Blueprint(
        1,
        [
            (4, 0, 0, 0, 0),
            (2, 0, 0, 0, 0),
            (3, 14, 0, 0, 0),
            (2, 0, 7, 0, 0),
            (0, 8, 7, 1, 0),
        ],
    ),
    Blueprint(
        2,
        [
            (2, 0, 0, 0, 0),
            (3, 0, 0, 0, 0),
            (3, 8, 0, 0, 0),
            (3, 0, 12, 0, 0),
            (0, 2, 3, 3, 0),
        ],
    ),
]


def test_simulate_examples():
    assert maximize_diamonds(bps[0]) == 3
    assert maximize_diamonds(bps[1]) == 3


def test_compute_qualities():
    qualities = dict(compute_qualities(bps))
    assert qualities == {1: 1 * 3, 2: 2 * 3}
