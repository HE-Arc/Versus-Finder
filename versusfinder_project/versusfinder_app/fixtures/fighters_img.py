import urllib.request, json

with urllib.request.urlopen("https://www.smashbros.com/assets_v2/data/fighter.json") as url:
    data = json.load(url)
     #print(data)
    json_data = []
    model = "versusfinder_app.character"
    for d in data["fighters"]:
        try:
            urllib.request.urlretrieve("https://www.smashbros.com/assets_v2/img/fighter/thumb_v/"+(((d["displayName"]["en_US"]).lower()).replace(" ", "_")).replace(".","")+".png", "./../img/"+(d["displayName"]["en_US"]).replace(" ", "_")+".png")
        except:
            print(d["displayName"]["en_US"])