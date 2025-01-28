travel_log = {
    "Nigeria": ["Delta", "Edo", "Lagos", "Abuja"],
    "America": ["Los Angeles", "California"]
}

print(travel_log["Nigeria"][1])

States_in_Nigeria = ["Rivers", "Enugu", ["Warri", "Asaba", "Ekpan"]]
print(States_in_Nigeria[2][1])



order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}


print(order["main"][2][0])