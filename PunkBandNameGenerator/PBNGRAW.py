import random

first_name = [
    "Dead",
    "Rotten",
    "Ugly",
    "Nervous",
    "Sick",
    "Fast",
    "Plastic",
    "Savage",
    "Cheap",
    "Dumb",
    "Broken",
    "Toxic",
    "Cracked",
    "Filthy",
    "Lame",
    "Stupid",
    "Greasy",
    "Paranoid",
    "Empty",
    "Illegal",
]

last_name = [
    "Rats",
    "Bricks",
    "Teeth",
    "Cigs",
    "Bones",
    "Kids",
    "Knives",
    "Trash",
    "Freaks",
    "Coffins",
    "Needles",
    "Doom",
    "Pills",
    "Vans",
    "Guts",
    "Threats",
    "Hooks",
    "Boots",
    "Chains",
    "Punches",
]


optional_addon = [
    "in the Microwave",
    "of Suburbia",
    "from Hell",
    "on Fire",
    "at Walmart",
    "& the Trauma",
    "vs the World",
    "in Detention",
    "Reloaded",
    "2025",
    "With the stuff",
    "on VHS",
    "ft. LoblachiPanMan",
]

print(f"{random.choice(first_name)} {random.choice(last_name)} {random.choice(optional_addon) if random.randint(0,1) == 1 else ""}")