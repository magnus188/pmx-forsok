import pylab as pl
import math
from getworkingpath import *

# Open file 3.txt
filnavn = getworkingpath()+'/data/3.txt'
myFile = open(filnavn,"r").readlines()

#open file gjennomsnitt.csv
filnavn2 = getworkingpath()+'/data/gjennomsnitt.csv'
GjennomsnittFile = pl.loadtxt(filnavn2, float, delimiter=";")
#tar gjennomsnittsverdiene ved 3 volt
gjennomsnitt = GjennomsnittFile[:,1]

#tom liste med måleverdier
y = []
#Fyller y med måleverdier
for element in myFile:
    element.strip("n")
    y.append(float(element))

#tom liste for x-aksen og gjennomsnittverdiene
x = []
Gjennomsnitt_y = []

#Lager liste med lengde til listen med måleverdiene
for i in range(len(y)):
    x.append(float(i))
    Gjennomsnitt_y.append(gjennomsnitt[0])

#Plotter verdiene
pl.title("Målinger ved 3 volt")
pl.xlabel("Måling nr.")
pl.ylabel("Magnetisk feltstyrke (µT)")
pl.scatter(x,y, label = "målinger", color = "red")
pl.plot(x,Gjennomsnitt_y, label = "gjennomsnitt")
pl.legend()
pl.show()