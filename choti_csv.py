import csv
file_path = "./stocks.csv"
fobj = open(file_path)
from datetime import datetime

# print(fobj.read())
reader = csv.reader(fobj)
print("Line no after opening file: " + str(reader.line_num))

# the first line in the header
# first_line = next(reader)
# print("Line number after first next method: " + str(reader.line_num))

# data = [row for row in reader]
data=[]
for row in reader:
    if reader.line_num < 5:
        print("Just read line number : " + str(reader.line_num))
        
    if reader.line_num == 1:
        first_line = row
    else:
        data += row # data = data + row

print("line number at end of file: " + str(reader.line_num))

fobj.close()
print("Printing F Line: \n" + str(first_line))
print(data[0])
    
    
    
#     date_datee = datetime.strptime(row[0], '%m/%d/%Y')
#     open_price = float(row[1])
#     high = float(row[2])
#     low = float(row[3])
#     close = float(row[4])
#     volume = int(row[5])
#     adj_close = float(row[6])

#     data.append([date_datee, open_price, high, low, close, volume, adj_close])
    
# # Compute and return daily stocks csv









