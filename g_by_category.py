import csv, json

csvfile = open('prod_review.csv', 'rU')
jsonfile = open('testdata_cat.py', 'w')

reader = csv.DictReader(csvfile)

for row in reader:
    c = int(row['CATGROUP_ID'])
    if 12497 <= c and c <= 12508: #Celulares
        json.dump((row['NAME'], row['USERS_ID'], row['REVIEWRATE']), jsonfile)
        jsonfile.write(',\n')