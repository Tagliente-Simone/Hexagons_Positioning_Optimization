import csv

def create_result_csv(origine_x, origine_y, rotazione):


    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["origine_x", "origine_y", "rotazione"])
        writer.writerow([origine_x, origine_y, rotazione])
