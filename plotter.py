import pylab as pl
import math
from getworkingpath import *

# Open file
filnavn = getworkingpath()+'/data/gjennomsnitt.csv'
myFile = pl.loadtxt(filnavn, float, delimiter=";")

# Read file
voltage = myFile[:,0]
magnetic_force = myFile[:,1]*10**-6

# Constants
RADIUS = 1
resistance = 0.0004 # Measured value

# Calculate model
model = [(4*math.pi*(10**-7)*n)/(2*math.pi*RADIUS*resistance) for n in voltage]

# Plot values
pl.plot(voltage, magnetic_force, label="Snitt målte verdier")

# Plot model
pl.plot(voltage, model, label="Model")

# Add title and labels
pl.title("Magnetisk styrke")
pl.xlabel('Spenning (V)')
pl.ylabel('Magnetfeltstyrke (T)')
pl.legend()

# Show plot
pl.show()


