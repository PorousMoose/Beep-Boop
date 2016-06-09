import threading
from random import random
from time import sleep as wait

class Beeper(threading.Thread):
    def __init__(self,message):
        threading.Thread.__init__(self)
        self.message=message
        
    def run(self):
        while(True):
            wait(5*random())
            print(self.message)
            
class Booper(Beeper):
    def __init__(self,message):
        super().__init__(message)

if __name__ == "__main__":
    a=Beeper('beep')
    b=Booper('boop')
    
    a.start()
    b.start()

    a.run()
    b.run()