from solve import compute_qualities
from io_methods import write_report, parse_blueprints
import sys


def main(file: str):
    try:
        blueprints = parse_blueprints(file)
        results = compute_qualities(blueprints)
        write_report(results)
    except ValueError as e:
        print(f"{str(e)}\nInvalid input format.")
        exit(1)

    print(f"Done. Check analysis.txt for results.")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Please provide a file to analyse")
        exit(1)

    file = sys.argv[1]
    main(file)
