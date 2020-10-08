import json


class Map:
    def __init__(self, save):
        self.savePath = "maps/" + save + ".sav"

    def get_tile(self, x, y):
        map_save = open(self.savePath, "r", encoding="utf-8")
        map_dict = json.loads(map_save.read())
        return map_dict["map"][x][y][0]

