import pygame
import ctypes
import sys
import win32api
import win32con
import win32gui
import time

def muli(vector, scale):
    return tuple(x * scale for x in vector)

def addi(vector_a, vector_b):
    return tuple(sum(s) for s in zip(vector_a,vector_b))

def subi(vector_a, vector_b):
    return tuple(s[0] - s[1] for s in zip(vector_a,vector_b))

def divi(vector, scale):
    return tuple(x/scale for x in vector)

def alwaysOnTop():    
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

pygame.init()

info = pygame.display.Info()

window_size = (info.current_w,info.current_h)
screen = pygame.display.set_mode(window_size, pygame.NOFRAME | pygame.SRCALPHA)

transparent = (0, 1, 0)

misty_size = (50,200)
cat_image = pygame.image.load("photos/i.png").convert_alpha()
cat_image = pygame.transform.scale_by(cat_image, 0.5)

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparent), 0, win32con.LWA_COLORKEY)


misty_position = muli(window_size,0.5)

running = True
while running:
    screen.fill(transparent)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Blit the cat image onto the screen
    screen.blit(cat_image, misty_position)

    misty_position = addi(misty_position, (0,1))
    
    # Update the display
    pygame.display.flip()
    alwaysOnTop()
    time.sleep(0.1)
    pass

pygame.quit()
sys.exit()