from dataclasses import dataclass
import json
def all_archetypes():
    out=[]
    for arch in data:
        out.append(Archetype(**arch))
    return out
@dataclass
class Archetype:
    nom: str
    description: str
    tags: list[str]

# Charge les info du json en mémoire
with open("archetypes.json", "r") as f:
    data: list[dict] = json.load(f)

def load(name: str):
    for arch in data:
        print(arch["nom"])
        if arch["nom"] == name:
            return Archetype(**arch)

    raise ValueError(f"Le nom {name} n'a pas été trouvé comme archetype")