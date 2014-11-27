import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_project.settings')

import django
django.setup()

from stabbening.models import Unit, City, Player

def populate():
    #f = open(instructions_populate.txt)
    p = Player()
    u = Unit()
    c = City()
    for line in open("instructions_populate.txt"):
        split = line.split(" ")
        instruction = split[0]
        if "#" in instruction:
            continue
        if len(split) == 1:
            continue
        name = ' '.join(split[1:len(split)])
        print(name)
        if instruction == "P":
            p = add_player(name)
        elif instruction == 'C':
            c = add_city(name, p)
        elif instruction == 'U':
            u = add_unit(name, p, c)

def add_unit(name, player, city):
    u = Unit.objects.get_or_create(name=name, owner=player, city=city)[0]
    return u

def add_city(name, player):
    c = City.objects.get_or_create(name=name, owner=player)[0]
    return c

def add_player(name):
    p = Player.objects.get_or_create(name=name)[0]
    return p

if __name__ == '__main__':
    print("Populating...")
    populate()
