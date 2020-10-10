class Button:
    def __init__(self, image, position, callback, name):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.callback = callback
        self.name = name
        self.disabled = False

    def on_click(self, event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                if not self.disabled:
                    self.callback(self)

