def CleanMenuTable(table_array):
    import math as m
    import re

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

    return table_array