import re
from consts.consts import PATTERN


class Blueprint:
    def __init__(self, id: int, costs: list[tuple[int, int, int, int, int]]):
        self.id = id
        self.costs = costs

    @staticmethod
    def from_string(line: str):
        pattern = re.compile(PATTERN)

        match = pattern.fullmatch(line)
        if not match:
            raise ValueError(f"Line {line}: invalid format")

        nums = list(map(int, match.groups()))

        (
            bp_id,
            ore_robot_ore_cost,
            clay_robot_ore_cost,
            obsidian_robot_ore_cost, obsidian_robot_clay_cost,
            geode_robot_ore_cost, geode_robot_obsidian_cost,
            diamond_robot_geode_cost, diamond_robot_clay_cost, diamond_robot_obsidian_cost,
        ) = nums # Assign matched costs

        costs = [
            (ore_robot_ore_cost, 0, 0, 0, 0),
            (clay_robot_ore_cost, 0, 0, 0, 0),
            (obsidian_robot_ore_cost, obsidian_robot_clay_cost, 0, 0, 0),
            (geode_robot_ore_cost, 0, geode_robot_obsidian_cost, 0, 0),
            (0, diamond_robot_clay_cost, diamond_robot_obsidian_cost, diamond_robot_geode_cost, 0),
        ]

        return Blueprint(bp_id, costs)
