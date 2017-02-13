#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os
from GameView import GameView
from RootView import RootView
import sys
sys.path.append("python-espeak/")
from HomeView import HomeView
from Speak import Speak
import espeak

class GameController:
    def __init__(self, view):
        # Engine to produce sound for any word
        # self.es = espeak.ESpeak()
        self.view = view
        self.view.window.connect("key-press-event", self.readKey)
        self.view.button.connect_object("clicked", self.playWord, "Play Word")
        self.view.nextButton.connect_object("clicked", self.nextWord, "Next Word")
        self.view.vbox.connect('expose-event', self.addImage)

        # Fields of the controller
        self.dictionary = {} # Keep all the words used in the game
        self.level_words = []
        self.level = 1
        self.currentIndex = 0 # index of the current word that is pronounced
        self.score = 0
        self.check_current_word = False # keep track of whether the current word has been typed correctly
        self.typed = "" # This field keeps track of what the user has typed so far
        self.skipped = [] # List of words that are skipped

        # Set the game up for the first level
        self.next_level()
        self.view.typeBox.createTextBoxes(len(self.level_words[0]))


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

    def checkEntryText(self, typed):
        if self.level_words[self.currentIndex] == typed.upper():
            self.view.resultLabel.set_text("CORRECT!")
            self.view.nextButton.set_label("NEXT")
            self.updateScore(10)
            self.check_current_word = True
        else:
            self.view.resultLabel.set_text("INCORRECT!")


    def playWord(self, widget, data=None):
        currentWord = self.level_words[self.currentIndex]
        speak = Speak(currentWord)
        speak.start()
        speak.stop()

    def nextWord(self, widget, data=None):
        self.typed = ""
        self.currentIndex += 1
        print self.currentIndex
        self.check_current_word = False

        if self.currentIndex == len(self.level_words):
            finalText = "LEVEL COMPLETED. You score " + str(self.score) + " out of " + str(len(self.level_words) * 10)
            os.system("espeak '{}'".format(finalText))
            self.level += 1
            self.next_level()
            # TO-DO: Render the view for the next level

        else:
            self.playWord(self.view)
            self.view.typeBox.createTextBoxes(len(self.level_words[self.currentIndex]))
            self.view.resultLabel.set_text("")
            self.view.nextButton.set_label("SKIP")

    # This function takes in a file name and load all the words from the corresponding file
    def load_words(self, filename):
        file = open(filename)
        word = file.readline()
        wordlist = []
        while len(word) > 0:
            wordlist.append(word[:len(word)-1])
            word = file.readline()

        # a global dictionary that keeps track of all the words used by levels
        self.dictionary[filename] = wordlist

    def updateScore(self, increment):
        self.score += increment
        self.view.scoreLabel.set_text("SCORE: " + str(self.score))

    def addImage(self, widget, event):
        path = 'background.jpg'
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0,0)

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    # Process the key pressed by the player
    def readKey(self, widget, event):
        keyval = event.keyval
        keyval_name = gtk.gdk.keyval_name(keyval)

        # Backspace function
        if keyval_name == 'BackSpace':
            self.typed = self.typed[:len(self.typed)-1]
            self.view.typeBox.addWord(self.typed)

        elif keyval_name == 'Return':
            if self.check_current_word == False:
                self.checkEntryText(self.typed)
            else:
                self.nextWord(self.view.nextButton)

        elif keyval_name.isalpha() and len(keyval_name) == 1 and len(self.typed) < len(self.level_words[self.currentIndex]):
            self.typed = self.typed + keyval_name
            self.view.typeBox.addWord(self.typed)

    # Get the words for the next level and reset the view
    def next_level(self):
        self.load_words("words-level" + str(self.level))

        # define words for the level
        self.level_words = self.dictionary["words-level" + str(self.level)]
        self.currentIndex = 0
        self.check_current_word = False

        # This field keeps track of what the user has typed so far
        self.typed = ""
        self.view.typeBox.createTextBoxes(len(self.level_words[0]))
        self.view.label.set_text("LEVEL " + str(self.level))

def main():
    game = GameController()
    gtk.main()


if __name__ == "__main__": main()