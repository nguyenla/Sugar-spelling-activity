#!/usr/bin/env python

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk
import os
from GameView import GameView

class GameController:
    def __init__(self):
        self.view = GameView()
        # When the window is given the "delete_event" signal (this is given
        # by the window manager, usually by the "close" option, or on the
        # titlebar), we ask it to call the delete_event () function
        # as defined above. The data passed to the callback
        # function is NULL and is ignored in the callback function.
        self.view.window.connect("delete_event", self.delete_event)

        # Here we connect the "destroy" event to a signal handler.
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.

        self.view.window.connect("destroy", self.destroy)

        # This will cause the window to be destroyed by calling
        # gtk_widget_destroy(window) when "clicked".  Again, the destroy
        # signal could come from here, or the window manager.

        self.view.button.connect_object("clicked", self.playWord, "Play Word")
        self.view.nextButton.connect_object("clicked", self.nextWord, "Next Word")
        self.view.wordField.connect("activate", self.checkEntryText, self.view.wordField)
        self.view.vbox.connect('expose-event', self.addImage)

        self.dictionary = {}
        self.load_words("words-level1")
        # for word in self.dictionary["words-level1"]:
        #     print word

        # define words for the level
        self.level1Words = self.dictionary["words-level1"]
        self.currentIndex = 0
        self.score = 0

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
            self.view.resultLabel.set_text("CORRECT!")
            self.view.nextButton.set_label("NEXT")
            self.score += 10;
            os.system("espeak 'CORRECT'")
        else:
            self.view.resultLabel.set_text("INCORRECT!")
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
            self.view.resultLabel.set_text("")
            self.view.wordField.set_text("")
            self.view.nextButton.set_label("SKIP")


    def load_words(self, filename):
        file = open(filename)
        word = file.readline()
        wordlist = []
        while len(word) > 0:
            wordlist.append(word)
            word = file.readline()

        self.dictionary[filename] = wordlist

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()


def main():
    game = GameController()
    gtk.main()


if __name__ == "__main__": main()
