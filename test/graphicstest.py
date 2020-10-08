import graphics

grp = graphics.Graphics()
active = True



while active:
    if grp.event_update():
        active = False

    grp.draw()
    grp.update()
    grp.fps(60)
