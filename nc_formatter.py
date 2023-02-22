import sys
from datetime import date

separator = ','
numberOfColumn = 17
inputFileName = sys.argv[1]
outputFileName = "extraction_nc_" + date.today().strftime("%d-%m-%Y") + ".csv"

with open(inputFileName, "r") as reader:
    with open(outputFileName, "w") as output:
        i = 0
        lines = reader.read().splitlines()
        while(i < len(lines)):
            splitLine = lines[i].split(separator)
            newLine = lines[i]
            i +=1
            while (len(splitLine) < numberOfColumn):
                nextSplitLine = lines[i].split(separator)
                splitLine = splitLine + nextSplitLine
                newLine = newLine + ' ' + lines[i]
                i +=1
            output.write(newLine + '\n')
                

