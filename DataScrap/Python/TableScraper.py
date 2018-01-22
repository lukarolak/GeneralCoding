#Checks for changes within website tables
import pandas as pd
def ClearData():
    print("Clearing data")
    f = open("test.txt", "w")
    f.write("")
    f.close()
while(1):
    print("-------------------------------------------------")
    UserInput = input()
    if(UserInput == 'clear'):
        ClearData()
    if(UserInput == 'check'):
        f = open("test.txt", "r")
        DataList = f.readlines()
        tables = pd.read_html("your website here")
        #print(tables)
        #writes new data to file
        f = open("test.txt","a")
        for i in range(0,len(tables[0].Name)):
            try:
                DataList.index(tables[0].Name[i]+'\n')
            except ValueError:
                print("not found, appending data to file")
                print("Data:" + tables[0].Name[i] + " ||| " +tables[0].Price[i])
                f.write(tables[0].Name[i]+"\n")
                f.write(tables[0].Price[i]+"\n")
            else:
                DataFile = DataList[DataList.index(tables[0].Name[i]+'\n')+1].replace("$","")
                DataFile = float(DataFile)
                DataWeb = tables[0].Price[i].replace("$","")
                DataWeb = float(DataWeb)
                print(tables[0].Name[i]+" "+str((DataFile-DataWeb)/DataFile*100)+"%")
        f.close()
    if(UserInput == 'close'):
        break
