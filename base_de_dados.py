import csv, json

csvfile = open('prod_review.csv', 'rU')
jsonfile = open('testdata.py', 'w')

reader = csv.DictReader(csvfile)

for row in reader:
    json.dump((row['CATGROUP_ID']), jsonfile)
    jsonfile.write(',\n')