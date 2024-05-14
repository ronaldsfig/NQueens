import matplotlib.pyplot as plt
import numpy as np

class TemperatureAnimation:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Temperatura ao Longo do Tempo')
        self.ax.set_xlabel('Tempo')
        self.ax.set_ylabel('Temperatura')
        self.line, = self.ax.plot([], [], 'ro-')  # 'ro-' for red circle markers and solid line
        self.x_data = []
        self.y_data = []

    def update_graph(self, x, y):
        self.x_data.append(x)
        self.y_data.append(y)
        self.line.set_data(self.x_data, self.y_data)

        self.ax.relim()  # Recompute the data limits
        self.ax.autoscale_view()  # Rescale the view to fit the data

        self.fig.canvas.draw()
        plt.pause(0.5)  # Adjust the pause time as needed


def main():
    # Example of data being generated in real-time
    animation = TemperatureAnimation()

    # Simulating a stream of data points
    time_points = np.arange(0, 10, 1)  # Time from 0 to 9
    temperature_points = np.random.randint(15, 25, size=10)  # Random temperatures between 15 and 25

    for t, temp in zip(time_points, temperature_points):
        animation.update_graph(t, temp)

    plt.show()

if __name__ == "__main__":
    main()
