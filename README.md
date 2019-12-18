Hello,

This is the code that will be responsible for parse the file generated via `hammer csv content-hosts --export` in a way where you should be able to create a nice report, for example, using pivot table.

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

Then the `parsed_output.csv` will be created and you will be able to move forward importing on Libre Office, MS Excel or Google Spreadsheet. After that, just create your Pivot Table.

Hope you enjoy it.
