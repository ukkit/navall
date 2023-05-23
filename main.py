
# VERSION 0.2
#
# STEPS
# Step1: Download the txt file - maintain line breaks and page breakes
# Step 2: remove all empty lines
# Step 3: convert text to csv
# Step 4: Add Scheme Type & Fund Family in CSV
#   find lines with only 1 entry - that will be fund family
#   find lines with 8 comma seperated values:
#   Scheme Type, Fund Family, Scheme Code, ISIN Div Payout/ISIN Growth, ISIN Div Reinvestment, Scheme Name, Net Asset Value, Date
# Step 6 convert csv to INSERT statement


import wget
import pandas as pd
import csv
import os
import time
from datetime import datetime

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

# datime =  str(time.time())
datime=str(datetime.now().strftime('%Y%m%d%H%M%S'))
tableName = datime
csvFileName='out/'+datime+'.csv'
sqlFileName='out/'+datime+'.sql'

#Step 4
def generateCSV(csv_file):

    header = ['Scheme Type', 'Fund Family', 'Scheme Code', 'ISIN Div Payout/ISIN Growth', 'ISIN Div Reinvestment', 'Scheme Name', 'Net Asset Value', 'Date']

    line_array = []
    writeX = csv.writer(open(csvFileName, 'w'))
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

def csv_to_sql_insert(csv_file, table_name, sql_file):
    # Open the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header row

        # Build the SQL insert statements
        with open(sql_file, 'w') as sql_output:
            for row in reader:
                if any(row):  # Skip rows with all blank values
                    values = "', '".join(row)  # Assuming all values are strings, adjust as needed
                    insert_statement = f"INSERT INTO {table_name} VALUES ('{values}');\n"
                    sql_output.write(insert_statement)

generateCSV(csv_file)
print("Step 4 done, "+csvFileName+" generated")

csv_to_sql_insert(csvFileName, tableName, sqlFileName)

print("Step 5 done, "+sqlFileName+" generated")