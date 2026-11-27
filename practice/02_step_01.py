# dictionaries


# house =  {
#     "city":"Pune",
#     "area" : 1200,
#     "price" : 5000000
# }

# print(house["city"])
# print(house.get("area"))
# print(house.get("price"))

# print(house)
# print(house.items())

# for key, value in house.items() :
#     print(key, "  ", value)


# list of dictionaries
houses = [
    {"city": "Pune",   "price": 250000},
    {"city": "Mumbai", "price": 900000},
    {"city": "Pune",   "price": 320000},
    {"city": "Nagpur", "price": 150000},
]

# print(houses[2].get("price"))

# print(houses[2].get("bedrooms", 1))

# print(houses)
# print(houses[2].get("bedrooms"))

# COunt he houses in each city in list of dictionaries 
# counts = {}
# print(type(counts))
# for h in houses:
    # city = h["city"]
    # counts[city] = counts.get(city, 0) + 1

# print(counts)

# print(houses.items())   -> gives error
# for h in houses :
#     for key, value in h.items():
#         print(key, " ", value)
#     print("\n")


##### dict comprehensions
# price_by_city = {
#     house["city"] : house["price"]
#     for house in houses
# }

# equivalent to 
# price_by_city = {}
# for house in houses:
    # price_by_city[house["city"]] = house["price"]

# print(price_by_city)


# -------------------------------------------
#-----STEP - 03------------------------------
# def greet() :
#     return "Hello from gaurav"

# message = greet()
# print(message)
# print(greet())

# def price_with_tax(price, tax_rate):
#     return price * (1 + tax_rate)

# total = price_with_tax(250000, 0.1)
# print(total)  # 275000.0

# total = price_with_tax(tax_rate=250000, price=0.1)
# print(total)

def price_total(*prices):
    return sum(prices)

# print(price_total(400, 300, 300))

def show_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_details(city="Pune", price=250000, bedrooms=3)
