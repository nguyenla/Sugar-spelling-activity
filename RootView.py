import pygtk
pygtk.require('2.0')
import gtk
from TypeBox import TypeBox

class RootView:
    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.resize(400,400)

        # Sets the border width of the window.
        self.window.set_border_width(20)
        self.window.show()
