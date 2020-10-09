import graphics

grp = graphics.Graphics("gentest")
active = True


grp.set_tile(1, 1, {"type": "grass"})
grp.set_tile(0, 0, {"type": "stone"})
while active:
    if grp.event_update():
        active = False
    grp.draw()
    grp.update()
    grp.fps(60)
