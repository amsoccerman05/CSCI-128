#   Aiden Morrison
#   CSCI 128 – Section J
#   Assessment 2
#   References: no one
#   Time: 3 Hours

# weight stuff
volume = 3.1415 * (63360 * 100) * (0.5 ** 2)
copper_weight = volume * 5.184
silver_weight = volume * 6.064
aluminum_weight = volume * 1.561

weight_list = ["Copper", copper_weight, "Silver", silver_weight, "Aluminum", aluminum_weight]

# resistivity stuff
resistance = (63360 * 100) / (3.1415 * (0.5 ** 2))
copper_resistance = resistance * 0.66
silver_resistance = resistance * 0.63
aluminum_resistance = resistance * 1.04

resistance_list = ["Copper", copper_resistance, "Silver", silver_resistance, "Aluminum", aluminum_resistance]

# taking price input and parsing it
price_input = input("PRICE> ")
price_list = price_input.split()

# metal input
metal_list = ["Copper", "Silver", "Aluminum"]
metal_input = input("METAL> ")

# find the index of the metal in the list
metal_index = metal_list.index(metal_input)

# seperate metal names and prices
metal_names = price_list[::2]
metal_prices = price_list[1::2]

# index of the selected metal
selected_metal_index = metal_names.index(metal_input)

# price for the selected metal
metal_price = float(metal_prices[selected_metal_index])

# calculate weight and resistance based on metal
metal_weight = weight_list[metal_index * 2 + 1]
metal_resistance = resistance_list[metal_index * 2 + 1]
total_price = metal_weight * metal_price

# print output in the correct units
print(f'OUTPUT {metal_input} Weight {metal_weight:.3f}')
print(f'OUTPUT {metal_input} Price {total_price:.3f}')
print(f'OUTPUT {metal_input} Resistivity {metal_resistance:.3f}')