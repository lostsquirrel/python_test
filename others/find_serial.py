from pathlib import Path


def main():
    s = {x + 1 for x in range(138)}

    c = Path()
    for x in c.iterdir():
        if x.is_file() and not x.name.endswith(".py"):
            _x = x.name.split("-")
            serial = _x[0]
            print(serial)
            s.discard(int(serial))

    print(s)


if __name__ == '__main__':
    main()
