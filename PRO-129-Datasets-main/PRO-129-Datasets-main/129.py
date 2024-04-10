import csv 
data = []
with open ("archive_dataset.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data.append(i)

headers = data[0]
planet_Data = data[1:]
# converting planet names to lower case
for i in planet_Data:
    i[2] = i[2].lower()

# sorting planet names 
planet_Data.sort(key=lambda planet_Data: planet_Data[2])
with open ("sorted_archive_dataset.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_Data)

# removing blank lines 
with open ("sorted_archive_dataset.csv") as input, open("sorted_archive_dataset_1.csv", "w", newline='') as output:
    writer = csv.writer(output)
    for i in csv.reader(input):
        if any(field.strip() for field in i):
            writer.writerow(i) 
        