"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." 

print 'Madlibs is on!'

name = raw_input('Give a name: ')
adj1 = raw_input('Give an adjective: ')
adj2 = raw_input('Give a second adjective: ')
adj3 = raw_input('And another: ')
verb = raw_input('We\'ll need a verb: ')
no1 = raw_input('Could we get a noun please?: ')
no2 = raw_input('Oh, we\'ll need a second one: ')
ani = raw_input('Sup, know any animal?: ')
food = raw_input('Food?: ')
fruit = raw_input('Fruity, hmm: ')
supe = raw_input('Your favourite superhero: ')
coum = raw_input('Nation: ')
dessert = raw_input('Cake or something else?: ')
year = raw_input('Gimme the year, son: ')

print STORY % (name, adj1, adj2, ani, food, verb, no1, fruit, adj3, name, supe, name, coum, name, dessert, name, year, no2)


