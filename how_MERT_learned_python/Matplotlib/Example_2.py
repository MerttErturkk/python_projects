import matplotlib.pyplot as plt

x_val = list(range(1,1001))
y_val =[x**2 for x in x_val]

plt.scatter(x_val,y_val,c=y_val,cmap=plt.cm.Blues,
            edgecolor="none",s=50) # c stands for color and normally
                                   # a list like[0,0,0.8]


# Set chart title and label axes.
plt.title("Square Number", fontsize =24)
plt.xlabel("Value",fontsize =14)
plt.ylabel("Sqare of Value",fontsize = 14)


# Set the range for each axis.
plt.axis([0,1100,0,1100000])


# Set size of tick labels.
plt.tick_params(axis="both",which="major",labelsize =14)


# Automaticly saves a file and plots the graph.
plt.savefig("squares_plot.png",bbox_inches = "tight" ) 

# bbox_inches creates extra white space around tha plot.
                                                  