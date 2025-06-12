TIME_LIMIT = 24

RESOURCE_TYPES = 5
ORE, CLAY, OBSIDIAN, GEODE, DIAMOND = range(RESOURCE_TYPES)

PATTERN = (
    r"Blueprint (\d+):"
    r" Each ore robot costs (\d+) ore\."
    r" Each clay robot costs (\d+) ore\."
    r" Each obsidian robot costs (\d+) ore and (\d+) clay\."
    r" Each geode robot costs (\d+) ore and (\d+) obsidian\."
    r" Each diamond robot costs (\d+) geode, (\d+) clay and (\d+) obsidian\."
)
