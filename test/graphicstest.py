import graphics

grp = graphics.Graphics()
active = True


grp.set_tile(1, 1, "grass")
grp.set_tile(0, 0, "stone")
while active:
    if grp.event_update():
        active = False
    grp.draw()
    grp.update()
    grp.fps(60)
