import pygame
import math
import random
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

import win32con
import win32gui

def isRealWindow(hWnd):
    '''Return True iff given window is a real Windows application window.'''
    if not win32gui.IsWindowVisible(hWnd):
        return False
    if win32gui.GetParent(hWnd) != 0:
        return False
    hasNoOwner = win32gui.GetWindow(hWnd, win32con.GW_OWNER) == 0
    lExStyle = win32gui.GetWindowLong(hWnd, win32con.GWL_EXSTYLE)
    if (((lExStyle & win32con.WS_EX_TOOLWINDOW) == 0 and hasNoOwner)
      or ((lExStyle & win32con.WS_EX_APPWINDOW != 0) and not hasNoOwner)):
        if win32gui.GetWindowText(hWnd):
            return True
    return False

def getWindowSizes():
    '''
    Return a list of tuples (handler, (width, height)) for each real window.
    '''
    def callback(hWnd, windows):
        if not isRealWindow(hWnd):
            return
        rect = win32gui.GetWindowRect(hWnd)
        if rect[0] < 0:
            return
        windows.append((hWnd, (rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])))
    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows

for win in getWindowSizes():
    print(win)

#input()

pygame.init()

info = pygame.display.Info()

window_size = (info.current_w,info.current_h)
screen = pygame.display.set_mode(window_size, pygame.NOFRAME | pygame.SRCALPHA)

transparent = (0, 1, 0)


cat_image = pygame.image.load("photos/i.png").convert_alpha()
cat_image = pygame.transform.scale_by(cat_image, 0.5)
misty_size = (cat_image.get_width(),cat_image.get_height())

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparent), 0, win32con.LWA_COLORKEY)


misty_position = muli(window_size,0.5)
misty_velocity = (70,70)

running = True
tick = 0
while running:
    screen.fill(transparent)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Blit the cat image onto the screen
    screen.blit(cat_image, misty_position)

    #misty_position = addi(misty_position, (0,1))
    #misty_position = addi(misty_position,(random.randrange(-10,10),random.randrange(-10,10)))
    misty_position = addi(misty_position, misty_velocity)
    if misty_position[1] + misty_size[1] > window_size[1] or misty_position[1] < 0:
        misty_velocity = (misty_velocity[0]+random.randrange(-5,5), -misty_velocity[1])
        if misty_position[1] > window_size[1]/2:
            misty_position = (misty_position[0], window_size[1]-misty_size[1])
        else:
            misty_position = (misty_position[0], 0)
        pass
    if misty_position[0] + misty_size[0] > window_size[0] or misty_position[0] < 0:
        misty_velocity = (-misty_velocity[0], misty_velocity[1]+random.randrange(-5,5))
        if misty_position[0] > window_size[0]/2:
            misty_position = (window_size[0]-misty_size[0], misty_position[1])
        else:
            misty_position = (0, misty_position[1])
    # Update the display
    pygame.display.flip()
    if tick % 10 == 0:
        alwaysOnTop()
    time.sleep(0.02)
    tick += 1
    pass

pygame.quit()
sys.exit()