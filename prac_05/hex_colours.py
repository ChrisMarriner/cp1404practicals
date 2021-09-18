"""
Christopher Marriner
CP1404 Practical
Hex Colours Program
"""

HEX_COLOURS = {"black": "#000000", "blue": "#0000ff", "brown": "#a52a2a", "gray": "#bebebe", "green": "#00ff00",
               "orange": "ffa500", "pink": "#ffc0cb", "purple": "#a020f0", "red": "#ff0000", "Yellow": "#ffff00"}
print(HEX_COLOURS)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print(colour_name, "is", HEX_COLOURS[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
