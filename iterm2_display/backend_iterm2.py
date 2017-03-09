import os
import base64
import StringIO
from PIL import Image
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib._pylab_helpers import Gcf
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backends.backend_agg import FigureCanvasAgg

from inline_img import create_inline_image_cmd

def show():
    for manager in Gcf.get_all_fig_managers():
        manager.show()
        Gcf.destroy(manager.num)

def new_figure_manager(num, *args, **kwargs):
    FigureClass = kwargs.pop('FigureClass', Figure)
    thisFig = FigureClass(*args, **kwargs)
    canvas = FigureCanvasAgg(thisFig)
    manager = FigureManagerITerm(canvas, num)
    return manager

class FigureManagerITerm(FigureManagerBase):
    def show(self):
        canvas = self.canvas
        canvas.draw()

        if mpl.__version__ < '1.2':
            buf = canvas.buffer_rgba(0, 0)
        else:
            buf = canvas.buffer_rgba()

        render = canvas.get_renderer()
        w, h = int(render.width), int(render.height)
        im = Image.frombuffer('RGBA', (w, h), buf, 'raw', 'RGBA', 0, 1)

        sio = StringIO.StringIO()
        im.save(sio, 'png')
        sio.seek(0)
        b64img = base64.b64encode(sio.read())

        cmd = create_inline_image_cmd(b64img, is_file=False, height=10)

        os.system('clear')
        print cmd

FigureManager = FigureManagerBase
