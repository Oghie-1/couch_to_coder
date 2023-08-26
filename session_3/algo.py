#!/usr/bin/python3

animals = [
    {"name": "capybara", "group": "mammal", "weight": 110},
    {"name": "hedgehog", "group": "mammal", "weight": 0.5},
    {"name": "bearded dragon", "group": "reptile", "weight": 1},
    {"name": "tortoise", "group": "reptile", "weight": 40},
    {"name": "hummingbird", "group": "bird", "weight": 0.01},
    {"name": "elephant", "group": "mammal", "weight": 10000},
    {"name": "ostrich", "group": "bird", "weight": 280},
    {"name": "python", "group": "reptile", "weight": 180},
    {"name": "blue whale", "group": "mammal", "weight": 300000},
    {"name": "lion", "group": "mammal", "weight": 350}
]
""""""

# Print out all the animals names that are heavier than 100 pounds!

#def heavy_animals(animals):
    for animal in animals:
        if animal["weight"] > 100:
            print(animal["name"])


#animal_names_heavier_than_100 = heavy_animals(animals)

#print(animal_names_heavier_than_100)


# Print out the heaviest animal!
def heaviest_animal(animals):
    heaviest_animal = animals[2]
    print(heaviest_animal)

    for animal in animals:
        if animal["weight"] > heaviest_animal["weight"]:
            heaviest_animal = animal


heaviest_animal = heaviest_animal(animals)

print(heaviest_animal)
