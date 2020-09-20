def ExtractMenu():
    from GetKleberMenuOnWebsite import getPdf
    from ConvertPdfMenuToTable import ConvertPdfMenuToTable
    from CleanMenuTable import CleanMenuTable

    #We get the PDF on the website
    getPdf()

    #We get the raw data of the PDF from tabula
    table_array = ConvertPdfMenuToTable()

    #We clean the data (remove spaces, split meals ...)
    table_array = CleanMenuTable(table_array)

    #print(table_array)
    #We return the cleaned data
    return table_array
