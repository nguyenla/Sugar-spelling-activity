#!/usr/bin/env python

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk
import os

class HelloWorld:

    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.
    def hello(self, widget, data=None):
        print "Hello World"

    def addImage(self, widget, event):
        path = 'background.jpg'
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0,0)

    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.
        print "delete event occurred"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False
    
    def checkEntryText(self, widget, field):
        if self.level1Words[self.currentIndex] == field.get_text().upper():
            self.resultLabel.set_text("CORRECT!")
            self.nextButton.set_label("NEXT")
            self.score += 10;
            os.system("espeak 'CORRECT'")
        else:
            self.resultLabel.set_text("INCORRECT!")
            os.system("espeak 'INCORRECT'")

    def playWord(self, widget, data=None):
        currentWord = self.level1Words[self.currentIndex]
        os.system("espeak '{}'".format(currentWord))

    def nextWord(self, widget, data=None):
        self.currentIndex += 1
        if self.currentIndex == len(self.level1Words):
            finalText = "LEVEL COMPLETED. You score " + str(self.score) + " out of 40."
            os.system("espeak '{}'".format(finalText))
        else:
            self.resultLabel.set_text("")
            self.wordField.set_text("")
            self.nextButton.set_label("SKIP")

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        
        # define words for the level
        self.level1Words = ["EAT", "PLAY", "RIDE", "FOOD"]
        self.currentIndex = 0
        self.score = 0;
        
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.resize(400,400)
    
        # When the window is given the "delete_event" signal (this is given
        # by the window manager, usually by the "close" option, or on the
        # titlebar), we ask it to call the delete_event () function
        # as defined above. The data passed to the callback
        # function is NULL and is ignored in the callback function.
        self.window.connect("delete_event", self.delete_event)
    
        # Here we connect the "destroy" event to a signal handler.  
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)
    
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


        # This will cause the window to be destroyed by calling
        # gtk_widget_destroy(window) when "clicked".  Again, the destroy
        # signal could come from here, or the window manager.
        self.button.connect_object("clicked", self.playWord, "Play Word")
        self.nextButton.connect_object("clicked", self.nextWord, "Next Word")
        self.wordField.connect("activate", self.checkEntryText, self.wordField)
        self.vbox.connect('expose-event', self.addImage)
    
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
    hello = HelloWorld()
    hello.main()
