import pytest
from io_methods import write_report, read_input_file, parse_blueprints
from models.blueprint import Blueprint
from consts.consts import PATTERN
import tempfile
import os

def test_write_report(tmp_path):
    results = [(1, 3), (2, 6)]
    out_file = tmp_path / "analysis.txt"
    write_report(results, str(out_file))
    text = out_file.read_text().splitlines()
    assert text[0] == "Blueprint 1: 3"
    assert text[1] == "Blueprint 2: 6"
    assert text[2] == ""
    assert text[3] == "Best blueprint is the blueprint 2."

def test_read_input_and_parse(tmp_path):
    lines = [
        "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian. Each diamond robot costs 1 geode, 8 clay and 7 obsidian.\n"
    ]
    tmp_file = tmp_path / "in.txt"
    tmp_file.write_text("".join(lines))
    # Test read_input_file
    contents = read_input_file(str(tmp_file))
    assert isinstance(contents, list) and lines[0] in contents
    # Test parse_blueprints
    bps = parse_blueprints(str(tmp_file))
    assert len(bps) == 1
    assert bps[0].id == 1
    assert bps[0].costs[0] == (4, 0, 0, 0, 0)
    assert bps[0].costs[1] == (2, 0, 0, 0, 0)
    assert bps[0].costs[2] == (3, 14, 0, 0, 0)
    assert bps[0].costs[3] == (2, 0, 7, 0, 0)
    assert bps[0].costs[4] == (0, 8, 7, 1, 0)
