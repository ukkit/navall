# NAVALL

python script that downloads entire NAVAll.txt file from amfiindia site and then generates CSV file in following format:

> Scheme Type, Fund Family, Scheme Code, ISIN Div Payout/ISIN Growth, ISIN Div Reinvestment, Scheme Name, Net Asset Value, Date

## Required Packages

1. wget
2. pandas
3. csv
4. os
5. datetime

## Execution

> python3 main.py

## Output

> out/YmdHMS.csv

> out/20230523114748.csv

> out/20230523114748.sql

## CSV File

```text
Scheme Type,Fund Family,Scheme Code,ISIN Div Payout/ISIN Growth,ISIN Div Reinvestment,Scheme Name,Net Asset Value,Date
Open Ended Schemes(Debt Scheme - Banking and PSU Fund),Aditya Birla Sun Life Mutual Fund,119551,INF209KA12Z1,INF209KA13Z9,Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - IDCW,111.3747,27-Apr-2023
Open Ended Schemes(Debt Scheme - Banking and PSU Fund),Aditya Birla Sun Life Mutual Fund,119552,INF209K01YM2,-,Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - MONTHLY IDCW,114.8782,27-Apr-2023
```

## SQL File

```sql
INSERT INTO 20230523114748 VALUES ('Open Ended Schemes(Debt Scheme - Banking and PSU Fund)', 'Aditya Birla Sun Life Mutual Fund', '119551', 'INF209KA12Z1', 'INF209KA13Z9', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - IDCW', '112.1196', '22-May-2023');
INSERT INTO 20230523114748 VALUES ('Open Ended Schemes(Debt Scheme - Banking and PSU Fund)', 'Aditya Birla Sun Life Mutual Fund', '119552', 'INF209K01YM2', '-', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - MONTHLY IDCW', '114.99', '22-May-2023');
INSERT INTO 20230523114748 VALUES ('Open Ended Schemes(Debt Scheme - Banking and PSU Fund)', 'Aditya Birla Sun Life Mutual Fund', '119553', 'INF209K01YO8', '-', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - Direct - Quarterly IDCW', '113.0564', '22-May-2023');
INSERT INTO 20230523114748 VALUES ('Open Ended Schemes(Debt Scheme - Banking and PSU Fund)', 'Aditya Birla Sun Life Mutual Fund', '108272', 'INF209K01LX6', 'INF209KA11Z3', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - REGULAR - IDCW', '158.6509', '22-May-2023');
INSERT INTO 20230523114748 VALUES ('Open Ended Schemes(Debt Scheme - Banking and PSU Fund)', 'Aditya Birla Sun Life Mutual Fund', '110282', 'INF209K01LU2', '-', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - REGULAR - MONTHLY IDCW', '111.6845', '22-May-2023');
```

