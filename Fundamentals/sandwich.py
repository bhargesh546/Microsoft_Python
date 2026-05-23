def make_sandwich(bread_type, filling, cheese = None, toasted = False):
    description = "Making a "

    if toasted:
        description += "toasted "

    description += f"{bread_type} sandwich with {filling}"

    if cheese != None:
        description += f" and {cheese} cheese"

    description += "."

    return description

#print(make_sandwich("wheat", "turkey", "cheddar", True))
print(make_sandwich("rye", "ham"))