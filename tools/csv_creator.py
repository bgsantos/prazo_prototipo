import csv 
from tools.logger import createLog

def createCSV(file, headers, data): 
    try: 
        output = csv.writer(open(file,'w'))
    except Exception as e:
        createLog('error', e)
        return False
    
    output.writerow(headers)

    for i in data:
        output.writerow(i)