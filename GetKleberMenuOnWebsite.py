def getPdf():
    import requests

    url = 'https://lycee-kleber.com.fr/wp-content/uploads/2020/03/menu_kleber.pdf'
    r = requests.get(url, allow_redirects=True)
    open('menu_kleber.pdf', 'wb').write(r.content)