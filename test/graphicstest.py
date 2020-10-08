import graphics


grp = graphics.Graphics()
active = True


while active:
    for event in graphics.pygame.event.get():  # close the mainloop on window close
        if event.type == graphics.pygame.QUIT:
            active = False

    grp.draw()
    grp.update()
    grp.fps(60)
