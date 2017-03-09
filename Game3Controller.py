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
        #calls the proper method when the button is clicked
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
        self.totalScore = 0
        self.isNext = False
        self.gotPoints = False
        self.nextLevel = False
        self.view.skipLabel.set_text("Skips left:" + str(self.skipsLeft))
        self.generate_level()

    #loads the words and definitions, then sets up the level
    def generate_level(self):
        self.get_correct(self.level)
        self.load_level_definitions(self.level)
        self.make_round()


    #resets the resultLabel and skip button to initial value, and resets gotPoints
    #to false. Sets up the words to display on the buttons and definition to display
    def make_round(self):
        self.view.resultLabel.set_text("")
        self.view.skip.set_label("SKIP")
        self.gotPoints = False
        self.roundList = []
        self.picked = []
        self.def_array = []

	#gets 5 unique words for the round, and the correspoinding defintions
        while len(self.roundList) < 5:
            x = randint(0,len(self.Words)-1)
            if x not in self.picked:
                self.roundList.append(self.Words[x])
                self.def_array.append(x)
                self.picked.append(x)

        shuffle(self.picked)
        self.view.def1.set_text(self.definitions[self.picked[0]])
        self.view.word1.set_label(self.roundList[0])
        self.view.word2.set_label(self.roundList[1])
        self.view.word3.set_label(self.roundList[2])
        self.view.word4.set_label(self.roundList[3])
        self.view.word5.set_label(self.roundList[4])

    #negates the skipLeft decrease if the label is currently next
    #makes a new round while skips are left and increments variables accordingly
    #When it is the end of the level, resets the screen
    def skip_press(self,widget):
        if self.isNext:
            self.skipsLeft += 1
            self.isNext = False
        if self.skipsLeft > 0:
            self.make_round()
            self.skipsLeft = self.skipsLeft - 1
            self.totalScore +=10
            self.view.skipLabel.set_text("Skips left:" + str(self.skipsLeft))
        else:
            self.view.resultLabel.set_text("No Skips Left!")
        if self.nextLevel:
            #puts the widgets back on the screen for the next level
            self.nextLevel = False
            self.view.label.set_text("LEVEL " + str(self.level))
            self.view.word1.show()
            self.view.word2.show()
            self.view.word3.show()
            self.view.word4.show()
            self.view.word5.show()
            self.view.definition.show()
            self.view.def1.show()
            self.generate_level()
    #if def matches word, updates variables accordingly and deletes the word and def from the array
    #when there are less than 5 words left, end the level
    def check_correct(self,widget):
        #checks if number matches the number at int(widget) index
        if self.picked[0] == self.def_array[int(widget)] and self.isNext==False:
            self.view.resultLabel.set_text("CORRECT!")
            self.updateScore(10)
            self.view.skip.set_label("NEXT")
            self.isNext = True
            self.gotPoints = True
            del self.definitions[self.picked[0]]
            del self.Words[self.picked[0]]
        else:
            if self.gotPoints == False:
                self.view.resultLabel.set_text("INCORRECT!")
        #the player answered enough correctly to move on.
        if len(self.definitions) <= 5:
            self.level += 1
            self.totalScore +=10
            self.endLevel()

    #hides the variables to display the results from the level
    def endLevel(self):
        self.view.word1.hide()
        self.view.word2.hide()
        self.view.word3.hide()
        self.view.word4.hide()
        self.view.word5.hide()
        self.view.definition.hide()
        #need the self.level-1 since we already incremented it
        self.view.label.set_text("Level " +str(self.level-1) + " completed. You have scored " + str(self.score) + " out of " + str(self.totalScore) + " points.")
        self.view.def1.hide()
        self.view.resultLabel.set_text("")
        self.view.skip.set_label("Continue")
        self.nextLevel = True

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
    def get_correct(self, level):
        self.Words = self.load_file("Game2-CorrectLevel" + str(level))

    # This function takes in a file name and load all the words from the corresponding file
    def load_level_definitions(self, level):
        self.definitions = self.load_file("CorrectlySpelled - Definitions" + str(level))






    #increates the score when points have no already been awarded
    def updateScore(self, increment):
        self.score += increment
        self.view.scoreLabel.set_text("SCORE: " + str(self.score))


#General Methods
    def addImage(self, widget, event):
        path = "background.jpg"
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
