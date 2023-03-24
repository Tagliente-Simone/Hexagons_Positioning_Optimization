import csv
import numpy as np
import CalculateDimension as calc
import pandas as pd

def create_csv_result(x, y, orientation):
    with open('./resources/result.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([x, y, orientation])

# Open the CSV file
with open('./resources/combinazioni.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Iterate over each row in the CSV file

    column_dest = []
    column_compo = []

    for row in reader:
        column_dest.append(row[1])
        column_compo.append(row[3])
    

input = np.array([column_dest, column_compo], dtype = 'str')
input = np.transpose(input)
input = np.delete(input, 0, 0)
index = 2

## Main Function calls
# Iterate over each row in the CSV file
for rows in input:
    rows_array = [float(i) for i in rows[1].split('-')]
    if(len(rows_array) % 2 == 1):
        n_rows = len(rows_array)
        radius = float(rows[0])
        radius = radius / 20

        #Call the function to calculate the dimension of the hexagon
        calc.Calculate(radius, n_rows, rows_array, index)

    else:
        print("Error: the number of rows must be odd")
        create_csv_result(000, 000, "error")
    index += 1

# Merge the two CSV files
combinations = pd.read_csv('./resources/combinazioni.csv', header=None)
results = pd.read_csv('./resources/result.csv', header=None)
merged = pd.concat([combinations, results], axis=1)
merged.to_csv('./resources/merged.csv', index=False)

print("Done! You can find the result in the merged.csv file and the images in the images folder.")



