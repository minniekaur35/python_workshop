import csv 
import datetime


birth = datetime.date(1998, 12, 31)
print(birth)

# get date from a string

stringDate =  "4-12-2022"
isoVar = "2022-06-04"
format = "%m-%d-%Y"
sd = datetime.datetime.strptime(stringDate, format)
# sd = datetime.date.fromisoformat(datetime.date.isoformat(isoVar))
print(sd.date())



# path = "stocks.csv"
# f = open(path)

# reader = csv.reader(f)
# kinkyHeader = next(reader)

# print(kinkyHeader)

# storingData=[]

# for row in reader:
#     # if reader.line_num < 10:
#         # print(row)
#         # row = [ Date, Open, High, Low, Close, Adj. Close ]
#     date_date = datetime.strptime(row[0])
#     storingData += [row]
   



