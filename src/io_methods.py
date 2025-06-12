from models.blueprint import Blueprint


def write_report(results: list[tuple[int, int]], path: str = "analysis.txt") -> None:
    lines = [f"Blueprint {id}: {quality}" for id, quality in results]
    best_id = max(results, key=lambda x: x[1])[0]
    lines += ["", f"Best blueprint is the blueprint {best_id}."]
    with open(path, "w") as f:
        f.write("\n".join(lines))


def read_input_file(file: str):
    with open(file, "r") as file_stream:
        return file_stream.readlines()
    return ""


def parse_blueprints(file: str):
    input_str = read_input_file(file)
    blueprints = [Blueprint.from_string(line.strip()) for line in input_str]
    if not blueprints:
        raise ValueError("No blueprints available")
    return blueprints
