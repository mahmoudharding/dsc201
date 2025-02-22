# os module for interacting with the operating system (e.g., reading files, handling paths)
# pandas for working with tabular data and crea
import os
import pandas as pd

# Define the folder containing the extracted name files
extract_folder = "data/names"

# Define the output file where the combined dataset will be saved
output_csv = "data/baby_names.csv"

# Initialize an empty list to store the file names that match the criteria
txt_files = []

# Iterate through the files in the specified folder
for f in os.listdir(extract_folder):

    # Check if the file starts with 'yob' (e.g., 'yob1880.txt') and ends with '.txt'
    if f.startswith("yob") and f.endswith(".txt"):

        # Add the matching file to the list
        txt_files.append(f)  

# Initialize an empty list to store the processed data
data = []

# Iterate through each selected text file
for tf in txt_files:
    
    # Construct the full file path
    file_path = os.path.join(extract_folder, tf)
    
    # Extract the year from the file name (e.g., 'yob1880.txt' → 1880)
    year = int(tf[3:7])
    
    # Open the file and read its contents
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:

            # Split each line by commas into a list of values (name, sex, count)
            columns = line.strip().split(',')
            
            # Prepend the year to the extracted data and append to the list
            data.append([year] + columns)

# Convert the collected data into a pandas dataframe
df = pd.DataFrame(data, columns=["year", "name", "sex", "count"])

# Save the dataframe to a csv file without the index column
df.to_csv(output_csv, index=False)

# Print confirmation message with the output file path
print(f"Combined all name files into: {output_csv}")