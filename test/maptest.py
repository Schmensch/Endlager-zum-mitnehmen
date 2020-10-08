import map

genmap = map.Map("gentest")

genmap.gen_new_map(4, 4)
print(genmap.get_tile(3, 3))
print(genmap.get_map_size())
