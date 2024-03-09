import csv
import os
import django
import sys


from otome_game_website.models import Game, Character


def run():
    with open('/Users/baoyintamier/Desktop/Engineering_software_design/django/project_temp/otome_game_website/database.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header
        Game.objects.all().delete()
        Character.objects.all().delete()
        title = set()
        platform=set()
        introduction=set()
        name = set()
        storyline = set()
        character = []

        for row in reader:
            print(row)
            title.add(row[0])
            platform.add(row[1])
            introduction.add(row[2])
            name.add(row[3])
            storyline.add(row[4])

        for (n,s) in zip(name, storyline):
            c = Character(
            name = n,
            storyline = s 
            )
            c.save()
            character.append(c)
        
        for (t,p,i) in zip(title, platform, introduction):
            game = Game(
                title=t, 
                platform=p,
                introduction=i,
                
            )
            game.save()
            game.characters.set(character) 
            

run()

