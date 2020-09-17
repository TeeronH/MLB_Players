# Find the 75th percentile of MLB players heights

import csv

height = []
with open ('MLB_Players.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		height.append(row[0])
print(height)