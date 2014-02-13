from Image import Image
from graphics import m3d


def m_print(m):
    rows, _ = m3d.shape(m)
    print '['
    for j in xrange(rows):
        print ' [' + ', '.join(str(e) for e in m[j]) + '],'        
    print ']'

def image_print(m, name='lines.png'):
    shape = m3d.shape(m)
    im = Image.new('RGB', shape)

    for j in xrange(shape[0]):
        for i in xrange(shape[1]):
            im.putpixel((i,j), m[j][i])
    im.save(name)    