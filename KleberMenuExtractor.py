import PyPDF2

#Stolen code from internet, does its job, don't care
pdf_file = open("C:\\Users\\Maxence Mathieu\\Desktop\\code\\KleberMenuExtractor\\menu_kleber.pdf", 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()

#Menu has lots of newlines because of the convertion from PDF to text, we remove those
#menu = page_content.replace('\n', '')
menu = page_content#.encode('utf-8')

#There are 5 keywords : Lundi, Mardi, Mercredi, Jeudi, Vendredi
#PyPDF2 reads them as : L U N D I, M A R D I, M E R C R E D I, J E U D I, V E N D R E D I
#So we split our text in 6 different parts : the 5 days, what's before
#\nM\n \nA\n \nR\n \nD\n \nI\n
keywords = ["\nL\n \nU\n \nN\n \nD\n \nI\n", "\nM\n \nA\n \nR\n \nD\n \nI\n", "\nM\n \nE\n \nR\n \nC\n \nR\n \nE\n \nD\n \nI\n", "\nJ\n \nE\n \nU\n \nD\n \nI\n", "\nV\n \nE\n \nN\n \nD\n \nR\n \nE\n \nD\n \nI\n"]
splitedMenuByDay = []
splitedMenu = [[0 for x in range(4)] for y in range(5)]

#We split by day the menu
for iKeyword in range(0, len(keywords)):
    print(menu.find(keywords[iKeyword]))
    #We get the part of the menu that we want
    partOfTheMenu = menu.split(keywords[iKeyword])

    #We remove the part of the menu that we got from the original menu
    menu = menu.replace(partOfTheMenu[0], "")

    #We remove the name of the day that is still in the menu
    menu = menu.replace(keywords[iKeyword], "")

    #We insert that part of the menu inside an array
    splitedMenuByDay.insert(iKeyword, partOfTheMenu[0])

#remove useless part of the menu
splitedMenuByDay.pop(0)
splitedMenuByDay.insert(4,menu)

print(splitedMenuByDay)

#Now that we have splitted by day, we split by categories
for iDay in range(0, 4):   
    for iCategorie in range(0, 3):
        splitedMenu[iDay][iCategorie] = splitedMenuByDay[iDay].split("ALLERGÈNES")
        splitedMenuByDay[iDay].replace(splitedMenu[iDay][iCategorie], "")

print(splitedMenu)