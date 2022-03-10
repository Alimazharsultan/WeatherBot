import csv
with open('brv_1_1 Mod (1).csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)