import json


class Map:
    def __init__(self, save):
        self.savePath = "../maps/" + save + ".sav"

    def get_tile(self, x, y):
        map_save = open(self.savePath, "r", encoding="utf-8")
        map_dict = json.loads(map_save.read())
        map_save.close()
        return map_dict["map"][x][y]

    def set_tile(self, x, y, tile):
        map_save = open(self.savePath, "r", encoding="utf-8")
        map_dict = json.loads(map_save.read())
        map_save.close()

        map_dict["map"][x][y] = tile

        with open(self.savePath, "w") as file:
            json.dump(map_dict, file)
        file.close()

    def gen_new_map(self, width, height):
        mapdict = {"map": [], "width": width, "height": height}
        for y in range(0, height):
            mapdict["map"].append([])
            for x in range(0, width):
                mapdict["map"][y].append({"type": "air"})
        with open(self.savePath, "w") as file:
            json.dump(mapdict, file)
        file.close()

    def get_map_size(self):
        map_save = open(self.savePath, "r", encoding="utf-8")
        map_dict = json.loads(map_save.read())
        map_save.close()
        return map_dict["width"], map_dict["height"]
