from login.models import User
import csv

datas = csv.reader(open('../1B.csv'), delimiter=',', quotechar='"')
for data in datas:
    user = User(name=data[1], password=data[2], email=data[3], c_name=data[0])
    user.save()
    print(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}")