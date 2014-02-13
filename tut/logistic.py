from tut import charts


def logistic_step(x, r):
    return r * x * (1.0 - x)


def logistic_regression(r, x, steps=300):
    data = []
    for i in xrange(steps):
        data.append(x)
        x = logistic_step(x, r)
    return data


def _get_stabilized_dynamic(data, count_after):
    data = data[count_after:]
    return sorted(list(set(data)))


def bifurcation():
    x = 0.001
    steps = 300
    count_after = 200
    ret = []
    rvals = [r / 100.0 for r in xrange(100, 399)]
    for r in rvals:
        data = logistic_regression(r, x, steps)
        fixed_points = _get_stabilized_dynamic(data, count_after)
        ret.append(fixed_points)
    return rvals, ret


def print_regresion():
    data = logistic_regression(3.4, 0.001)
    charts.print_chart([d*100 for d in data])


def print_bifurcation():
    rvals, data = bifurcation()

    grid = [[0]*100 for _ in xrange(len(data))]
    for j, rv in enumerate(data):
        for fixed_point in rv:
            i = int(80*fixed_point)
            grid[j][i] = 1
    charts.print_grid(grid, 100, len(data), legend_h=rvals)


if __name__ == '__main__':
    print_bifurcation()
