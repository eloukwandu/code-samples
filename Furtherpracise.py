import random
import urllib.request

def add_number(*args):
    total = 0
    for a in args:
        total += a
    print(total)


def numbers(*args):

    grade = 0
    for n in args:
        grade += n
    print(grade)


def get_gender(sex='unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    elif sex is 'name':
        sex = "Kindness"

    print(sex)


def download_web_image(url):
    name = random.randrange(1, 2000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)













