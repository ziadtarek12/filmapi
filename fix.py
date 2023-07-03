import json
with open("films.json", "r") as f:
    films = f.read()

films = json.loads(films)
id = 1
for film in films:
    film["id"] = id
    id += 1
    
with open ("films.json", "w") as f:
    f.write(json.dumps(films,indent=4))