# Excel2sql
generate .sql from the excel

## the format of the excel and NOTES
1. the column name of sheet must be legal
eg: 'name','location','名字',‘性别'... which do not contain character '\' or ' " ' ...
2. the column name must not be empty
3. the generate table name is same as the excel sheet
4. all the attribute of the table field are varchar(255)
5. 'use xxxdatabase', before 'source xxx.sql' in DBMS
6. the .sql contains 'create' statement

## quick start
``` python
import os
from excelobj import ExcelObj

if __name__ == '__main__':
    import argparse
    parse = argparse.ArgumentParser()
    # the excel path
    parse.add_argument("--src", type=str, help='excel_path',required=True)
    # the .sql path
    parse.add_argument("--dst", type=str, help='target_path',required=True)
    
    args = parse.parse_args()

    if not (os.path.exists(args.src)):
        print("{0} doesn't exists".format(args.src))
        
    excelobj = ExcelObj(args.src)

    sqllist = excelobj.excel2sql()

    for (table,sqlstatement) in sqllist.items():
        targetpath = os.path.join(args.dst, '{0}.sql'.format(table))
        for ind in range(0,len(sqlstatement)):
            sqlstatement[ind] += '\n'

        with open(targetpath, 'w') as sqlfile:
            sqlfile.writelines(sqlstatement)
```
