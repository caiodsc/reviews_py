import csv, json

csvfile = open('prod_review.csv', 'rU')
jsonfile = open('testdata_cat2.py', 'w')

reader = csv.DictReader(csvfile)

for row in reader:
    c = int(row['CATGROUP_ID'])
    if True:#12030 <= c and c <= 12068: #Celulares
        json.dump((row['NAME'], row['USERS_ID'], row['REVIEWRATE']), jsonfile)
        jsonfile.write(',\n')