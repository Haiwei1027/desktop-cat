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
        return all([position[x] < bottom_right[x] and position[x] > top_left[x] for x in range(2)])
    
    def confine(self, bound):
        top_x,top_y = self.position
        size_x, size_y = self.animated_sprite.size
        bottom_x,bottom_y = addi(self.position, self.animated_sprite.size)
        if top_x < bound[0]:
            self.position = setX(self.position, bound[0])
        elif bottom_x > bound[2]:
            self.position = setX(self.position, bound[2] - size_x)
        if top_y < bound[1]:
            self.position = setY(self.position, bound[1])
        elif bottom_y > bound[3]:
            self.position = setY(self.position, bound[3] - size_y)
        pass
    pass