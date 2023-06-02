import csv
import os

# This script is used to preproccess the csv file to set seperator to ',' and remove space after comma
# and merge adult.test and adult.data into one file

# Set the path to the csv file
path_adult = os.path.join(os.getcwd(), 'data', 'adult.data')
path_adult_test = os.path.join(os.getcwd(), 'data', 'adult.test')

# Set the path to the output file
path_output = os.path.join(os.getcwd(), 'data', 'adult.csv')

# Open the csv file
with open(path_adult, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = list(reader)

# Open the csv file
with open(path_adult_test, 'r') as f:
    # Skip the . at the end of the file
    reader = csv.reader(f, delimiter=',')
    data_test = list(reader)

# Merge the two files
data.extend(data_test)

# strip the space after comma
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = data[i][j].strip()
        if data[i][j].endswith('.'):
            data[i][j] = data[i][j][:-1]
        

# Write the merged file to the output file
with open(path_output, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Print the number of rows in the output file
print(f'Number of rows in the output file: {len(data)}')
