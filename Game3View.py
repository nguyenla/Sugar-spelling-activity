import pygtk
pygtk.require('2.0')
import gtk
from RootView import RootView
from TypeBoxVert import TypeBoxVert

class Game3View:
    def __init__(self, window):
        self.window = window
        #create the buttons for the game. Make sure you can't select them
        self.skip = gtk.Button("SKIP")
        self.skip.set_can_focus(False)
        self.word1 = gtk.Button("word1")
        self.word1.set_can_focus(False)
        self.word2 = gtk.Button("word2")
        self.word2.set_can_focus(False)
        self.word3 = gtk.Button("word3")
        self.word3.set_can_focus(False)
        self.word4 = gtk.Button("word4")
        self.word4.set_can_focus(False)
        self.word5 = gtk.Button("word5")
        self.word5.set_can_focus(False)

	    #create the labels for the game
        self.definition = gtk.Label("Definition: ")
        self.def1 = gtk.Label("def1")
        self.label = gtk.Label("LEVEL 1")
        self.scoreLabel = gtk.Label("SCORE: 0")
        self.resultLabel = gtk.Label("")
        self.skipLabel = gtk.Label("Skips left: 0")
        #create a vertical box and add it to the window
        self.vbox = gtk.VBox(False, 0)
        self.window.add(self.vbox)
        self.vbox.show()

	    #put the horizontal box in the vertical box. This allows for proper
        #placement of the defintion on the screen
        self.vbox.pack_start(self.label, True, True, 0)
        self.hbox2 = gtk.HBox(False,0)
        self.hbox2.pack_start(self.definition, False, False, 0)
        self.hbox2.pack_start(self.def1, False, False,0)
        self.vbox.add(self.hbox2)
        #stacks the word buttons and result label vertically on the screen,
        self.vbox.pack_start(self.word1, False, False, 0)
        self.vbox.pack_start(self.word2, False, False, 0)
        self.vbox.pack_start(self.word3, False, False, 0)
        self.vbox.pack_start(self.word4, False, False, 0)
        self.vbox.pack_start(self.word5, False, False, 0)
        self.vbox.pack_start(self.resultLabel, True, True, 0)
        #puts the score label, skip button, and skipLabel horizontally at the
        #bottom of the vertical box
        self.hbox = gtk.HBox(False, 0)
        self.hbox.pack_start(self.scoreLabel, True, True, 0)
        self.hbox.pack_start(self.skip, True, True, 0)
        self.hbox.pack_start(self.skipLabel, True, True, 0)
        self.vbox.add(self.hbox)
        self.hbox2.show()
        self.hbox.show()

        # Makes everything visible on the screen
        self.skip.show()
        self.word1.show()
        self.word2.show()
        self.word3.show()
        self.word4.show()
        self.word5.show()
        self.definition.show()
        self.def1.show()
        self.label.show()
        self.scoreLabel.show()
        self.resultLabel.show()
        self.skipLabel.show()

        self.window.show()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()
