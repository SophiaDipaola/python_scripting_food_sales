#read only

def read_only():
    # a method that only reads the file
    try:
        file1 = open('data.txt','r')
        text = file1.read()
        print(text)

        file1.close() #the reason for closing this way is because it will remain open in memory if you dont close it
    except FileNotFoundError:
        text = None
        print(text)

def write_only():
    #a method that writes to a file
    #if file exists, it will be overwritten 
    #if it doesnt exist, it will be created
    file2  = open('more_data.txt','w')
    file2.write('tomatoes')
    file2.close()

#to close a file
# with open('data.txt') as f:
#     txt = f.read()
#     print(txt)


def read_food_sales(): 
    all_dates = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        print(data)

        for food_sale in data:
            split_food_sale = food_sale.split(',')
            

            order_date = split_food_sale[0]
            print(order_date)

            all_dates.append(order_date) 
    print(all_dates)
    
    with open ('dates.txt', 'w') as f:
        for date in all_dates:
            f.write(date)
            f.write('/n')
def append_text():
    #append data on an existing file
    with open('dates.txt', 'a') as f:
        f.write('3/17/2021')
        print('done')

def read_city():
    all_cities = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        print(data)

        for read_cities in data:
            split_read_cities = read_cities.split(',')
            

            my_city = split_read_cities[0]
            print(my_city)

            all_cities.append(my_city) 
    print(all_cities)
    
    with open ('cities.txt', 'w') as f:
        for city in all_cities:
            f.write(city)
            f.write('/n')
def append_text():
    #append data on an existing file
    with open('cities.txt', 'a') as f:
        f.write('Oakland')
        print('done')
 
if __name__ == '__main__':
    #read_only()
    # write_only()
    # read_food_sales()
    read_city()