import os
from excelobj import ExcelObj

if __name__ == '__main__':
    import argparse
    parse = argparse.ArgumentParser()
    parse.add_argument("--src", type=str, help='excel_path',required=True)
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






    
    
    
