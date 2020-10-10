import graphics

grp = graphics.Graphics("gentest")
active = True

grp.set_tile(1, 1, {"type": "stone"})
grp.set_tile(0, 0, {"type": "grass"})
while active:
    if grp.event_update():
        active = False
    grp.draw()
    grp.update()
    grp.fps(60)
    # grp.set_tile(1, 1, {"type": "air"})
    # grp.set_tile(0, 0, {"type": "air"})
