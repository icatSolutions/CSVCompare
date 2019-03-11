# Compare Two CSV Files

from os import listdir
from os.path import isdir, join
import pathlib

#decimal precision
precision = 5


def compare(directory, field):
    file_list = [directory+"/"+field+'_original.csv', directory+"/"+field+'.csv']  # List of file names
    output = open(directory+'/'+field+'Output.txt', 'w')
    file1 = []
    file2 = []
    diffFound = 0
    print(directory)
    print(field)
    
    # read file data
    with open(file_list[0]) as f:
        file1 = f.readlines()
    with open(file_list[1]) as f:
        file2 = f.readlines()
#   print("file data read")

    # remove first line from source file
    file1.pop(0);

#   reference matrix
    rowCount = (len(file1) - 1) / 2
    columnCount = (len(file1[0].strip().split(',')[:-1]) - 1) / 2
#   write to file
    output.write("------------------------------------\n" + "Scanner Name: " + directory + "\n------------------------------------\n" + "Field name: " + field + ":\n" + "\nMatrix: " + str(rowCount) + "cm" + " x " + str(columnCount) + "cm\n" +  "Decimal precision: " + str(precision) + " decimals\n\n")

    # iterate through data
    for line in file1:
#        row
#        print(len(file1))
        index = file1.index(line)
        lineValues1 = line.strip().split(',')[:-1]

        # remove first element from row
        lineValues1.pop(0)

        secondFileValues = file2[index].strip().split(',')[:-1]
        for value in lineValues1:
#            column
#            print(len(lineValues1))
            valueIndex = lineValues1.index(value)
            secondValue = secondFileValues[valueIndex]

            # comparison
#            print(index)
#            print(valueIndex)
            if round(float(value.strip()), precision) != round(float(secondValue.strip()), precision):
                diffFound += 1
                output.write("row:"+str(index+1)+", column:"+str(valueIndex+1)+", Original value:"+ value+", Compared value:"+ secondValue+"\n")

#    print("csv files compared")
#    print(str(diffFound) + " difference(s) found!")
    if diffFound == 0:
        output.write("no differences found between files")
                 
current_dir = pathlib.Path(__file__).parent
dirs = [f for f in listdir(current_dir) if isdir(join(current_dir, f))]

#remove directories
#dirs.remove("venv")
dirs.remove(".git")
#dirs.remove(".idea")
for directory in dirs:
    fields = list(map(lambda x: x.split("_")[0], [f for f in listdir(directory) if "original" in join(current_dir, f)]))
    for field in fields:
        compare(directory, field)


# compare("b0")
