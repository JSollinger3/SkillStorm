import csv

with open("Expenditure.csv", "r") as file:
    exp_reader = csv.reader(file)   # Get contents of csv file
    next(exp_reader)    # Skip headings
    expenditures = list(exp_reader)
    exp_dict = dict()

DEPARTMENTS = set()
for row in expenditures:
    if row[0] != '':
        DEPARTMENTS.add(row[0])
    else:
        DEPARTMENTS.add("Unspecified")
DEPARTMENTS = sorted(DEPARTMENTS)

for key in DEPARTMENTS:
    exp_dict[key] = 0

for row in expenditures:
    for key in exp_dict:
        to_add = 0
        if row[0] == key:
            if row[3] != '':
                to_add = int(row[3])
            exp_dict[key] += to_add

for exp in exp_dict.items():
    print(exp[0] + "\'s spending: $" + str(exp[1]) + ".00")