from xlrd import open_workbook
from xlutils.copy import copy
import json

# Reading the Json file and Getting the Customer number
json_file='output4.json'
with open(json_file) as f:
    data=json.load(f)
    try:
        keys=data['environment']['values']
        for key in keys:
            if key['key']=="cust_no":
                customer_number=key['value']
    except Exception as e:
        print e

#Updating the Excel Sheet
rb = open_workbook("Modesto_Inputs.xls")
wb = copy(rb)
s = wb.get_sheet('CustomerSearch')
s.write(1,1,customer_number)
wb.save('Modesto_Inputs.xls')
