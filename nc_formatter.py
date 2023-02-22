import sys
from datetime import date

separator = ','
beginParsing = False
numberOfColumn = 17
outputFileName = "extraction_nc_" + date.today().strftime("%d-%m-%Y") + ".csv"

try:
    inputFileName = sys.argv[1]
except IndexError:
    print("You did not specify a file")
    sys.exit(1)

with open(inputFileName, "r") as reader:
    with open(outputFileName, "w") as output:
        i = 0
        lines = reader.read().splitlines()
        # Specify separator for excel
        output.write("sep=," + '\n')

        while (i < len(lines)):
            splitLine = lines[i].split(separator)
            newLine = lines[i]
            i += 1

            if (splitLine[0] == "# Accession"):
                beginParsing = True

            if (not beginParsing):
                i += 1
                continue

            # Concat line with previous when shorter (ex multiple Dr)
            while (len(splitLine) < numberOfColumn):
                nextSplitLine = lines[i].split(separator)
                splitLine = splitLine + nextSplitLine
                newLine = newLine + ' ' + lines[i]
                i += 1
            output.write(newLine + '\n')
