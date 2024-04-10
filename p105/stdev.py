import math

data = [60,61,65,63,98,99,90,95,91,96]

sum = 0

for i in range(len(data)):
    sum+=data[i]

mean = sum/len(data)

deviation_sum = 0
for i in range(len(data)):
    deviation_sum+=(data[i] - mean)**2
    
psd = math.sqrt((deviation_sum)/len(data))

ssd = math.sqrt((deviation_sum)/len(data) - 1)

print("Standard deviation", psd)