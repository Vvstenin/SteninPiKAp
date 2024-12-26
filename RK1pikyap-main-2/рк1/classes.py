class Manufacturer:
    """Производитель"""

    def __init__(self, id, type, name):
        self.id = id
        self.type = type
        self.name = name


class Part:
    """Деталь"""

    def __init__(self, id, name, price, manufacturer_id):
        self.id = id
        self.name = name
        self.price = price
        self.manufacturer_id = manufacturer_id


class PartManufacturer:
    """Связь детали и производителя"""

    def __init__(self, manufacturer_id, part_id):
        self.manufacturer_id = manufacturer_id
        self.part_id = part_id


manufacturers = [
    Manufacturer(1, 1, "Производитель A"),
    Manufacturer(2, 2, "Производитель B"),
    Manufacturer(3, 1, "Производитель C"),
    Manufacturer(4, 3, "Производитель D"),
    Manufacturer(5, 2, "Производитель E")
]

parts = [
    Part(1, "Деталь 1", 12000, 1),
    Part(2, "Деталь 2", 300, 2),
    Part(3, "Деталь 3", 234, 3),
    Part(4, "Деталь 4", 1234, 5),
    Part(5, "Деталь 5", 12345, 1),
    Part(6, "Деталь 6", 12, 4)
]

part_manufacturer = [
    PartManufacturer(1, 4),
    PartManufacturer(2, 1),
    PartManufacturer(3, 2),
    PartManufacturer(4, 1),
    PartManufacturer(1, 2),
    PartManufacturer(5, 5),
    PartManufacturer(2, 5),
    PartManufacturer(3, 3),
    PartManufacturer(2, 4)
]

# Связь "один ко многим"
one_to_many = {}
for manufacturer in manufacturers:
    one_to_many[manufacturer.name] = [
        (part.name, part.price) for part in parts if part.manufacturer_id == manufacturer.id
    ]

# Связь "многие ко многим"
many_to_many_temp = [
    (manufacturer.name, part.name)
    for manufacturer in manufacturers
    for part in parts
    for relation in part_manufacturer
    if relation.manufacturer_id == manufacturer.id and relation.part_id == part.id
]


def main():
    """Основная функция"""

    print("Задание 1:", first(one_to_many))
    print("Задание 2:", second(one_to_many))
    print("Задание 3:", third(many_to_many_temp))


# Задание 1
def first(one_to_many):
    result = dict(filter(lambda item: len(item[1]) > 0,
                         {key: list(filter(lambda item: str(item[0]).startswith("Д"), val)) for key, val
                          in one_to_many.items()}.items()))
    return result


# Задание 2
def second(one_to_many):
    result = sorted({k: min([val[1] for val in one_to_many[k]]) for k in one_to_many.keys()}.items(),
                    key=lambda item: item[1])
    return result


# Задание 3
def third(many_to_many):
    result = sorted(many_to_many, key=lambda item: item[1])
    return result


def getOneToMany():
    return one_to_many


def getManyToMany():
    return many_to_many_temp


if __name__ == '__main__':
    main()