import sys


def parse_args():
    result = []
    for var in sys.argv[1:]:
        result.append(var)
    return " ".join(result)
