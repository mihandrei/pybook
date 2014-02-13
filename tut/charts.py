def print_chart(data, show_values=False, bar_ch='-'):
    for value in data:
        print '|' + bar_ch * int(value) + 'o ',
        if show_values:
            print str(value)
        else:
            print


def print_grid(g, w, h, legend_w=None, legend_h=None):
    grad = """ .'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""
    if legend_w:
        if legend_h:
            print ' ',
        print ''.join(legend_w)
    for j in xrange(h):
        if legend_h:
            print legend_h[j],
        for i in xrange(w):
            v = g[j][i]
            if v >= len(grad):
                v = len(grad) - 1
            if v < 0:
                v = 0
            print grad[v],
        print


def func(x):
    x = 12*(x-40)/80.0
    val = x
    val -= x**3/(2*3)
    val += x**5/(2*3*4*5)
    val -= x**7/(2*3*4*5*6*7)
    val += x**9/(2*3*4*5*6*7*8*9)
    return 40 + 40 * val


def test_chart():
    print_chart([func(i) for i in xrange(80)])

def test_grid():
    d = 80
    g = [[((i-10)**2 + (j-10)**2)/d for i in xrange(d)] for j in xrange(d)]
    print_grid(g, d, d)

if __name__ == '__main__':
    test_chart()
    test_grid()
