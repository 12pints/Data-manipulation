#This code iterates over a number of txt files in the  DFJ/Test directory and writes the csv files as .csv files
# maintaining the file name.
#This code works

import os

input_dir = 'DFJ/Test'
output_dir = 'DFJ/Test_csv'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # Construct input and output file paths
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename[:-4] + '.csv')

        # Read the contents of the input file
        with open(input_path, 'r') as f:
            lines = f.readlines()

        # Write the contents of the input file to the output file in CSV format
        with open(output_path, 'w') as f:
            for line in lines:
                fields = line.strip().split()
                csv_line = ','.join(fields) + '\n'
                f.write(csv_line)
