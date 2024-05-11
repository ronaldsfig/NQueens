import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class GraphAnimation:
    def __init__(self, xlim=(-10, 10), ylim=(-10, 10)):
        self.fig, self.ax = plt.subplots()
        self.points, = self.ax.plot([], [], 'bo')
        self.xlim = xlim
        self.ylim = ylim
        self.ax.set_xlim(*xlim)
        self.ax.set_ylim(*ylim)
        self.points.set_data([], [])
        self.frames = []

    def update(self, frame):
        if len(frame) == self.total_frames:
            self.ani.event_source.stop()
        x, y = zip(*frame)
        self.points.set_data(x, y)
        return self.points,

    def animate(self):
        self.total_frames = len(self.frames)
        self.ani = FuncAnimation(
            self.fig, self.update, frames=self.frames, interval=200, blit=True)
        plt.show()


def main():
    # Pontos a serem adicionados à animação
    points_list = [[(1, 2)], [(1, 2), (3, 4)], [(1, 2), (3, 4), (5, 6)]]

    graph_anim = GraphAnimation()
    for points in points_list:
        graph_anim.frames.append(points)
    graph_anim.animate()


if __name__ == "__main__":
    main()
