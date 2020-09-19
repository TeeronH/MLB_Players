# Find the 75th percentile of MLB players heights

import csv
import statistics
import collections

height = []
with open ('MLB_Players.csv') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)
	for row in reader:
		height.append(int(row[3]))

	height_percentiles = statistics.quantiles(height, n = 4, method = 'exclusive')
	print(height_percentiles[-1])

	d = collections.Counter(height)
	print(d)

	sorted_keys = sorted(d)
	for key in sorted_keys:
		value = d[key]
		string = '*' * value
		print(str(key) + ':' + string)
