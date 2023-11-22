import csv
import random
import time

Hour = 19
Vehicles = 2653
fieldnames = ['Hour', 'Vehicles']

with open('Vehicle.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('Vehicle.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "Hour": Hour,
            "Vehicles": Vehicles
        }
        csv_writer.writerow(info)
        print("----------", "100%", "----------", Hour, Vehicles, "----------" )
        Hour += 1
        Vehicles = Vehicles + random.randint(-50, 50)
    time.sleep(1)