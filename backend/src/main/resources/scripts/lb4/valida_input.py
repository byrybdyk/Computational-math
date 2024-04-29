import sys


def validate_pairs():
    pairs = []
    try:
        for arg in sys.argv[1:9]:
            x, y = map(float, arg.replace(",", ".").split(" "))
            pair = [x, y]
            pairs.append(pair)

        for arg in sys.argv[9:]:
            if arg.strip():
                x, y = map(float, arg.replace(",", ".").split(" "))
                pair = [x, y]
                pairs.append(pair)
            else:
                continue
    except ValueError:
        print("Incorrect value entered")
        exit()
    return pairs
