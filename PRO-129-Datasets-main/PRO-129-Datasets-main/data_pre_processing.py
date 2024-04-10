import csv 
dataset1 = []
dataset2 = []

with open ("final.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset1.append(i)

with open ("sorted_archive_dataset_1.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset2.append(i)

headers = dataset1[0]
planet_Data = dataset1[1:]

headers_1 = dataset2[0]
planet_Data_1 = dataset2[1:]

main_header = headers + headers_1
main_planet_data = []

for index, i in enumerate(planet_Data):
    main_planet_data.append(planet_Data[index] + planet_Data_1[index])

with open("merged_data_set.csv", "a+") as f:
    csv_Writer = csv.writer(f)
    csv_Writer.writerow(main_header)
    csv_Writer.writerows(main_planet_data)
