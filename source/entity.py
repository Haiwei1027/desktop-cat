from source.vector import *

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

    def contains(self, position):
        top_left = self.position
        bottom_right = addi(self.position, self.animated_sprite.size)
        if position[1] < bottom_right[1] and position[1] > top_left[1]:
            y_contains = True
        else:
            y_contains = False
        if position[0] < bottom_right[0] and position[0] > top_left[0]:
            x_contains = True
        else:
            x_contains = False

        if  y_contains and x_contains:
            return True
        else:
            return False

        pass
    def click(self):

        pass
    pass