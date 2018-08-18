import pandas as pd
import re

run = True

def loadexcel(x):#, #y = 'Sheet1'):
    global run
    file= pd.ExcelFile(x)
    names = file.sheet_names
    names = re.sub("'",'', str(names))
    print ("This file contains this tab names:", names )
    while run is True:
        try:
            decision = (input("Choose your tab name? "))
            print ("Your choice is", decision)
            confirm = int(input("This is correct? Please write 1 for yes or 2 for no "))
            if confirm == 1:
                print ("Processing Tab, please wait")
                header = input('Where the headers are located? ')
                final_file = file.parse(sheet_name = decision,header=int(header))
                return final_file
                run = False
            else:
                print ('Choose the right tab!')
        except Exception as e:
            print ("There is an error: ", e)
            print ("Please Try Again! :)")
            continue

def loadcsv(x):
    location = x
    print ('How do you want to split the data, usually is with a comma?')
    sep = input('Write your separator?')
    while run is True:
        try:
            if sep == '':
                sep = ','
                print('The default value is ,')
                header = input('Where the headers are located? ')
                final_file = pd.read_csv(location,sep=sep,header=int(header))
                return  final_file
            else:
                print('The default value is', sep)
                header = input('Where the headers are located? ')
                final_file = pd.read_csv(location,sep=sep,header=int(header))
                return  final_file
        except Exception as e:
            print ("There is an error: ", e)
            print ("Please Try Again! :)")
            continue
