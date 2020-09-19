import tabula
import pandas as pd
import math as m
import re

options = tabula.io.build_options(pages = '1', lattice = True)

df = tabula.read_pdf_with_template(input_path = r'C:\Users\Maxence-Mathieu\Desktop\code\Kleber-menu\menu_kleber.pdf', 
                                   template_path = r'C:\Users\Maxence-Mathieu\Desktop\code\Kleber-menu\menu_kleber.tabula-template.json',
                                   lattice = True #, format = "CSV", output_path = (r'C:\Users\Maxence-Mathieu\Desktop\code\Kleber-menu\menu.csv')
                                   )
table = df[0]

table = table[:5]

cols = [0,2,4,6,8]
table.drop(table.columns[cols], axis = 1, inplace = True)

#table.to_excel("output.xlsx")

table_array = table.values.tolist()

for day in range(len(table_array)):

    category = 0
    while category < len(table_array[day]):
        table_array[day][category]
        
        #We remove eventual NaN values
        if((not isinstance(table_array[day][category], str)) and m.isnan(table_array[day][category])):
            table_array[day].pop(category)
            continue

        #We replace \r by spaces
        table_array[day][category] = table_array[day][category].replace("\r", " ")

        #We remouve double spaces
        table_array[day][category] = " ".join(table_array[day][category].split())

        category += 1

#Convert each category into a list, so we can split them
for day in range(len(table_array)):
    for category in range(len(table_array[day])):
        table_array[day][category] = re.findall('[A-Z][^A-Z]*', table_array[day][category])


for day in range(len(table_array)):
    for category in range(len(table_array[day])):
        for meal in range(len(table_array[day][category])):
            #We remove useless spaces at the start of the end
            table_array[day][category][meal] = table_array[day][category][meal].strip()

print(table_array)
