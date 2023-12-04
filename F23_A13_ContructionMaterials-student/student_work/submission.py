#   Aiden Morrison
#   CSCI 128 – Section J
#   Assessment 13
#   References: no one
#   Time: 1 hours

class Material:
    def __init__(self, id):
        self.id = id
        self.price = 0
        self.materialType = 'Not Determined'

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setMaterialType(self, materialType):
        self.materialType = materialType

    def getMaterialType(self):
        return self.materialType

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id


class ConstructionSite:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.price = 0
        self.materials = []

    def addMaterial(self, material):
        self.materials.append(material)

    def findMaterial(self, id):
        for material in self.materials:
            if material.getID() == id:
                return material
        return -1

    def calculatePrice(self):
        self.price = sum(material.getPrice() for material in self.materials)

    def countMaterials(self):
        wood_count = sum(1 for material in self.materials if material.getMaterialType() == 'WOOD')
        steel_count = sum(1 for material in self.materials if material.getMaterialType() == 'STEEL')
        brick_count = sum(1 for material in self.materials if material.getMaterialType() == 'BRICK')
        return [wood_count, steel_count, brick_count]

    def __str__(self):
        return f"{self.name} site in {self.city} has {len(self.materials)} materials, with a value of {int(self.price)}."


if __name__ == "__main__":
    site_name = input("NAME> ")
    city_name = input("CITY> ")
    file_path = input("FILE> ")

    construction_site = ConstructionSite(site_name, city_name)

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.split()
            material_id = int(data[0])
            material_type = data[1]
            material_price = float(data[2])

            material = Material(material_id)
            material.setMaterialType(material_type)
            material.setPrice(material_price)
            construction_site.addMaterial(material)

    construction_site.calculatePrice()
    construction_site_info = f"OUTPUT {construction_site}"

    materials_count = construction_site.countMaterials()
    materials_output = f"OUTPUT WOOD:{materials_count[0]} STEEL:{materials_count[1]} BRICK:{materials_count[2]}"

    print(construction_site_info)
    print(materials_output)
