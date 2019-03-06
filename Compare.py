# Compare Two CSV Files

file_list = ['input1.csv', 'input2.csv']  # List of file names
output = open('Output.txt', 'w')
file1 = []
file2 = []
diffFound = 0

# read file data
with open(file_list[0]) as f:
    file1 = f.readlines()
with open(file_list[1]) as f:
    file2 = f.readlines()
print("file data read")

# iterate through data
for line in file1:
    index = file1.index(line)
    lineValues1 = line.strip().split(',')[:-1]
    secondFileValues = file2[index].strip().split(',')[:-1]
    for value in lineValues1:
        valueIndex = lineValues1.index(value)
        secondValue = secondFileValues[valueIndex]
        
        #comparison
        if value != secondValue:
            diffFound+=1
            output.write("row:"+str(index+1)+", column:"+str(valueIndex+1)+", first value:"+ value+", second value:"+ secondValue+"\n")

print("csv files compared")
print(str(diffFound) + " difference(s) found!")




