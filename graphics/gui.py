from Tkinter import Tk, Canvas, PhotoImage
from graphics import m3d


class App(object):
    def __init__(self, update, fps=8):
        self.t = 0
        self.period = 1000/fps        
        self.update = update
        self.master = Tk()
        
        m = self.update(self.t)
        self.W, self.H = m3d.shape(m)
        self.img = PhotoImage(width=self.W, height=self.H)
        
        canvas = Canvas(self.master, width=self.W, height=self.H)
        canvas.pack()
        canvas.create_image((self.W/2, self.H/2), image=self.img, state="normal")
        self._on_tick()

    def _on_tick(self):  
        def _formatcolor(c):
            return '#{0:02X}{1:02X}{2:02X}'.format(*c)

        m = self.update(self.t)
        self.img.blank()

        lines = []
        for j in xrange(self.H):            
            line = ' '.join(_formatcolor(m[j][i]) for i in xrange(self.W))
            lines.append( '{' + line + '}')
                
        self.img.put(' '.join(lines))                        
        self.master.after(self.period, self._on_tick)
        self.t += self.period

    def start(self):
        self.master.mainloop()