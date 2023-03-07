#this code iterates over a number of file in the /dfj/files_csv, it takes the SECOND column in that file and checks
#if the value is 0 , if it is it accumulates the count of zeros by 1, until it reaches the end of the column,
#skips to next file if an empty line is found and writes the result, together with the source file in output_file
#it will also skip the line if the FIRST line contains aiether "Te" or "Po"
#this code works

import os

# Set the directory containing the input files
input_dir = "dfj/files_csv"

# Set the name and path of the output file
output_file = "dfj/CBD inactive ports summary V2"

# Initialize a dictionary to keep track of the count of zeros for each file
zeros_counts = {}

# Loop over all the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):  # Assumes all input files are .csv files
        zeros = 0
        with open(os.path.join(input_dir, filename)) as f:
            for line in f:
                line = line.strip()
                if not line:
                    break  # Skip to next file if empty line is found
                cols = line.split(",")
                if "Po" in cols[0] or "Te" in cols[0]:
                    continue  # Skip if "Po" or "Te" in first column
                if cols[1] == "0":
                    zeros += 1
        # Add the count of zeros for this file to the dictionary
        zeros_counts[filename] = zeros

# Write the dictionary to the output file
with open(output_file, "w") as out:
    out.write("Input file,Number of zeros\n")
    for filename, zeros in zeros_counts.items():
        out.write(f"{filename},{zeros}\n")
    # Write the total count of zeros to the output file
    total_zeros = sum(zeros_counts.values())
    out.write(f"Total zeros,{total_zeros}\n")
