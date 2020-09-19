def ExtractMenu():
    from GetKleberMenuOnWebsite import getPdf
    from ConvertPdfMenuToTable import ConvertPdfMenuToTable
    from CleanMenuTable import CleanMenuTable

    getPdf()
    table_array = ConvertPdfMenuToTable()
    table_array = CleanMenuTable(table_array)

    print(table_array)
    return table_array
