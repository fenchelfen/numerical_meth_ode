def heun_new(x, y, h, func):
    return y + h / 2 * (func(x, y) + \
                        func(x + h, y + h * \
                             func(x, y)))


def heun_compute(x0, y0, h, func, X):
    x, y = x0, y0
    pairs = list()
    while (x <= X):
        pairs.append((x, y));
        y = heun_new(x, y, h, func)
        x += h
    return pairs


def main():
    pass


if __name__ == "__main__":
    main()
