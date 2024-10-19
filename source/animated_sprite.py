from pygame.surface import Surface

class AnimatedSprite:
    
    def __init__(self, width, height):
        self.surface = Surface(width, height)
        # example format {"misty_sleep":["misty_sleep1","misty_sleep2","misty_sleep3"]}
        self.animation_tracks = {}
        self.animation = ""
        self.pointer = 0
        pass
    
    def update(self):
        # update animation states
        
        # TODO get animation
        
        # TODO blit sprite onto surface
        
        # TODO update pointer with looping
        
        
        pass
    
    def render(self):
        # update surface with image
        pass