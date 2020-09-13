"""from pdf2image import convert_from_path

images = convert_from_path('C:\\Users\\Maxence Mathieu\\Desktop\\code\\Kleber-menu\\menu_kleber.pdf')

image = images[0]
image.save('out.jpg', 'JPEG')"""

from pdf2image import convert_from_path

pages = convert_from_path(r'C:\Users\Maxence-Mathieu\Desktop\code\Kleber-menu\menu_kleber.pdf', 500, poppler_path = r"C:\Users\Maxence-Mathieu\Desktop\code\Kleber-menu\poppler\bin")
page = pages[0]
page.save('out.jpg', 'JPEG')