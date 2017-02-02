# @author: Angel Shiwakoti
# @createdOn: 01/31/2017
# This class created the required number of textfields based
# on the number of characters in a given word.

import pygtk
pygtk.require('2.0')
import gtk
import re

class TypeBox(gtk.HBox):
    def __init__(self):

        # Call init method for superclass
        gtk.HBox.__init__(self)

        # Array to hold textFields
        self.textFields = []

        # hBox holds all the textFields
        self.hbox = gtk.HBox(False, 0)
        self.hbox.show()


    # This method creates the necessary amount of textfields
    # based on the number of characters in current word
    def createTextBoxes(self, size):
        self.numBoxes = size
        requiredCount = self.resetContent()
        for index in range(requiredCount):
            self.textFields.append(gtk.Entry(max=1))

        # disable the highlighting of the boxes
        for box in self.textFields:
            box.set_can_focus(False)
        self.showBoxes()


    # This method resets the text for existing textfields.
    # If there are more than required textfields previously
    # created, this method removes them.
    def resetContent(self):
        if (len(self.textFields) == 0):
            return self.numBoxes

        # If we have more text boxes than we need
        elif (len(self.textFields) > self.numBoxes):
            removeCount = len(self.textFields) - self.numBoxes
            for index in range(removeCount):
                self.hbox.remove(self.textFields.pop())

        self.resetTextBox()
        return self.numBoxes - len(self.textFields)


    # This method shows all the existing textfields.
    def showBoxes(self):
        for textField in self.textFields:
            textField.set_size_request(50,30)
            self.hbox.pack_start(textField, True, False, 0)
            textField.set_property("editable", False)
            textField.set_alignment(xalign = 0.5)
            textField.show()

    def addWord(self, word):
        self.resetTextBox()
        for index in range(len(word)):
            self.textFields[index].set_text(word[index])

    # Reset the text of all textbox to ""
    def resetTextBox(self):
        for textField in self.textFields:
            textField.set_text("")

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    typeBox = TypeBox()
    typeBox.main()
