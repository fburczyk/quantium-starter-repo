import csv
import os

enter_path = "./data"
exit_path = "./formatted_data.csv"

with open(exit_path, "w", newline="") as output_data:
    writer = csv.writer(output_data)

    writer.writerow(["Sales", "Date", "Region"])

    for filename in os.listdir(enter_path):
        if filename.endswith(".csv"):
            with open(os.path.join(enter_path, filename), "r") as input_data:
                reader = csv.reader(input_data)
                row_index = 0
                for row in reader:
                    if row_index > 0:
                        product = row[0]
                        price = row[1]
                        quantity = row[2]
                        date = row[3]
                        region = row[4]
                        if product == "pink morsel":
                            sales =  float(price[1:]) * int(quantity)

                            output = [sales, date, region]
                            writer.writerow(output)
                    row_index += 1


