def remove_items(countries, island):
    original = []
    original.append(countries)
    island = island
    countries.remove(island)
    return countries
print(remove_items(countries=["Perú", "Margarita", "Ecuador", "Panamá"], island="Margarita"))