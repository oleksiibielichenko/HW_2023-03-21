# + Auto-park
# + DB ->
# +       named as auto =>
# +                       [ scheme of auto :
# +                           {
# +                              "label" : ... ,
# +                              "price" : ... ,
# +                              "wheels" : ... ,
# +                              "color" : ... ,
# +                              "number" : "random value"
# +                           }
# +                        ]
# + Amount of auto > 10
# + color : red , green , black , yellow , blue
# + label : more than 5
# + price : from 2000 till 200 000
# + number and number length > 12
# + Form category dictionary :
# + dynamic
# + cheap (2000 - 20000) , expensive(100000 - 200000) , medium - (20000 - 100000) - class car
# + def sort_car_by_price (arr)
# + return {
# +   cheap : [],
# +   medium : [],
# +   expensive : []
# + }
# print( cars that we have : for poor , rich , and medium-lvl persons )
# input -> sort : color -> choose on of : blue , green , ... ;  price , label
# for , while

import random

auto_park = []
cheap_auto = []
medium_auto = []
expensive_auto = []
color_auto = []

label = ['Volkswagen', 'Audi', 'Mercedes-Benz', 'BMW', 'Ford', 'Volvo',
         'Peugeot', 'Renault', 'Daewoo', 'Fiat', 'Seat', 'Chevrolet',
         'Honda', 'Hyundai', 'KIA', 'Mazda', 'Mitsubishi', 'Nissan',
         'Opel', 'Skoda', 'Toyota']

body_type = ['sedan', 'hatchback', 'universal', 'cross', 'coupe', 'cabriolet']

color = ['red', 'green', 'black', 'yellow', 'blue', 'white', 'gray']


def random_from(list):  # Function for created random item from list
    return str(list[random.randint(0, len(list)-1)])


def price_of_auto():  # Function for created random price auto
    return random.randint(2_000, 200_000)


def number_of_engine():  # Function for created random number of engine
    return random.randint(100_000_000_000, 999_999_999_999)


# Ask user, how many auto in Auto-park
numbers_of_auto = int(
    input("Hello! How much auto in Auto-park would you want?: "))
print("   Auto-park:")
# Create Auto-park from user's numbers_of_auto
for auto in range(numbers_of_auto):
    random_auto = {
        'label': random_from(label),
        'body type': random_from(body_type),
        'price': price_of_auto(),
        'wheels': 4,
        'color': random_from(color),
        'number': number_of_engine(),
    }
    print(f"{auto + 1}) ", random_auto)
    auto_park.append(random_auto)


# def get_name(auto):
#     return auto['price']
# auto_park.sort(key=get_name)

auto_park.sort(key=lambda auto: auto['price'])


for auto in range(numbers_of_auto):
    if auto_park[auto]['price'] < 20_000:
        auto_cheap = auto_park[auto]
        cheap_auto.append(auto_cheap)
    elif auto_park[auto]['price'] >= 20_000 and auto_park[auto]['price'] < 100_000:
        auto_medium = auto_park[auto]
        medium_auto.append(auto_medium)
    else:
        auto_expensive = auto_park[auto]
        expensive_auto.append(auto_expensive)

print("   Cheap auto:")
for num, auto in enumerate(cheap_auto):
    print(f"{num + 1}) {auto}")

print("   Medium auto:")
for num, auto in enumerate(medium_auto):
    print(f"{num + 1}) {auto}")

print("   Expensive auto:")
for num, auto in enumerate(expensive_auto):
    print(f"{num + 1}) {auto}")

user_color = input("Enter color of auto: ")

for auto in range(numbers_of_auto):
    if auto_park[auto]['color'] == user_color:
        auto_color = auto_park[auto]
        color_auto.append(auto_color)

if color_auto:
    print(f"   Auto of {user_color} color: ")
    for num, auto in enumerate(color_auto):
        print(f"{num + 1}) {auto}")
else:
    print(f"   Sorry, there are no auto of {user_color} color.")
