"""Print out all the melons in our inventory."""


from melons import melon_list 


def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for key, value in melons.items():
        print("\n", key.upper())

        for value, attributes in value.items():
            print(f"{value}: {attributes}")

print_melon(melon_list)

    

    
