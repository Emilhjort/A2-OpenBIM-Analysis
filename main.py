from pathlib import Path
import ifcopenshell

modelname = "LLYN - ARK_modified"

try:
    dir_path = Path(__file__).parent
    model_url = Path.joinpath(dir_path, 'model', modelname).with_suffix('.ifc')
    model = ifcopenshell.open(model_url)
except OSError:
    try:
        import bpy
        model_url = Path.joinpath(Path(bpy.context.space_data.text.filepath).parent, 'model', modelname).with_suffix('.ifc')
        model = ifcopenshell.open(model_url)
    except OSError:
        print(f"ERROR: please check your model folder : {model_url} does not exist")


import ifcopenshell.util.element

# Get all walls in the IFC file
walls = model.by_type("IfcWall")

# Create a dictionary to store the wall type properties
wall_type_properties = {}

# Iterate over each wall and print its properties
for wall in walls:
    wall_type = ifcopenshell.util.element.get_type(wall)

    # Get selected properties for Walls
    Wall_qtos=(ifcopenshell.util.element.get_psets(wall, qtos_only=True))
    
    # Create a dictionary to map the quantity names to their respective values
    quantity_names = {
        "NetSideArea": Wall_qtos["Qto_WallBaseQuantities"]["NetSideArea"],
        "NetVolume": Wall_qtos["Qto_WallBaseQuantities"]["NetVolume"],
    }

    # Add the wall type properties to the dictionary
    if wall_type.Name not in wall_type_properties:
        wall_type_properties[wall_type.Name] = quantity_names
    else:
        for name, value in quantity_names.items():
            wall_type_properties[wall_type.Name][name] += value

# Print the final list of wall type properties
for wall_type, properties in wall_type_properties.items():
    print(f"Wall Type: {wall_type}")
    for name, value in properties.items():
        print(f"{name} = {value}")