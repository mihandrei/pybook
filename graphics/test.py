from graphics import draw, m3d, view, gui

P = [(255,255,255), (255,0,0), (200,100,0), (255,255,0), (0,255,0), (0,0,255)] * 10


def text_test():
    b = m3d.zeros((10, 10))
    # b[2][3] =2
    # b[8][2:5] = [5]*3
    draw.line(b, (1, 1), (8, 1), color=1)
    draw.line(b, (1, 1), (1, 8), color=2)
    draw.line(b, (1, 1), (8, 8), color=5)
    # draw.line(b, bs, (1, 1) , (9, 9))
    view.m_print(b)

    
def line_test():
    b = m3d.zeros((400, 400))
    draw.line(b, (40, 40), (320, 40), color=P[0])
    draw.line(b, (40, 40), (40, 320), color=P[1])
    draw.line(b, (40, 40), (320, 320), color=P[2])
    draw.line(b, (40, 40), (80, 320), color=P[3])
    draw.line(b, (40, 40), (320, 80), color=P[4])
    draw.line(b, (320, 80), (80, 320), color=P[5])
    return b


def render_test(t=0):
    vertices = [
        (0,0,0), (1,0,0), (1,1,0), (0,1,0), 
        (0,0,1), (1,0,1), (1,1,1), (0,1,1),         
        ]
    colors = [
        P[1], P[1], P[2],
        P[2], P[2], P[3],
        P[3], P[4], P[4],
    ]
    indices = [
        0,1,2, 
        2,3,0,
        0,1,5,
        0,5,4,
        0,3,4,
        4,7,3,
        3,2,7,
        2,7,6,
        4,7,5,        
    ]

    b = m3d.zeros((440, 440), (50,50,50))
    draw.render(b, vertices, colors, indices, t/1000.0)
    return b

def render_test2(t=0):
    vertices = [
        (-1,-1,0), (1,-1,0), (1,1,0), (-1,1,0), 
        (0, 0, 2),         
        ]
    colors = [
        P[1], P[2], P[3],
        P[4], P[5]
    ]
    indices = [
        0,1,2, 
        2,3,0,
        4,0,1,
        4,1,2,
        4,2,3,
        4,3,0        
    ]

    b = m3d.zeros((440, 440), (50,50,50))
    draw.render(b, vertices, colors, indices, t/1000.0)
    return b

def animation():
    app = gui.App(render_test2)    
    app.start()

animation()
# text_test()
# view.image_print(line_test(),'line_test.png')
# view.image_print(render_test(), 'render_test.png')