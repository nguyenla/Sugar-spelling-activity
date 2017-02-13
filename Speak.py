# @author: Angel Shiwakoti
# @createdOn: 02/06/2017
# This class uses threading to spell the word
# using Espeak Library. It prevents the UI Blocking
# while Espeak is spelling a word.

import threading
import gobject
import os
import espeak

gobject.threads_init()

class Speak(threading.Thread):
    def __init__(self, word):
        super(Speak, self).__init__()
        self._stop = threading.Event()
        self.word = word
        self.es = espeak.ESpeak(voice="en+f1", speed = 230)

    def stop(self):
        self._stop.set()

    def run(self):
        self.es.say(self.word)
        # os.system("espeak '{}'".format(self.word))
