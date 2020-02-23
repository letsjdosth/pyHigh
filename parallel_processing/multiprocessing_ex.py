import multiprocessing
import time

class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        self.id = id
    
    def run(self):
        time.sleep(1)
        print("I'm the process with id: {}".format(self.id))

if __name__ == "__main__":
    processes = [Process(0), Process(1), Process(2), Process(3)]
    [p.start() for p in processes]