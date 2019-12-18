Hello,

This is the code that will be responsible for parse the file generated via `hammer csv content-hosts --export` in a way where you should be able to create a nice Entitlement Report until Satellite version 6.6 (in 6.7 we have already a cute and awesome Report Template that will do it for you).

In order to use:

- Download the script
```
# wget https://raw.githubusercontent.com/waldirio/entitlement_report_parser/master/ent_report_parser.py
```

- Generate the input file
```
# hammer csv content-hosts --export > report.csv
```

- Parse the file
```
# ./ent_report_parser.py report.csv
```

Then the `parsed_output.csv` file will be created and you will be able to move forward importing on Libre Office, MS Excel or Google Spreadsheet. After that, just create your Pivot Table and combine the information.

In `Pivot Table`, our recommendation is
- In Row Fields
 -- Organization
 - Virtual
 - Guest of Host
 - Host Subscription
 - Name
 - SKU
 - Subscription Name
 - Socket
 - Cores

- In Data Fields
 - Subscription Name (Count)

Doing that, your report will be really AMAZING and totally useful.

Hope you enjoy it.
