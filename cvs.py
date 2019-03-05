import csv

new_names = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open ("new_export.csv", "w", encoding="utf-8") as f:
    fields = ["name", "age", "job"] 
    writer = csv.DictWriter(f, fields, delimiter=",")
    writer.writeheader()
    for user in new_names:
        writer.writerow(user)
