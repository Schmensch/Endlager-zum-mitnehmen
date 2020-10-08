import graphics
import map

grp = graphics.Graphics()
active = True

maptest = map.Map("test")
print(maptest.get_tile(2,2))


while active:
    if grp.event_update():
        active = False

    grp.draw()
    grp.update()
    grp.fps(60)
