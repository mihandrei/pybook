def fixed_point(f, x0, epsilon=0.0001, max_it=10000):
    """f:\\R -> \\R fixpoint"""
    iters = 0
    xp = float(x0)
    x = f(xp)
    while abs(x - xp) > epsilon:
        iters += 1
        if iters >= max_it:
            raise ValueError('failed to converge')
        xp = x
        x = f(x)
    return x


def sqrt(a):
    def _newton_sqrt_iter(x):
        return 0.5 * (x + a / x)

    return fixed_point(_newton_sqrt_iter, 1)


def test1():
    print fixed_point(lambda x: x + 1 if x < 5 else x, 1.6)


def test2():
    print sqrt(2)


def test3():
    print fixed_point(lambda x: x + 1, 0)


if __name__ == '__main__':
    test1()
    test2()
    test3()
