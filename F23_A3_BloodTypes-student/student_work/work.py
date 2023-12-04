#   Aiden Morrison
#   CSCI 128 – Section J
#   Assessment 3: Blood Types
#   References: no one
#   Time: 1 Hour

#  inputs
bank1 = input("PRIMARY> ")
bank2 = input("SECONDARY> ")
wanted_blood = input("TYPE> ")

#  types of blood inventory
blood = {"P": "plenty", "S": "scarce", "I": "insufficient"}
#  types of blood
blood_types = ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]

#  checking if blood wanted is in the types, then indexing and outputting availability
if wanted_blood in blood_types:
    blood_index = blood_types.index(wanted_blood)
    availability1 = blood[bank1[blood_index]]
    availability2 = blood[bank2[blood_index]]

    print(f"OUTPUT {wanted_blood} in the primary blood bank stocks is {availability1}.")
    print(f"OUTPUT {wanted_blood} in the secondary blood bank stocks is {availability2}.")
#  else: if any input not in blood_types is given, invalid
else:
    print("OUTPUT Invalid blood type. Please provide a valid blood type.")