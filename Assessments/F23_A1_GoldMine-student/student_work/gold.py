#   Aiden Morrison
#   CSCI 128 – Section J
#   Assessment 1: Gold Mine
#   References: no one
#   Time: 35 minutes

name = input("NAME> ")  #  name of mine stored as name
price = int(input("PRICE> "))  # gold ounce price as an integer

# the following are variables for development costs in millions
land = 145.23 * (10 ** 6)
equpiment = 36.2 * (10 ** 6)
equpiment1 = 209.5 * (10 ** 6)
infastructure = 80.7 * (10 ** 6)
dam = 48.1 * (10 ** 6)
misc = 28.2 * (10 ** 6)

costs = land + equpiment + equpiment1 + infastructure + dam + misc  # costs of development AKA investment

# the following are variables for operating costs
exca = 9 * 1_000_000
proc = 10 * 1_000_000
employ = 100_000 * 150
util = 100_000_000 * 1

costs1 = exca + proc + employ + util   # costs of operating costs

closure = 150_000_000

gold = (1_000_000 * 11) - 550_000  # resulting gold bars a year in grams - 5%

goldounce = (gold / 28.35)  # gold bars a year in ounces

yrrevenue = goldounce * price  # yearly revenue
yrrrevenue40 = goldounce * (price * 0.65)  # yearly revenue last 40yrs

yearlyprofit = yrrevenue - costs1  # yearly proft
yearlyprofit40 = yrrrevenue40 - costs1  # yearly profit last 40yrs
totalprofit = (20 * yearlyprofit) - (costs + closure)  # profit over 20 yrs
totalprofit40 = (20 * yearlyprofit) + (20 * yearlyprofit40) - (costs + closure)  # profit over 40yrs

print("OUTPUT Investment Planning Report of", name, "Mine in Colorado Springs")  # heading sentence for the report
print("OUTPUT", yearlyprofit)
print("OUTPUT", totalprofit)
print("OUTPUT", totalprofit40)
