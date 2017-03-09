#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os
from Game2View import Game2View
from RootView import RootView
import sys
from HomeView import HomeView
from random import randint
from random import shuffle
import time

class Game2Controller:
    def __init__(self, view):
        self.view = view

        self.view.skip.connect_object("clicked", self.skip_press, "SKIP")
        self.view.next.connect_object("clicked", self.generate_level, "NEXT LEVEL")
	self.view.word1.connect_object("clicked", self.check, "0")
	self.view.word2.connect_object("clicked", self.check, "1")
	self.view.word3.connect_object("clicked", self.check, "2")
	self.view.word4.connect_object("clicked", self.check, "3")
        self.view.vbox.connect('expose-event', self.addImage)

        # Fields of the controller
        self.level = 0
        self.score = 0
	self.skipsLeft = 0
        self.incorrectList = []
        self.correctList = []
	self.incorrectWord = ""
	self.roundList = []

        # Set the game up for the first level
        self.generate_level("")

    #Generate level by loading the level's incorrect words & make a round
    def generate_level(self, widget):
	self.reveal_screen()
	self.skipsLeft = 3
	self.view.skipLabel.set_text("Skips left:" + str(self.skipsLeft))
	self.level = self.level + 1
	self.load_level_correct()
	self.load_level_incorrect()
	self.make_round()


    #Function populates the 4 buttons for the round (3 correct, 1 incorrect)
    def make_round(self):
	self.roundList = []
        self.incorrectWord = ""
	picked = []

	#generate a word list for this round and randomly assign them
	while len(picked)<3:
	    x = randint(0,len(self.correctList)-1)
	    if x not in picked:
	        self.roundList.append(self.correctList[x])
	    	picked.append(x)

	#Randomly pick the round's incorrect word
	self.incorrectWord = self.incorrectList[randint(0,len(self.incorrectList)-1)]
	self.roundList.append(self.incorrectWord)

	#Randomizes where the words appear
	shuffle(self.roundList)
	self.view.word1.set_label(self.roundList[0])
	self.view.word2.set_label(self.roundList[1])
	self.view.word3.set_label(self.roundList[2])
	self.view.word4.set_label(self.roundList[3])


    #Function checks the button pressed to see if the player is correct
    def check(self, widget):
	target = self.roundList[int(widget)]
	#if the user selected word is the incorrect word, take it out, update score, make new round
	if target in self.incorrectList:
	    self.updateScore(10)
	    del self.incorrectList[self.incorrectList.index(target)]

	    if len(self.incorrectList) == 0:
	        print "LEVEL OVER"
		self.level_over()
	    else:
		self.view.resultLabel.set_text("")
	        self.make_round()
	#else, keep the incorrect word in the level and make new round
	else:
	   self.view.resultLabel.set_text("Wrong! Try again!")
	   self.make_round()

    #Function updates score
    def updateScore(self, increment):
        self.score += increment
        self.view.scoreLabel.set_text("SCORE: " + str(self.score))

    #Function occurs when the skip button is pressed
    def skip_press(self, widget):
	#if there are skips left, load new round & decrement skips
	if self.skipsLeft > 0:
            self.make_round()
	    self.skipsLeft = self.skipsLeft - 1
	    self.view.skipLabel.set_text("Skips left:" + str(self.skipsLeft))
	    self.view.resultLabel.set_text("")
	#if none left, disable button
	if self.skipsLeft == 0:
	    self.view.skip.set_sensitive(False)

    #temporary level over function
    def level_over(self):
	self.view.skip.hide()
        self.view.word1.hide()
        self.view.word2.hide()
        self.view.word3.hide()
        self.view.word4.hide()
        self.view.scoreLabel.hide()
	self.view.skipLabel.hide()

	self.view.levelLabel.set_text("LEVEL " + str(self.level+1))
        self.view.resultLabel.set_text("Ready for the next level?")
	self.view.next.show()

    def reveal_screen(self):
	self.view.skip.show()
	self.view.word1.show()
        self.view.word2.show()
        self.view.word3.show()
        self.view.word4.show()
        self.view.scoreLabel.show()
	self.view.skipLabel.show()

        self.view.resultLabel.set_text("")
	self.view.next.hide()

#Text File Methods
    # This function takes in a file name and load all the words from the corresponding file
    def load_file(self, filename):
        file = open(filename)
        word = file.readline()
        wordlist = []
        while len(word) > 0:
            wordlist.append(word[:len(word)-1])
            word = file.readline()
	return wordlist

    # This function takes in a file name and load all the words from the corresponding file
    def load_level_correct(self):
        self.correctList = self.load_file("Game2-CorrectLevel" + str(self.level))

    # This function takes in a file name and load all the words from the corresponding file
    def load_level_incorrect(self):
        self.incorrectList = self.load_file("Game2-IncorrectLevel" + str(self.level))


#General Methods
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

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()


def main():
    game = Game2Controller()
    gtk.main()


if __name__ == "__main__": main()
