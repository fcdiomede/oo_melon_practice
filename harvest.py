############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType('musk', 1998, 'green',
                      True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange',
                        True, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green',
                        True, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow',
                        True, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f'{melon.name} paris with')
        for pairing in melon.pairings:
            print(f'-{pairing}')
        print('\n')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}
    # Fill in the rest
    for melon in melon_types:
        melon_codes[melon.code] = melon

    return melon_codes

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating,
                    field_harvested, farmer_harvested):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_harvested = field_harvested
        self.farmer_harvested = farmer_harvested

    def is_sellable(self):
        return (self.shape_rating > 5 and self.color_rating > 5
                and self.field_harvested != 3)

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)

    melons_harvested = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melons_harvested.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melons_harvested.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melons_harvested.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melons_harvested.append(melon_4)

    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Micheal')
    melons_harvested.append(melon_5)

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Micheal')
    melons_harvested.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Micheal')
    melons_harvested.append(melon_7)

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Micheal')
    melons_harvested.append(melon_8)

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    melons_harvested.append(melon_9)

    return melons_harvested

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        can_sell = melon.is_sellable()
        if can_sell:
            sellable = 'CAN BE SOLD'
        else:
            sellable = 'NOT SELLABLE'
        print(f'Harvested by {melon.farmer_harvested} from',
            f'Field {melon.field_harvested} ({sellable})')

def make_melons_from_file(filename, melon_types):
    f = open(filename)

    melons_by_id = make_melon_type_lookup(melon_types)
    
    melons = []

    for line in f:
        line = line.rstrip()
        data = line.split(" ")

        melon_type = data[5]
        shape_rating = int(data[1])
        color_rating = int(data[3])
        field_harvested = int(data[11])
        farmer_harvested = data[8]

        melon = Melon(melons_by_id[melon_type], shape_rating, 
                    color_rating, field_harvested, farmer_harvested)

        melons.append(melon)

    f.close()

    return melons



