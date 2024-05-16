from math import inf
import json

from my_grafics import Grafics
from my_methods import Methods

data = {
    "initial": {
        "baseX": 50000,
        "baseY": 0,
        "aimPhiTMinus3": 41.63,
        "aimRTMinus3": 45155,
        "aimPhiTMinus2": 41.97,
        "aimRTMinus2": 44860,
        "rocketSpeedCoeff": -2,
        "aimSpeedCoeff": 0.5,
        "oneTimeInterval": 0.3,
        "catchDistance": 500
    },
    "fly": []
}


def print_json(table):
    print("initial :\n",
          json.dumps(table["initial"], indent=2),
          "\nfly :")
    for i in table["fly"]:
        print(" {", "\n   moment:", i["moment"],
              "\n   aimPhi:", i["aimPhi"], "\n   aimR:", i["aimR"],
              "\n   aimX:", i["aimX"], "\n   aimY:", i["aimY"],
              "\n   catcherPhi:", i["catcherPhi"], "\n   catcherRho:", i["catcherRho"],
              "\n   catcherX:", i["catcherX"], "\n   catcherY:", i["catcherY"],
              "\n   distance:", i["distance"], "\n }")


method = Methods(data)

print("Please, choose your method")
print("1. Three point")
print("2. Straightening")
print("3. Сhase")
print("4. Parallel_approach")
print("5. Proportional convergence")
print("6. Constant angle")

choose_1 = int(input())

print("Then, please choose:")
print("1. Meeting")
print("2. Catching up")

choose_2 = int(input())

if (choose_2 == 2):
    if (choose_1 == 1):
        my_table_1 = method.three_point(False)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Three point, Catching up")
    elif (choose_1 == 2):
        my_table_1 = method.straightening(True, 0.5)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Straightening, Catching up")
    elif (choose_1 == 3):
        my_table_1 = method.chase(True)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Chase, Cathcing up")
    elif (choose_1 == 4):
        my_table_1 = method.parallel_approach(False)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Parallel approach, Catching up")
    elif (choose_1 == 5):
        my_table_1 = method.proportional_convergence(False, inf)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Proportional convergence, Catching up")
    elif (choose_1 == 6):
        my_table_1 = method.constant_angle(True)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Constant angle, Catching up")
    else:
        print("Wrong input!")

elif (choose_2 == 1):
    if (choose_1 == 1):
        my_table_1 = method.three_point(False)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Three point, Meeting")
    elif (choose_1 == 2):
        my_table_1 = method.straightening(True, 0.5)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Straightening, Meeting")
    elif (choose_1 == 3):
        my_table_1 = method.chase(True)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Chase, Meeting")
    elif (choose_1 == 4):
        my_table_1 = method.parallel_approach(False)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Parallel approach, Meeting")
    elif (choose_1 == 5):
        my_table_1 = method.proportional_convergence(False, inf)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Proportional convergence, Meeting")
    elif (choose_1 == 6):
        my_table_1 = method.constant_angle(True)
        print_json(my_table_1)
        Grafics(my_table_1, False, "Constant angle, Meeting")
    else:
        print("Wrong input!")
else:
    print("Wrong input!")