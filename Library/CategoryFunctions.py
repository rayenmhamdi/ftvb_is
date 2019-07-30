import datetime


def getCategory(year, sexe):
    thisyear = datetime.datetime.now().year
    age = thisyear - year
    category = ''
    genre = ''
    if sexe == 'M':
        genre = 'G'
        if age in range(13):
            category = 'B'
        if age in range(13,15):
            category = 'E'
        if age in range(15,17):
            category = 'M'
        if age in range(17,19):
            category = 'C'
        if age in range(19,21):
            category = 'J'
        if age >= 21 :
            category = 'S'

    if sexe == 'F':
        genre = 'F'
        if age in range(14):
            category = 'E'
        if age in range(14,16):
            category = 'M'
        if age in range(16,18):
            category = 'C'
        if age in range(18,21):
            category = 'J'
        if age >= 21 :
            category = 'S'
    return '{}{}'.format(category,genre)
