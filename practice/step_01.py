price = 250000        # int
area = 1200.5         # float
city = "Pune"         # str
is_sold = False       # bool
# print(type(price), type(area), type(city), type(is_sold))

# print(f"House in {city} with area {area} and price {price}")


prices = [250000, 300000, 150000, 400000]
# print(type(prices))

# print("Prices list: ", prices)
# print(f"price is {prices}")

prices.append(10)
print("Updated prices list: ", prices)
# print(prices[0], prices[1:3], prices[-1], prices[-2])

for p in prices :
    if p > 300000:
        print(p, " expensive")
    else :
        print(p, " affordable")

in_lakhs = [p / 10000 for p in prices]
print(in_lakhs, type(in_lakhs))

in_expensive = [p for p in prices if p > 300000]
print(in_expensive)





















# area
# print(type(area))
# area = 5
# print(type(area))
# area = "gaurav"
# print(type(area))
# area = 0.0
# print(type(area))
# area = "fjdjf"
# print(type(area))
# area = 'C'
# print(type(area))

# # area = true
# # print(type(area))

# area = True
# print(type(area))

