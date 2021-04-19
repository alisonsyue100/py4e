
import datetime
import csv



header=("Idx| Name | Temperature | Unit | Date")

class Record:
    def __init__(self, Idx: int, Name: str, Temperature: float, Unit: str, Date: str):
        self.Idx = Idx 
        self.Name = Name
        self.Temperature = Temperature
        self.Unit = Unit
        self.Date = Date
records = []



#輸入檔案名稱
def key_in_filename():
    global file_name
    file_name=input("please enter filename:")



#reveal_file
def reveal_file():
    with open(file_name,"r",newline="")as csvfile:
           rows=csv.reader(csvfile)
           print(header)
           for row in rows:
               print(row)

        

#read_file
def read_file():
    data=open(file_name)
    print(header)
    for row in data:
        records.append(Record(int(data[0]), data[1], float(data[2]), data[3], data[4]))
        print(row)
        
        
       

#新增
def add_data():
    record=Record("1",input("please enter name:"),input("please enter temperature:"),input("please enter unit:"),datetime.date.today())
    print(record.Idx,"|",record.Name,"|",record.Temperature,"|",record.Unit,"|",record.Date)
    
    

    

def print_all_data():
    print("idx  | name	| temperature 	|   Unit	| date")
    for record in records:
        print(record.id, "  |   ", record.name, "   |   ", record.temperature, "    |  ", record.unit, "    |  ", record.date)


        
    
    

    

        
while True:
    print("1.Read records from file\n"
          "2.Add a record\n"
          "3.Remove a record\n"
          "4.Save records to a file\n"
          "5.Search by name from records\n"
          "6.Print all records\n"
          "7.Exit")
    option=int(input("Enter the option:"))

    if option==1:
        
        key_in_filename()
        reveal_file()
    
    
                
    if option==2:
        
        add_data()

        
        
    if option==3:
        pass
    if option==4:
        pass
    if option==5:
        pass
    if option==6:
        
        print_all_data()
        
    if option==7:
        print("-----\nExit\n-----")
        break
    

