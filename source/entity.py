class Entity:
    
    def __init__(self, name, animated_sprite, position=(0,0)):
        self.name = name
        self.animated_sprite = animated_sprite
        self.position = position
        pass
    
    def update(self):
        # update entity states and then update components
        self.animated_sprite.update()
        pass
    
    def render(self, screen):
        # draw entity onto the screen
        self.animated_sprite.render()
        screen.blit(self.animated_sprite.surface, self.position)
        pass
    pass