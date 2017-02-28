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
        self.level = 1
        self.score = 0
        self.dictionary = {} # A dictionary of all the words used in the game
        self.level_words = [] # the list of words to be played
        self.currentIndex = 0 # index of the current word that is pronounced
        self.check_current_word = False # keep track of whether the current word has been checked
        self.typed = "" # keeps track of what the user has typed so far
        self.skipped = [] # list of words that are skipped

        # Set the game up for the first level
        self.next_level()
        self.view.typeBox.createTextBoxes(len(self.level_words[0]))
        self.es = espeak.ESpeak(voice="en+f1", speed = 230)

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

    # This function checks if the typed word are correctly spelled
    def checkEntryText(self, typed):
        if self.level_words[self.currentIndex] == typed.upper():
            self.view.resultLabel.set_text("CORRECT!")
            self.view.nextButton.set_label("NEXT")
            self.update_score(10)
            self.check_current_word = True
        else:
            self.view.resultLabel.set_text("INCORRECT!")


    # This function plays the audio for the current word
    def playWord(self, widget, data = None):
        currentWord = self.level_words[self.currentIndex]
        speak = Speak(currentWord)
        speak.start()
        speak.stop()

    # This function gets the next word to be played and display it on the screen
    def nextWord(self, widget, data=None):
        # If the user skips a word, add the skipped word to the skipped list
        if self.view.nextButton.get_label() == "SKIP":
            self.skipped.append(self.level_words[self.currentIndex])

        self.typed = "" # reset the typed field
        self.currentIndex += 1
        self.check_current_word = False # the new word has not been checked

        # reach the end of level
        if self.currentIndex == len(self.level_words):
            if self.score >= 70: # if the player scores well enough
                # finalText = "LEVEL COMPLETED. You scored " + str(self.score) + " out of " + str(len(self.level_words) * 10)
                finalText = "LEVEL COMPLETED."
                os.system("espeak '{}'".format(finalText))
                self.review_level()
                self.level += 1

            else: # if the player skips too many words
                message = "Level incomplete. You skipped too many words. "
                + "You need at least 70 points to move to the next level"
                self.es.say(message)
                # os.system("espeak '{}'".format(message))
                self.currentIndex = 0
                self.level_words = self.skipped # Go over the list of skipped words

        else: # play the next word and create the corresponding textboxes
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

    # This function updates the score of the player by the value specified by the increment parameter
    def update_score(self, increment):
        self.score += increment
        self.view.scoreLabel.set_text("SCORE: " + str(self.score))

    # This function brings up the review screen when a level ends
    def review_level(self):
        self.view.show_review_screen()
        self.view.nextButton.connect_object("clicked", self.next_level, "Next Word")

    # Add the background picture
    def addImage(self, widget, event):
        path = 'background.jpg'
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0,0)

    # Process the key pressed by the player
    def readKey(self, widget, event):
        keyval = event.keyval
        keyval_name = gtk.gdk.keyval_name(keyval)

        # Backspace function
        if keyval_name == 'BackSpace':
            self.typed = self.typed[:len(self.typed)-1] # remove the last character of the string stored in self.typed
            self.view.typeBox.addWord(self.typed) # update the display

        # Enter function
        elif keyval_name == 'Return':
            if self.check_current_word == False: # if the word hasn't been validated yet
                self.checkEntryText(self.typed)
            else:
                self.nextWord(self.view.nextButton) # move on to the next word

        # if the key entered is a character, and if the textboxes have not been all filled
        elif keyval_name.isalpha() and len(keyval_name) == 1 and len(self.typed) < len(self.level_words[self.currentIndex]):
            self.typed = self.typed + keyval_name # append new character to the word typed by the player
            self.view.typeBox.addWord(self.typed) # update display

    # Get the words for the next level and reset the view
    def next_level(self, widget = None):
        self.load_words("words-level" + str(self.level))

        # define words for the level
        self.level_words = self.dictionary["words-level" + str(self.level)]
        self.currentIndex = 0 # reset the current index
        self.check_current_word = False

        self.typed = "" # reset the display
        self.view.vbox.add(self.view.typeBox.hbox)
        self.view.typeBox.createTextBoxes(len(self.level_words[0]))
        self.view.label.set_text("LEVEL " + str(self.level))
        self.view.vbox.remove(self.view.hbox)
        self.view.vbox.add(self.view.hbox)

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()


def main():
    game = GameController()
    gtk.main()


if __name__ == "__main__": main()
