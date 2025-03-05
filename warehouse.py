warehouse_locations = {
    "Warehouse A": (12.9715987, 77.5945627),  
    "Warehouse B": (28.7040592, 77.1024902),
    "Warehouse C": (19.076090, 72.877426),
}

def get_warehouse_location(warehouse_name):
    lowercase_locations = {k.lower(): v for k, v in warehouse_locations.items()}
    print(lowercase_locations)
    print(warehouse_name.lower())
    return lowercase_locations.get(warehouse_name.lower(), "Warehouse not found")

print(get_warehouse_location("Warehouse A"))  
print(get_warehouse_location("Warehouse B"))
print(get_warehouse_location("Warehouse C"))  
print(get_warehouse_location("Warehouse X"))  
