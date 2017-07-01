import csv
with open("breastCancerData.csv", 'r') as f:
    reader = csv.DictReader(f)
    for i, line in enumerate(reader):
        print 'line[{}] = {}'.format(i, line['diagnosis'])
