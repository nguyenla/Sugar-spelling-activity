import pygtk
pygtk.require('2.0')
import gtk
from TypeBox import TypeBox

class HomeView:
    def __init__(self, window):
        self.window = window

        # Creates a new button with the label "Hello World".
        self.button = gtk.Button("Game 1")
        self.button.set_can_focus(False)

        self.nextButton = gtk.Button("Game 2")
        self.nextButton.set_can_focus(False)

        self.vbox = gtk.VBox(False, 0)
        self.window.add(self.vbox)
        self.vbox.show()

        self.hbox = gtk.HBox(False, 0)
        self.hbox.pack_start(self.button, True, True, 0)
        self.hbox.pack_start(self.nextButton, True, True, 0)
        self.vbox.add(self.hbox)
        self.hbox.show()

        # The final step is to display this newly created widget.
        self.button.show()
        self.nextButton.show()