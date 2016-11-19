import time

#
# timerTools
#
class Timer:
    def __init__(self, name="Default"):
        self.name = name
        self.tic()

    def tic(self):
        self.time = time.time()

    def toc(self):
        print('Time spent from ', self.name, ' tic : ', time.time() - self.time)
