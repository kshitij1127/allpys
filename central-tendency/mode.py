import csv
from collections import Counter

with open("Data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    # converts the file data to a list

# remove the first line, titles
file_data.pop(0)
# initialize a new list
new_data = []

# loop through the file data and convert each element to a float
for i in range(len(file_data)):
    num = file_data[i][1]
    # I is the line number and 1 is the column number which is the height. 
    # column to row
    # append the data to the new list. 
    new_data.append(float(num))

# find the mode. 
data = Counter(new_data)
# data is a dictionary.
# data[key] is the number of times the key appears in the list.
mode_data = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0,
}

# using a for loop to find the mode. 
for height, occurance in data.items():
    if(50 < float(height) < 60):
        # example: 55
        mode_data["50-60"] += occurance
    elif(60 < float(height) < 70):
        # example: 65
        mode_data["60-70"] += occurance
    elif(70 < float(height) < 80):
        # example: 75
        mode_data["70-80"] += occurance

mode_range, mode_occurance = 0,0
for range, occurance in mode_data.items():
    if(occurance > mode_occurance):
        mode_range, mode_occurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance

mode = float((mode_range)[0] + ((mode_range)[1])/2)
print("mode is:", str(mode))