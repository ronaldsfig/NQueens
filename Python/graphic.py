import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Line3DCollection


class Graphic:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.points = []
        self.lines = []
        self.finished = False
        self.current_frame = 0
        self.num_actions = 0

    def add_point(self, x, y, z):
        self.points.append((x, y, z))

    def update(self, action):
        x, y, z = action
        self.add_point(x, y, z)
        self.current_frame += 1
        if self.current_frame >= self.num_actions:
            self.finished = True

    def animate(self, action):
        self.update(action)
        if self.finished:
            xs, ys, zs = zip(*self.points)
            self.ax.scatter(xs, ys, zs, c=np.arange(len(xs)),
                            cmap='YlOrRd_r', s=100, alpha=0.7)
            segments = [[(xs[i], ys[i], zs[i]), (xs[i+1], ys[i+1], zs[i+1])]
                        for i in range(len(xs)-1)]
            lc = Line3DCollection(segments, cmap='YlOrRd_r', alpha=0.9)
            lc.set_array(np.arange(len(xs)))
            self.ax.add_collection3d(lc)
            plt.show()
        else:
            xs, ys, zs = zip(*self.points)
            self.ax.clear()
            self.ax.scatter(xs, ys, zs, c=np.arange(len(xs)),
                            cmap='YlOrRd_r', s=100, alpha=0.9)
            self.ax.set_xlim(min(xs), max(xs))
            self.ax.set_ylim(min(ys), max(ys))
            self.ax.set_zlim(min(zs), max(zs))
            self.ax.set_xlabel('x tabuleiro')
            self.ax.set_ylabel('y tabuleiro')
            self.ax.set_zlabel('Afinidade (fit)')
            if self.current_frame > 1:
                segments = [[(xs[i], ys[i], zs[i]), (xs[i+1], ys[i+1], zs[i+1])] for i in range(len(xs)-1)]
                lc = Line3DCollection(segments, cmap='YlOrRd_r', alpha=0.9)
                lc.set_array(np.arange(len(xs)-1))
                self.ax.add_collection3d(lc)
            plt.pause(0.5)


# Test the class
graphic = Graphic()
actions = [
    (6, 2, 16),
    (1, 6, 19),
    (5, 4, 13),
    (2, 6, 11),
    (2, 2, 12),
    (3, 4, 9),
    (3, 2, 8),
    (3, 3, 9),
    (4, 4, 5),
    (4, 3, 3),
    (4, 2, 1),
    (4, 1, 0),
]

graphic.num_actions = len(actions)

for action in actions:
    graphic.animate(action)
