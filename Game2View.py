import pygtk
pygtk.require('2.0')
import gtk
from RootView import RootView
from TypeBox import TypeBox

class Game2View:
    def __init__(self, window):
        self.window = window

        #Generate the necessary buttons
        self.word1 = gtk.Button("word1")
        self.word1.set_can_focus(False)

	self.word2 = gtk.Button("word2")
        self.word2.set_can_focus(False)

	self.word3 = gtk.Button("word3")
        self.word3.set_can_focus(False)

	self.word4 = gtk.Button("word4")
        self.word4.set_can_focus(False)

        self.skip = gtk.Button("SKIP")
        self.skip.set_can_focus(False)

	self.next = gtk.Button("NEXT LEVEL")
        self.skip.set_can_focus(False)

	#Generate the necessary labels
        self.levelLabel = gtk.Label("LEVEL 1")
        self.scoreLabel = gtk.Label("SCORE: 0")
        self.resultLabel = gtk.Label("")
	self.skipLabel = gtk.Label("SKIPS LEFT: 0")


        #self.button.set_size_request(20,30)

        self.vbox = gtk.VBox(False, 0)
        self.window.add(self.vbox)
        self.vbox.show()

	#Pack the first box with everything
        self.vbox.pack_start(self.levelLabel, True, True, 0)
        self.vbox.pack_start(self.word1, True, True, 0)
        self.vbox.pack_start(self.word2, True, True, 0)
        self.vbox.pack_start(self.word3, True, True, 0)
        self.vbox.pack_start(self.word4, True, True, 0)
        self.vbox.pack_start(self.resultLabel, True, True, 0)


        self.hbox = gtk.HBox(False, 0)

	self.hbox.pack_start(self.scoreLabel, True, True, 0)
        self.hbox.pack_start(self.skip, True, True, 0)
        self.hbox.pack_start(self.next, True, True, 0)
        self.hbox.pack_start(self.skipLabel, True, True, 0)
	

        self.vbox.add(self.hbox)
        self.hbox.show()


        # The final step is to display this newly created widget.
        self.skip.show()
        self.word1.show()
        self.word2.show()
        self.word3.show()
        self.word4.show()
        self.levelLabel.show()
        self.scoreLabel.show()
        self.resultLabel.show()
	self.skipLabel.show()

        self.window.show()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()
