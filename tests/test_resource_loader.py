import unittest
import pygame

from source.resource_loader import *

class TestResourceLoader(unittest.TestCase):
    
    def test_images(self):
        
        pygame.init()
        images_path = "resources/photos"
        should_contain = ["misty_sat","misty_move","misty_sleep"]
        
        ResourceLoader.load_images(images_path)
        for file in should_contain:
            self.assertIn(file, ResourceLoader.resources)
            pass
        
        pygame.quit()
        
        pass
    
    
    pass

if __name__ == "__main__":
    unittest.main()
        
