import csv

with open('Data.csv', newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    num = file_data[i][1]
    # I is the line number and 1 is the column number which is the height. 
    # column to row
    new_data.append(float(num))

new_data.sort()
n = len(new_data)
# find the median. 
# if the number of elements is odd, then the median is the middle element.
# if the number of elements is even, then the median is the average of the two middle elements.

if(n % 2 == 0):
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    median = (median1 + median2)/2

else:
    median = float(new_data[n//2])
    
print("median is:", str(median))