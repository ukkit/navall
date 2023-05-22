
# STEPS
# Step1: Download the txt file - maintain line breaks and page breakes
# Step 2: remove all empty lines
# Step 3: convert text to csv
# Step 4: Add Scheme Type & Fund Family in CSV
# find lines with only 1 entry - that will be fund family
# find lines with 8 comma seperated values:
# Scheme Type, Fund Family, Scheme Code, ISIN Div Payout/ISIN Growth, ISIN Div Reinvestment, Scheme Name, Net Asset Value, Date


import wget
import pandas as pd
import csv
import os
import time

# Step 1
url = "https://www.amfiindia.com/spages/NAVAll.txt"
wget.download(url, "navall.txt")

# Step 2
with open('navall.txt') as reader, open('navall.txt', 'r+') as writer:
  for line in reader:
    if line.strip():
      writer.write(line)
  writer.truncate()
print("\nStep 2 done")

# Step 3
account = pd.read_csv("navall.txt", delimiter = ';')
account.to_csv('navall.csv', index = None)
csv_file = pd.read_csv("navall.csv")
# print(csv_file['ISIN Div Payout/ ISIN Growth'])
print("Step 3 done")

exportFileName='out/'+str(time.time())+'.csv'

#Step 4
def generateCSV(csv_file):

    header = ['Scheme Type', 'Fund Family', 'Scheme Code', 'ISIN Div Payout/ISIN Growth', 'ISIN Div Reinvestment', 'Scheme Name', 'Net Asset Value', 'Date']

    line_array = []
    writeX = csv.writer(open(exportFileName, 'w'))
    writeX.writerow(header)

    first = 0
    second = 0
    with open("navall.csv", "r") as f:
        next(f)

        for line in f:
            line_array = []
            # print(line)
            spill = line.split(',')
            #print(spill[1])
            if not spill[1]:
                #print(spill[0])
                if first == 0 and second == 0:
                    fund_family = spill[0]
                    second = 1
                else:
                    scheme_type = fund_family
                    fund_family = spill[0]
                    first = 0
            else:
                line_array = [scheme_type, fund_family]
                for text in spill:
                    #print(text)
                    text = text.strip()
                    text = text.strip('\n')

                    line_array.append(text)
                second = 0

            if line_array:
                writeX.writerows([line_array])

    os.remove('navall.txt')
    os.remove('navall.csv')
    return

generateCSV(csv_file)
print("Step 4 done")
print(exportFileName+" generated")
