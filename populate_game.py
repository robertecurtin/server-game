import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_project.settings')

import django
django.setup()

from stabbening.models import Unit, City#, Player

def populate():
    python_city = add_city('Carlton')
    python_unit = add_unit('Dave', python_city)



def add_unit(name, city):
    u = Unit.objects.get_or_create(name=name, city=city)[0]
    return u

def add_city(name):
    c = City.objects.get_or_create(name=name)[0]
    return c

if __name__ == '__main__':
    print("Populating...")
    populate()
