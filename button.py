class Button:
    def __init__(self, image, image_hover, image_clicked, position, callback, name):
        self.image_default = image
        self.image_hover = image_hover
        self.image_clicked = image_clicked
        self.image = self.image_default
        self.rect = image.get_rect(topleft=position)
        self.callback = callback
        self.name = name
        self.disabled = False
        self.no_hover = False

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.no_hover = True
            if not self.disabled:
                self.image = self.image_clicked

    def on_release(self, event):
        self.no_hover = False
        if self.rect.collidepoint(event.pos):
            if not self.disabled:
                self.image = self.image_default
                self.callback(self)

    def on_hover(self, event):
        if self.rect.collidepoint(event.pos):
            if not self.no_hover:
                if not self.disabled:
                    self.image = self.image_hover
        else:
            if not self.disabled:
                self.image = self.image_default

