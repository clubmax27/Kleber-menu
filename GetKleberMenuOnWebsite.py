def getPdf():
    import requests

    #Link of the pdf
    url = 'https://lycee-kleber.com.fr/wp-content/uploads/2020/03/menu_kleber.pdf'
    r = requests.get(url, allow_redirects=True)

    #Download the PDF in a file called "menu_kleber.pdf"
    open('menu_kleber.pdf', 'wb').write(r.content)