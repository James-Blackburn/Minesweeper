class Text:

    """
    Arguments
    ---------
    display = pygame window
    x = text x (center)
    y = text y (center)
    text = text string
    font = text font
    text_colour = colour of text
    """

    def __init__(self,display,x,y,text,font,text_colour):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.display = display
        self.text_colour = text_colour

        message = self.font.render(self.text, 1, self.text_colour)
        text_rect = message.get_rect(center=(self.x, self.y))
        self.display.blit(message, text_rect)

    def update(self,x,y,text):
        self.x = x
        self.y = y
        self.text = text
        message = self.font.render(self.text, 1, self.text_colour)
        text_rect = message.get_rect(center=(self.x, self.y))
        self.display.blit(message, text_rect)
