import csv
import numpy as np
import CalculateDimension as calc
import ResultPrinter as rp

# Open the CSV file
with open('combinazioni.csv', 'r') as file:
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

def create_csv_result(x, y, orientation):
    with open('result.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([x, y, orientation])

index = 2

for rows in input:
    rows_array = [float(i) for i in rows[1].split('-')]
    if(len(rows_array) % 2 == 1):
        n_rows = len(rows_array)
        radius = float(rows[0])
        radius = radius / 20
        calc.Calculate(radius, n_rows, rows_array, index)
    else:
        print("Error: the number of rows must be odd")
        create_csv_result(000, 000, "error")
    index += 1


print("Done! You can find the result in the result.csv file and the images in the images folder.")


