import csv
import requests, datetime, time

basic_url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='
stock_num = '&stockNo=2330'

now = datetime.datetime.now()
current_date = now.strftime("%Y%m%d")

def get_data(date):
    url = basic_url + date + stock_num
    json_data = requests.get(url).json()
    if json_data != None:
        print('success')
        data = json_data['data']
    else:
        print('error in ' + date)
    return data

with open('2330.csv', 'w', newline='') as csvfile:
    fieldnames = ['Date', 'Traded_shares','Turnover','Open','High','Low','Close','Spread','Volume']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    
    current_year = now.year
    current_month = now.month
    day = '01'
    

    #from 2000 to 2017
    count =0
    for y in range(18):
        #12month
        year_data = []
        for x in range(1,13):
            if x >= 10 and y >= 10:
                #EX: 20171001
                data = get_data('20' + str(y) + str(x) + '01')
                year_data.append(data)
                count += 1
            elif x >= 10 and y < 10:
                #EX: 20170101
                data = get_data('200' + str(y) + str(x) + '01')
                year_data.append(data)
                count += 1
            elif x > 0 and x < 10 and y >= 10:
                #EX: 20170101
                data = get_data('20' + str(y) + '0' + str(x) + '01')
                year_data.append(data)
                count += 1
            elif x > 0 and x < 10 and y < 10:
                #EX: 20170101
                data = get_data('200' + str(y) + '0' + str(x) + '01')
                year_data.append(data)
                count += 1
            #wait 30sec to avoid be blocked ip
            time.sleep(30)
        for i in year_data:
            for y in i:
                writer.writerow(y)
                print(y)
    print('total {} months'.format(count))

    
