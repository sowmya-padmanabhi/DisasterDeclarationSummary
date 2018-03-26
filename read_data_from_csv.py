import csv 

with open('DisasterDeclarationsSummaries.csv', 'r', newline='') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for row in csv_reader:
		print(row)
