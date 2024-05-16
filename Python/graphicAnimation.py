import matplotlib.pyplot as plt


class GraphicAnimation:
    def __init__(self, title, x_title, y_title, color):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title(title)
        self.ax.set_xlabel(x_title)
        self.ax.set_ylabel(y_title)
        self.line, = self.ax.plot([], [], color)
        self.x_data = []
        self.y_data = []

    def updateGraphic(self, x, y):
        self.x_data.append(x)
        self.y_data.append(y)
        self.line.set_data(self.x_data, self.y_data)

        self.ax.relim()
        self.ax.autoscale_view()

        self.fig.canvas.draw()
        plt.pause(0.01)
