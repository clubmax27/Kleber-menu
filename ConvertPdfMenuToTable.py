import tabula
import pandas as pd

def ConvertPdfMenuToTable():
    #Read the PDF with a template in lattice mode
    df = tabula.read_pdf_with_template(input_path = r'C:\Users\Maxence-Mathieu\Desktop\code\Kleber-menu\menu_kleber.pdf', 
                                    template_path = r'C:\Users\Maxence-Mathieu\Desktop\code\Kleber-menu\menu_kleber.tabula-template.json',
                                    lattice = True #, format = "CSV", output_path = (r'C:\Users\Maxence-Mathieu\Desktop\code\Kleber-menu\menu.csv')
                                    )
    table = df[0]

    #Only keep the five first rows
    table = table[:5]

    cols = [0,2,4,6,8]
    #Remove columns about alergens
    table.drop(table.columns[cols], axis = 1, inplace = True)

    return table.values.tolist()