import pylab as pl
import math
from getworkingpath import *




utgangspunkt_3volt = 1500
x = []
y = []
for i in range(1,4):
    x.append(3*i)
    y.append(utgangspunkt_3volt*i)


pl.plot(x,y)


# Add title and labels
pl.title("Plotting av modell")
pl.xlabel('Spenning (V)')
pl.ylabel('Magnetfeltstyrke (µT)')
pl.legend()
# Show plot
pl.show()