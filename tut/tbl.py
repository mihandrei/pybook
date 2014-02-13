from collections import defaultdict
import os
import re
import sys


def compute_column_widths(rows):
    col_w = defaultdict(int)

    for r in rows:
        for i, c in enumerate(r):
            col_w[i] = max(col_w[i], len(str(c)))

    return [col_w[i] for i in sorted(col_w.keys())]


def format_table(rows, pad=2):
    if not rows:
        rows = [["* no data *"]]

    col_w = compute_column_widths(rows)

    def prow(r, pch=' ', d='|'):
        def cell(i, c):
            c = str(c)
            whitespace = col_w[i] - len(c) + 2 * pad
            pre = whitespace / 2
            post = whitespace - pre
            return pch * pre + c + pch * post

        return d + d.join(cell(i, c) for i, c in enumerate(r)) + d

    def sep(pch='-', d='+'):
        return d + d.join(pch * (w + 2 * pad) for w in col_w) + d

    head_sep = sep('=')
    row_sep = sep('-')

    first, rest = rows[0], rows[1:]

    tbl = []
    tbl.append(sep('='))
    tbl.append(prow(first))
    tbl.append(sep('='))

    for r in rest:
        tbl.append(prow(r))
        tbl.append(sep('-'))

    return '\n'.join(tbl)


def lspy(d='.'):
    out = []
    for f in sorted(os.listdir(d)):
        if f.endswith('.py'):
            out.append([f])
    print format_table([['name']] + out)


def grep_file(f, pattern):
    res = []
    with open(f, 'r') as fo:
        for i, line in enumerate(fo):
            if re.match(pattern, line):
                res.append((i, line.rstrip()))
    return res


def grep_py(d, pattern):
    out = []

    for f in sorted(os.listdir(d)):
        if f.endswith('.py'):
            for lnr, l in grep_file(f, pattern):
                out.append([f, lnr, l[:70]])

    print format_table([['name', 'lineno', 'line']] + out)


def full_coverage_oh_my():
    print format_table([['nume', 'verb', 'ce'],
                        ['ana', 'are', 'mere'],
                        ['nina', 'are', 'pere'],
                        ['aa', 'fs']])
    print format_table([])
    lspy()
    grep_py('.', '\s*def')


def partial_coverage():
    print format_table([['nn', 'ss'], ['99', '00']])


if __name__ == '__main__':
    full_coverage_oh_my()
