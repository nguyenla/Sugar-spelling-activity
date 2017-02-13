#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os
from GameView import GameView
from Game2View import Game2View
from RootView import RootView
from GameController import GameController
from Game2Controller import Game2Controller
import sys
sys.path.append("python-espeak/")
from HomeView import HomeView
from Speak import Speak
import espeak

class MasterController:
    def __init__(self):
        self.root_view = RootView()

        # Create a game view
        self.view = HomeView(self.root_view.window)
        self.view.button.connect_object("clicked", self.render_game1, "")
<<<<<<< HEAD
        self.view.button2.connect_object("clicked", self.render_game2, "")
=======
        self.view.nextButton.connect_object("clicked", self.render_game2, "")
        self.view.button3.connect_object("clicked", self.render_game3, "")
>>>>>>> 046b9c0a328d9b29f090005900f69f02f998acb6

        self.view.window.connect("delete_event", self.delete_event)
        self.view.window.connect("destroy", self.destroy)
        self.view.vbox.connect('expose-event', self.addImage)

    # Render the first game
    def render_game1(self, button):
        self.root_view.window.remove(self.view.vbox)
        self.view = GameView(self.root_view.window)
        self.controller = GameController(self.view)

    # Render the second game
    def render_game2(self, button):
<<<<<<< HEAD
        self.root_view.window.remove(self.view.vbox)
        self.view = Game2View(self.root_view.window)
        self.controller = Game2Controller(self.view)

=======
        print "render game2"

    def render_game3(self,button):
        self.root_view.window.remove(self.view.vbox)
        self.view = GameView3(self.root_view.window)
        self.controller = GameController3(self.view)
>>>>>>> 046b9c0a328d9b29f090005900f69f02f998acb6

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
    game = MasterController()
    gtk.main()


if __name__ == "__main__": main()
