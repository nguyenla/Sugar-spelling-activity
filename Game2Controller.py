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

class Game2Controller:
    def __init__(self, view):
        self.view = view

#        self.view.skip.connect_object("clicked", self.skip, "SKIP")
        self.view.vbox.connect('expose-event', self.addImage)

        # Fields of the controller
        self.level = 1
        self.score = 0
	self.skipsLeft = 3
        self.incorrectWords = []
        self.correctWords = [] 

        # Set the game up for the first level
	self.get_correct("Game2-CorrectlySpelled")
        self.generate_level()

    def generate_level(self):
	self.load_level_incorrect(self.level)
	self.make_round()

    def make_round(self):
	roundList = []
	picked = []
	#generate a word list for this round and randomly assign them	
	for i in range(3):
	    x = randint(0,len(self.correctWords)-1)
	    if x not in picked:
	        roundList.append(self.correctWords[x])
	    picked.append(x)
	roundList.append(self.incorrectWords[randint(0,len(self.incorrectWords)-1)])

	self.view.word1.set_label(roundList[0])
	self.view.word2.set_label(roundList[1])
	self.view.word3.set_label(roundList[2])
	self.view.word4.set_label(roundList[3])


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
    def get_correct(self, filename):
        self.correctWords = self.load_file(filename)

    # This function takes in a file name and load all the words from the corresponding file
    def load_level_incorrect(self, levelNum):
        self.incorrectWords = self.load_file("Game2-IncorrectlySpelled" + str(levelNum))







    def updateScore(self, increment):
        self.score += increment
        self.view.scoreLabel.set_text("SCORE: " + str(self.score))


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
