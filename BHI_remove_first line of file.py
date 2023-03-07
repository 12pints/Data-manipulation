#this code iterates over a number of file in directory DFJ/test, it removes the first line from each file
# and rewrites the file
#this code works

import os

# Set the directory containing the files to process
directory = 'DFJ/Test'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Only process files with .txt extension (modify as needed)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            # Read the contents of the file
            lines = f.readlines()
        # Remove the first line of the file
        lines.pop(0)
        # Write the updated contents to the same file
        with open(filepath, 'w') as f:
            f.writelines(lines)
