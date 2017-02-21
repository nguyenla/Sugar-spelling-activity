import pygtk
pygtk.require('2.0')
import gtk
from TypeBox import TypeBox

class HomeView:
    def __init__(self, window):
        self.window = window

        self.gameName = gtk.Label("")
        self.gameName.set_markup("<span size='18000' color='#F5F6F7'><b>SPELL IT!</b></span>")

        # Creates a new button with the label "Hello World".
        self.button = gtk.Button("Game 1")
        self.button.set_can_focus(False)
        self.button.set_size_request(150,150)

        self.button2 = gtk.Button("Game 2")
        self.button2.set_can_focus(False)
        self.button2.set_size_request(150,150)

        self.button3 = gtk.Button("Game 3")
        self.button3.set_can_focus(False)
        self.button3.set_size_request(150,150)

        # image = gtk.Image()
        # image.set_from_file("background.png")
        # image.show()
        # self.nextButton.add(image)
        # #make a gdk.color for red
        # map = self.nextButton.get_colormap()
        # color = map.alloc_color("#2F343F")

        # #copy the current style and replace the background
        # style = self.nextButton.get_style().copy()
        # style.bg[gtk.STATE_NORMAL] = color

        # #set the button's style to the one you created
        # self.nextButton.set_style(style)

        self.vbox = gtk.VBox(True, 0)
        self.window.add(self.vbox)
        self.vbox.show()


        eb = gtk.EventBox()
        eb.add(self.gameName)
        eb.set_size_request(150,50)
        eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#2F343F"))

        valign = gtk.Alignment(0, 0, 1, 0)
        valign.add(eb)
        self.vbox.pack_start(valign, True, True, 0)
        valign.show()

        self.selectGame = gtk.Label("")
        self.selectGame.set_size_request(150,30)
        self.selectGame.set_markup("<span size='25000' color='#2F343F'><b><u>SELECT A GAME</u></b></span>")
        self.selectGame.show()

        valign2 = gtk.Alignment(0, 0, 1, 0)
        valign2.add(self.selectGame)
        self.vbox.pack_start(valign2, True, True, 0)
        valign2.show()

        #self.vbox.pack_start(eb, False, False, 0)
        self.gameName.show()
        eb.show()
        self.hbox = gtk.HBox(False, 0)
        self.hbox.pack_start(self.button, False, False, 10)
        self.hbox.pack_start(self.button2, False, False, 10)
        self.hbox.pack_start(self.button3, False, False, 10)
        self.vbox.pack_start(self.hbox, False, False, 10)
        self.hbox.show()


        # The final step is to display this newly created widget.
        self.button.show()
        self.button2.show()
        self.button3.show()
