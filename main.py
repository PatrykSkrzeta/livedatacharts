import random 
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('Vehicle.csv')
    x_vals = data['Hour']
    y_vals = data['Vehicles']
    plt.title('Vehicles driven per hour')
    plt.cla()
    plt.plot(x_vals, y_vals)
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000, frames=500)


plt.tight_layout()
plt.show()