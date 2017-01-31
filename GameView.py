import pygtk
pygtk.require('2.0')
import gtk

class GameView:
    def __init__(self):

        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.resize(400,400)

        # Sets the border width of the window.
        self.window.set_border_width(20)

        # Creates a new button with the label "Hello World".
        self.button = gtk.Button("Play Word")
        self.nextButton = gtk.Button("SKIP")
        self.wordField = gtk.Entry(max=10)
        self.label = gtk.Label("LEVEL 1")
        self.resultLabel = gtk.Label("")

        self.button.set_size_request(20,30)

        self.vbox = gtk.VBox(False, 0)
        self.window.add(self.vbox)
        self.vbox.show()

        self.vbox.pack_start(self.label, True, True, 0)
        self.vbox.pack_start(self.wordField, True, True, 0)
        self.vbox.pack_start(self.resultLabel, True, True, 0)

        self.hbox = gtk.HBox(False, 0)

        self.hbox.pack_start(self.button, True, True, 0)
        self.hbox.pack_start(self.nextButton, True, True, 0)

        self.vbox.add(self.hbox)
        self.hbox.show()


        # The final step is to display this newly created widget.
        self.button.show()
        self.nextButton.show()
        self.wordField.show()
        self.label.show()
        self.resultLabel.show()

        # and the window
        self.window.show()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    hello = GameView()
    hello.main()
