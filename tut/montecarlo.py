import random


def pi(trials=10**6):
    in_circle = 0

    for _ in xrange(trials):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            in_circle += 1

    return float(in_circle) / trials * 4

if __name__ == '__main__':
    print pi()