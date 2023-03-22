# Auto-park
# DB ->
#       named as auto =>
#                       [ scheme of auto :
#                           {
#                              "label" : ... ,
#                              "price" : ... ,
#                              "wheels" : ... ,
#                              "color" : ... ,
#                              "number" : "random value"
#                           }
#                        ]
# Amount of auto > 10
# color : red , green , black , yellow , blue
# label : more than 5
# price : from 2000 till 200 000
# number and number length > 12
# Form category dictionary :
# dynamic
# cheap (2000 - 20000) , expensive(100000 - 200000) , medium - (20000 - 100000) - class car
# def sort_car_by_price (arr)
# return {
#   cheap : [],
#   medium : [],
#   expensive : []
# }
# print( cars that we have : for poor , rich , and medium-lvl persons )
# input -> sort : color -> choose on of : blue , green , ... ;  price , label
# for , while

import random

auto_park = []

label = ['Volkswagen', 'Audi', 'Mercedes-Benz', 'BMW', 'Ford', 'Volvo',
         'Peugeot', 'Renault', 'Daewoo', 'Fiat', 'Seat', 'Chevrolet',
         'Honda', 'Hyundai', 'KIA', 'Mazda', 'Mitsubishi', 'Nissan',
         'Opel', 'Skoda', 'Toyota']

body_type = ['sedan', 'hatchback', 'universal', 'cross', 'coupe', 'cabriolet']

color = ['red', 'green', 'black', 'yellow', 'blue', 'white', 'gray']


def random_from(list):  # Function for created random item from list
    return str(list[random.randint(0, len(list)-1)])


def price_of_auto():  # Function for created random price auto
    return random.randint(20_000, 200_000)


def number_of_engine():  # Function for created random number of engine
    return random.randint(100_000_000_000, 999_999_999_999)


# Ask user, how many auto in Auto-park
numbers_of_auto = int(
    input("Hello! How much auto in Auto-park would you want? "))

# Create Auto-park from user's numbers_of_auto
for auto in range(numbers_of_auto):
    auto_default = {
        'label': random_from(label),
        'body type': random_from(body_type),
        'price': price_of_auto(),
        'wheels': 4,
        'color': random_from(color),
        'number': number_of_engine(),
    }
    auto_park.append(auto_default)


print("- - - - - - - - - - - - - - - - -")
print("Auto-park: ", auto_park[0].values())
print("Auto-park: ", auto_park[1].values())
print("Auto-park: ", auto_park[2].values())


# def get_name(dictionary):
#     return dictionary['number']


# sorted_auto_park = auto_park.sort(key=get_name)

# print(sorted_auto_park)
