import numpy as np
import time

class Robot:
    def __init__(self):
        self.maxBalls = 10
        self.numBalls = 0
        self.map = np.zeros((self.maxBalls, 2))

    def updateMap(self, points):
        error = 0.1
        if (self.numBalls == 0):
            self.map[self.numBalls] = points[0]
            self.numBalls = 1
        for point in points:
            added = False
            for i,ball in enumerate(self.map[:self.numBalls]):
                if (np.linalg.norm(point - ball) < error):
                    self.map[i] = ball
                    added = True
            if added:
                continue
            self.map[self.numBalls] = point
            self.numBalls += 1

        return
        

    def loop(self):
        hz = 1/10 
        dt = 1.0 / hz

        points = [np.array((2,2)), np.array((10,3)), np.array((2.00001, 2))]
        self.updateMap(points)

        while True:
            start = time.time()
            # print(self.map)
            elapsed = time.time() - start
            if (elapsed < dt):
                time.sleep(dt - elapsed)

if __name__ == "__main__":
    program = Robot()
    program.loop()
