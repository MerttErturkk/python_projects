import matplotlib.pyplot as plt

from random_walk import RandomWalk
""" Keep making new walks, as log as the program is active."""

while True:
    #Make a random walk,plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Set the size of the plotting window.(THE RESOLUTION OF PLOT)
    plt.figure(dpi = 128, figsize=(10,6)) 
    #(default dpi is 1=80pixel plot is 800x480 in that case)
    
    #Plot the points and show the plot.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values ,c =point_numbers,
                cmap =plt.cm.Blues,edgecolor ="none", s=1)
    
    # Emphasize the first and last points.
    plt.scatter(0,0,c="green",edgecolors="none",s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c="red",edgecolors ="none",
                s=100)
    
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    keep_running = input("Make another walk?(y/n):")
    if keep_running == "n":
        break
