from django.test import TestCase
# Create your tests here.
import csv

datas = csv.reader(open('1A.csv'), delimiter=',', quotechar='"')
for data in datas:

    print(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}")