import urllib.request, json

with urllib.request.urlopen("https://www.smashbros.com/assets_v2/data/fighter.json") as url:
    data = json.load(url)
     #print(data)
    json_data = []
    model = "versusfinder_app.character"
    for d in data["fighters"]:
        id = d["id"][-2:]
        #print(id)
        name = str(d["displayName"]["en_US"])
        #print(name)
        json_data.append({
                        'model': model,
                        'pk': id,
                        'fields': {
                            'game_id' : 1,
                            'name' : name
                            }
                     })

    #print(json.dumps(json_data))
    with open('fighters.json', 'w') as outfile:
        json.dump(json_data, outfile)
