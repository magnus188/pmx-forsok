import pylab as pl

# List of pathnames
fileNames = ['data/3v.txt', 'data/4,5v.txt', 'data/6v.txt']

# Max length of datapoints in files to be read
maxLength = 24

# Iterate through filepaths
for path in fileNames:
    # Load textfile
    datas = pl.loadtxt(path, int)
    # Remova datapoints which are 0
    fixedData = datas[(-0.1 > datas) | (datas > 0.1)]
    # Calculte average score
    average = sum(fixedData[:maxLength-1])/len(fixedData[:maxLength-1])

    # Write average to new textfile 'gjennomsnitt.txt'
    with open("data/gjennomsnitt.csv", "a") as myfile:
        myfile.write(path.split('/')[1].split('.')[0]+ '; ' + str(round(average, 3)) + '\n')