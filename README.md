# NAVALL

python script that downloads entire NAVAll.txt file from amfiindia site and then generates CSV file in following format:

> Scheme Type, Fund Family, Scheme Code, ISIN Div Payout/ISIN Growth, ISIN Div Reinvestment, Scheme Name, Net Asset Value, Date

## Required Packages

1. wget
2. pandas
3. csv
4. os
5. time

## Execution

> python main.py

## Output

```
> time.csv
```
## CSV File

```
Scheme Type,Fund Family,Scheme Code,ISIN Div Payout/ISIN Growth,ISIN Div Reinvestment,Scheme Name,Net Asset Value,Date
Open Ended Schemes(Debt Scheme - Banking and PSU Fund),Aditya Birla Sun Life Mutual Fund,119551,INF209KA12Z1,INF209KA13Z9,Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - IDCW,111.3747,27-Apr-2023
Open Ended Schemes(Debt Scheme - Banking and PSU Fund),Aditya Birla Sun Life Mutual Fund,119552,INF209K01YM2,-,Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - MONTHLY IDCW,114.8782,27-Apr-2023
```
