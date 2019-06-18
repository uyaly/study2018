# coding:utf-8
import csv
rows_str = ''
with open("test.csv", "rt", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, rows in enumerate(reader):
        if i != 0:
            rows = rows[0] + ';'
            rows_str += rows
            if i % 51 == 0:
                with open('test1.csv', 'a') as f:
                 f.write(rows_str + '\n')
                rows_str = ''
