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

# my_table_1 = method.three_point(True)
# print_json(my_table_1)
# Grafics(my_table_1, False)

# my_table_2 = method.straightening(True, 0.5)
# print_json(my_table_2)
# Grafics(my_table_2, False)

# my_table_3 = method.chase(True)
# print_json(my_table_3)
# Grafics(my_table_3, False)

# my_table_4 = method.parallel_approach(False)
# print_json(my_table_4)
# Grafics(my_table_4, False)

my_table_5 = method.proportional_convergence(True, inf)
print_json(my_table_5)
Grafics(my_table_5, True)

# my_table_6 = method.constant_angle(False)
# print_json(my_table_6)
# Grafics(my_table_6, False)