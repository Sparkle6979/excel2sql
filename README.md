# Excel2sql
generate .sql from the excel

## the format of the excel and NOTES
1. the column name of sheet must be legal,eg: 'name','location','名字',‘性别'... which do not contain character '\' or ' " ' ...
2. the column name must not be empty
---
3. the generate table name is same as the excel sheet
4. all the attribute of the table field are varchar(255)
5. the .sql contains 'create' statement

## quick start

