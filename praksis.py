import pylab as pl
import math
from getworkingpath import *



#open file gjennomsnitt.csv
filnavn2 = getworkingpath()+'/data/gjennomsnitt.csv'
GjennomsnittFile = pl.loadtxt(filnavn2, float, delimiter=";")
#tar gjennomsnittsverdiene ved 3 volt
gjennomsnitt = GjennomsnittFile[:,1]

volt = GjennomsnittFile[:,0]
print(volt)

pl.plot(volt, gjennomsnitt)
pl.scatter(volt,gjennomsnitt, color = "red")


# Add title and labels
pl.title("Plotting av gjennomsnittsverdiene")
pl.xlabel('Spenning (V)')
pl.ylabel('Magnetfeltstyrke (µT)')
pl.legend()
# Show plot
pl.show()