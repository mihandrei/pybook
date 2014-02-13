from graphics import m3d


def line(buff, s, e, color):
    """Draws a line segment in the matrix buff
       Starting from  point s to point e
    """
    # print 's=', s, 'e=', e, 'col=', color
    # s must be leftmost. If it is not we swap s with e
    if s[0] > e[0]:
        s, e = e, s

    def vline(x, y, yn):
        """ Draws a vertical recangle.
            The carthesian product of [x] with the closed interval [y yn]
        """
        # we transform an interval like [3,2 ] to [2,3]
        if yn < y:
            y, yn = yn, y
        for j in xrange(y, yn + 1):
            buff[j][x] = color

    sx, sy = s
    ex, ey = e

    if ex == sx:
        #the segment is vertical
        vline(sx, sy, ey)
    else:
        slope = float(ey - sy) / (ex - sx)
        y_previous = sy

        for i in xrange(sx + 1, ex + 1):
            y = int(slope * (i - sx) + sy)  # line equantion
            vline(i, y_previous, y)
            y_previous = y


def frag(buff, points, colors, indices):
    'draws 2d triangles'
    buffs = m3d.shape(buff)

    def visible(p):
        return 0 <= p[0] < buffs[0] and 0 <= p[1] < buffs[1]

    for i in xrange(0, len(indices) - 2, 3):
        a, b, c = indices[i: i + 3]
        pa, pb, pc = points[a], points[b], points[c]
        # print pa, pb, pc
        if visible(pa) and visible(pb) and visible(pc):
            line(buff, pa, pb, colors[a])
            line(buff, pb, pc, colors[b])
            line(buff, pc, pa, colors[c])


def vertex(v, t):
    'transforms 3d poins to 2d screen coords'
    view_matrix = m3d.eye(4)
    # rotate stuff
    view_matrix = m3d.mm_mul(m3d.rot(-0.8 * t, 0.2 * t, 0.1 * t), view_matrix)

    # set up view matrix so that -1,1 x -1,1 is visible in the center of buff
    # vertices in the interval -1,1 will be transformed to 20, 420
    # we assume the buffer is 440x440
    # [-1,1] -> [-100,100]    
    view_matrix = m3d.mm_mul(m3d.scale(100, 100, 100), view_matrix)
    # [-1,1] -> [120,220]    
    view_matrix = m3d.mm_mul(m3d.translation(220, 220, 0), view_matrix)


    # set up projection
    projection_matrix = m3d.ortographic()
    graphics_matrix = m3d.mm_mul(projection_matrix, view_matrix)
    v = m3d.mv_mul(graphics_matrix, [v[0], v[1], v[2], 1])

    point = (v[0] / v[3], v[1] / v[3])
    return point


def render(buff, vertices, colors, indices, t):
    # vertex shading, position only for now
    points = []
    for v in vertices:
        p = vertex(v, t)
        truncated = int(p[0]), int(p[1])
        points.append(truncated)
    # fragment shading
    frag(buff, points, colors, indices)

