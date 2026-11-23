# dictionaries


house =  {
    "city":"Pune",
    "area" : 1200,
    "price" : 5000000
}

# print(house["city"])
# print(house.get("area"))
# print(house.get("price"))

# print(house)
# print(house.items())

# for key, value in house.items() :
#     print(key, "  ", value)


houses = [
    {"city": "Pune",   "price": 250000},
    {"city": "Mumbai", "price": 900000},
    {"city": "Pune",   "price": 320000},
    {"city": "Nagpur", "price": 150000},
]

print(houses[2].get("price"))

print(houses[2].get("bedrooms", 1))

print(houses)
print(houses[2].get("bedrooms"))

# COunt he houses in each city in list of dictionaries 
counts = {}
# print(type(counts))
for h in houses:
    city = h["city"]
    counts[city] = counts.get(city, 0) + 1

print(counts)