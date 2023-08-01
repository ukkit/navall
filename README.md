# NAVALL

python script that downloads entire NAVAll.txt file from amfiindia site and then generates CSV file in following format:

``` csv
Scheme Type, Fund Family, Scheme Code, ISIN Div Payout/ISIN Growth, ISIN Div Reinvestment, Scheme Name, Net Asset Value, Date
```

It also generates SQL file with insert statements, like below:

``` sql
INSERT INTO <TABLENAME> VALUES ('Open Ended Schemes(Debt Scheme - Banking and PSU Fund)', 'Aditya Birla Sun Life Mutual Fund', '119551', 'INF209KA12Z1', 'INF209KA13Z9', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - IDCW', '112.1196', '22-May-2023');
```

## Required Packages

1. wget
2. pandas
3. csv
4. os
5. datetime
6. sqlalchemy
7. re
8. configparser

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

## MYSQL Database

1. Make a copy of file.ini.sample file as file.ini and populate the mysql database details
2. Uncomment last 2 lines in main.py file:

    ```python
    # sql_to_mysql(tableName, sqlFileName)
    # print("Step 6 done")
    ```

3. Execute the script and a new table will be created, with table name as in sql file (20230523114748)
4. The output will show how many records were commited, and list of failed commits:

    ```python
    Commited 12866| Failed 0
    ```
