import win32gui
import win32con
import pygame
import win32api

class WindowManager:
    
    def __init__(self, transparent=(0,2,0)):
        self.hwnd = pygame.display.get_wm_info()["window"]
        self.transparent = transparent
        info = pygame.display.Info()
        self.window_size = (info.current_w,info.current_h)
        pass
    
    def isValidWindow(self, hWnd):
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

    def grabWindows(self):
        '''
        Return a list of tuples (handler, (width, height)) for each real window.
        '''
        def callback(hWnd, windows):
            if not self.isValidWindow(hWnd):
                return
            rect = win32gui.GetWindowRect(hWnd)
            if rect[0] < 0:
                return
            windows.append((hWnd, (rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])))
        windows = []
        win32gui.EnumWindows(callback, windows)
        return windows

    def putAppOnTop(self):
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        pass

    def makeWindowTransparent(self):
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        # set window transparency color
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(*WindowManager.transparent), 0, win32con.LWA_COLORKEY)
        pass
    pass