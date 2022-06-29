
import csv
from datetime import datetime

path = "stocks.csv"
f = open(path, newline = '')
reader = csv.reader(f) 

# the first line in the header
header = next(reader)
data = []
for row in reader:
    # row = [ Date, Open, High, Low, Close, Adj. Close ]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

    # Compute and return daily stocks csv 

    returns_path = "./google_returns.csv"
    file = open(returns_path, 'w')
    writer = csv.writer(f)
    write.writerow(["Date", "Return"])

    for i in range(len(data) - 1):
        todays_row = data[i]
        todays_dates = todays_row[0]
        todays_price = todays_row[-1]
        yesterdays_row = dats[i+1]
        yesterdays_price = yesterdays_row[-1]
        daily_return = (todays_price - yesterdays_price) / yesterdays_price
        writer.writerow([todays_dates, daily_return])