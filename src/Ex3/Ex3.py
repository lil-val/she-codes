import random
import urllib.request

def download_image(url):
    name = random.randint(1, 1000)
    full_name = str(name) + ".png"
    urllib.request.urlretrieve(url, full_name)

download_image("http://www.she-codes.org/sc/wp-content/uploads/2014/11/logo-copy200.png")