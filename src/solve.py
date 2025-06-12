from functools import lru_cache
from models.blueprint import Blueprint
from consts.consts import (
    ORE,
    CLAY,
    OBSIDIAN,
    GEODE,
    DIAMOND,
    RESOURCE_TYPES,
    TIME_LIMIT,
)


def maximize_diamonds(bp: Blueprint) -> int:
    # Determine maximum useful robots for each resource (except diamonds)
    max_needed = [max(cost[i] for cost in bp.costs) for i in range(RESOURCE_TYPES)]
    max_needed[DIAMOND] = float("inf")
    best_diamonds = 0

    # dfs explores build/wait decisions to maximize diamonds.
    # Memoized on (minutes, robots, stock) to avoid redundant search.
    @lru_cache(None)
    def explore_build_sequences(minutes: int, robots: tuple[int, ...], stock: tuple[int, ...]) -> int:
        nonlocal best_diamonds
        if minutes == 0:
            best_diamonds = max(best_diamonds, stock[DIAMOND])
            return stock[DIAMOND]

        # Upper-bound prune: current diamonds + maximum possible future production
        potential = (
            stock[DIAMOND] + robots[DIAMOND] * minutes + minutes * (minutes - 1) // 2
        )
        if potential <= best_diamonds:
            return 0

        max_found = stock[DIAMOND]
        # Try building each robot type (one branch per choice), prioritizing diamonds
        for kind in (DIAMOND, GEODE, OBSIDIAN, CLAY, ORE):
            cost = bp.costs[kind]
            if (
                all(stock[i] >= cost[i] for i in range(RESOURCE_TYPES))
                and robots[kind] < max_needed[kind]
            ):
                # Deduct cost and add robot
                next_stock = tuple(
                    stock[i] + robots[i] - cost[i] for i in range(RESOURCE_TYPES)
                )
                next_robots = list(robots)
                next_robots[kind] += 1
                result = explore_build_sequences(minutes - 1, tuple(next_robots), next_stock)
                max_found = max(max_found, result)
                if kind == DIAMOND:
                    return max_found

        # Or wait: collect resources without building
        waited_stock = tuple(stock[i] + robots[i] for i in range(RESOURCE_TYPES))
        return max(max_found, explore_build_sequences(minutes - 1, robots, waited_stock))

    # Start with one ore robot, zero in all stocks
    return explore_build_sequences(TIME_LIMIT, (1, 0, 0, 0, 0), (0, 0, 0, 0, 0))


def compute_qualities(bps: list[Blueprint]) -> list[tuple[int, int]]:
    return [(bp.id, bp.id * maximize_diamonds(bp)) for bp in bps]