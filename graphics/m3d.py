"""
matrix math

As this is a teching tool
simplicity is more important than efficiency
"""

import math

# matrix creation and utilities
# -----------------------------

def zeros(shape, zero=0):
    """creates a zero filled matrix of the given shape"""
    rows, cols = shape
    return [[zero] * cols for _ in xrange(rows)]


def eye(rows):
    r = zeros((rows, rows))
    for i in xrange(rows):
        r[i][i] = 1
    return r


def shape(m):
    """returns the shape of m"""
    return len(m), len(m[0])


# 4x4 matrix multiplications an 4 - row vectors
# ---------------------------------------------

def dot(v1, v2):
    """inner product of row vectors"""
    return sum(v1[i] * v2[i] for i in xrange(4))


def mv_mul(m, v):
    """multiplies a 4 matrix with a 4 row vector"""
    return [dot(m[i], v) for i in xrange(4)]


def mm_mul(m1, m2):
    """multiplies a 4 matrix with a 4 matrix"""
    r = zeros((4, 4))
    for i in xrange(4):
        for j in xrange(4):
            r[i][j] = sum(m1[i][a] * m2[a][j] for a in xrange(4))
    return r


# 3d geometry
# -----------

def _rotz(a):
    c, s = math.cos(a), math.sin(a)
    return [[c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]


def _roty(a):
    c, s = math.cos(a), math.sin(a)
    return [[c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]]


def _rotx(a):
    c, s = math.cos(a), math.sin(a)
    return [[1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]]


def rot(a, b, g):
    return mm_mul(_rotx(g), mm_mul(_roty(b), _rotz(a)))


def translation(x, y, z):
    return [[1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]]


def scale(x, y, z):
    return [[x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]]


def ortographic():
    return [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]