#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os
from Game3View import Game3View
from RootView import RootView
import sys
from HomeView import HomeView
from random import randint
from random import shuffle

class Game3Controller:
    def __init__(self, view):
        self.view = view

        self.view.skip.connect_object("clicked", self.skip_press, "SKIP")
        self.view.word1.connect_object("clicked", self.check_correct, "0")
    	self.view.word2.connect_object("clicked", self.check_correct, "1")
    	self.view.word3.connect_object("clicked", self.check_correct, "2")
    	self.view.word4.connect_object("clicked", self.check_correct, "3")
        self.view.word5.connect_object("clicked", self.check_correct, "4")
        self.view.vbox.connect('expose-event', self.addImage)

        # Fields of the controller
        self.level = 1
        self.score = 0
        self.skipsLeft = 3
        self.definitions = []
        self.Words = []
        self.roundList = []
        self.picked = []
        self.def_array = []
        self.isNext = False
        self.gotPoints = False
        self.view.skipLabel.set_text("Skips left:" + str(self.skipsLeft))
        self.get_correct("Game2-CorrectLevel1")
        self.generate_level()

    def generate_level(self):
	    self.load_level_definitions()
	    self.make_round()


    #INDEXERROR seems to occur sometimes where an incorrect word is saved into the word3
    # no clue why yet
    def make_round(self):
        self.view.resultLabel.set_text("")
        self.view.skip.set_label("SKIP")
        self.gotPoints = False
        self.roundList = []
        self.picked = []
        self.def_array = []
	#generate a word list for this round and randomly assign them
        while len(self.roundList) < 5:
	        x = randint(0,len(self.Words)-1)
	        if x not in self.picked:
	            self.roundList.append(self.Words[x])
                    self.def_array.append(x)
                    self.picked.append(x
        shuffle(self.picked)
        self.view.def1.set_text(self.definitions[self.picked[0]])
        self.view.word1.set_label(self.roundList[0])
        self.view.word2.set_label(self.roundList[1])
        self.view.word3.set_label(self.roundList[2])
        self.view.word4.set_label(self.roundList[3])
        self.view.word5.set_label(self.roundList[4])


    def skip_press(self,widget):
        if self.isNext:
            self.skipsLeft += 1
            self.isNext = False
        if self.skipsLeft > 0:
            self.make_round()
	    self.skipsLeft = self.skipsLeft - 1
	    self.view.skipLabel.set_text("Skips left:" + str(self.skipsLeft))
        else:
            self.view.resultLabel.set_text("No Skips Left!")


    def check_correct(self,widget):
        #need to check to see if the spot in the word file in the same as
        #in the definition file. If they are on the same line then it matches
        #If they are not, then the answer is wrong. Once the player gets it correct
        #remove the definition from the potential list and the word from the list.
        #print "In def_array"
        #print self.def_array[int(widget)]
        #print "defintions at picked"
        #print self.definitions.index(self.definitions[self.picked[0]])
        if self.definitions.index(self.definitions[self.picked[0]]) == self.def_array[int(widget)]:
            self.view.resultLabel.set_text("CORRECT!")
            self.updateScore(10)
            self.view.skip.set_label("NEXT")
            self.isNext = True
            self.gotPoints = True
        else:
            #if self.gotPoints == False:
            self.view.resultLabel.set_text("INCORRECT!")
        #the player answered enough correctly to move on.
        if len(self.definitions) <= 5:
            print "Level Over"

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
        self.Words = self.load_file(filename)

    # This function takes in a file name and load all the words from the corresponding file
    def load_level_definitions(self):
        self.definitions = self.load_file("CorrectlySpelled - Definitions")







    def updateScore(self, increment):
        if self.gotPoints == False:
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
