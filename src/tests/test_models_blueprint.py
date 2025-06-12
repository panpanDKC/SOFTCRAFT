import pytest
from models.blueprint import Blueprint
from consts.consts import PATTERN
from io_methods import parse_blueprints
import tempfile
import os

EXAMPLE_LINE_1 = "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian. Each diamond robot costs 1 geode, 8 clay and 7 obsidian."
EXAMPLE_LINE_2 = "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian. Each diamond robot costs 3 geode, 2 clay and 3 obsidian."

def test_blueprint_from_string_invalid():
    with pytest.raises(ValueError):
        Blueprint.from_string("Invalid blueprint line")

def test_parse_blueprints(tmp_path):
    # Create a temporary file with two lines
    lines = EXAMPLE_LINE_1 + "\n" + EXAMPLE_LINE_2 + "\n"
    tmp_file = tmp_path / "bp.txt"
    tmp_file.write_text(lines)
    bps = parse_blueprints(str(tmp_file))
    assert len(bps) == 2
    assert [bp.id for bp in bps] == [1, 2]
